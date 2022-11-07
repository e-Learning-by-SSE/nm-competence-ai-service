from flask import Flask, request
import json, jsonschema
from jsonschema import validate
from flask_restx import Api, Resource, fields



import swagger_client
import json
from swagger_client.rest import ApiException
import networkx as nx
gr = nx.DiGraph()


configuration = swagger_client.Configuration()


configuration.api_key_prefix['Authorization'] = 'Bearer'
api_client = swagger_client.ApiClient(configuration=configuration)
api_instance = swagger_client.AuthenticationApi()
repApi = swagger_client.CompetenciesApi(api_client)
loApi = swagger_client.LearningObjectsApi()


flask_app = Flask(__name__)
app = Api(app = flask_app, version='0.2', title='SSE', description='Web service')

cmr = app.namespace('PAth Finder', path='/pathFinder', description='APIs for the Path Finder')

proofPath_request_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'timestamp': {'type': 'integer'},
        'event': {'type': 'string'},
        'user_id': {'type': 'string'},
        'user_token': {'type': 'string'},
        'rep_id': {'type': 'integer'},
        'goal_id': {'type': 'integer'}},
    'required': ['id', 'timestamp', 'event', 'user_id', 'user_token','rep_id', 'goal_id'],
}
token=''


proof_path_dto = app.schema_model('Proof Path DTO', proofPath_request_schema)



def addEdgeforList(comp, graph ):
    for nestedcomp in comp.nested_competencies:
        graph.add_edge(nestedcomp.id,comp.id+'ueber', art='neestedComp' )
    for nestedubercomp in comp.nested_ueber_competencies:    
        graph.add_edge(nestedubercomp.id+'ueber',comp.id+'ueber', art='neestedueberComp')
        print('add ',nestedubercomp.id+'ueber',comp.id+'ueber')
        if nestedubercomp.nested_ueber_competencies:
            for nestcomp in nestedubercomp.nested_ueber_competencies:
                addEdgeforList(nestcomp, graph )

def find_LO_for_competence(competence):
    for lo in my_lo.learning_objects:
        try:
            api_response = loApi.lo_repository_controller_load_learning_object(learning_object_id=lo.id)
            print(api_response.name)
        except ApiException as e:
            print("Exception when calling Api-> %s\n" % e)

@cmr.route('/hello_world')
class Hello(Resource):
    def get(self, **kwargs):
        return 'Hello'
      
@cmr.route('/find/')
class Concept_Map_Prediction(Resource):
    @cmr.expect(proof_path_dto, validate=True)
    def post(self):
        if request.is_json:
            data = request.get_json()
            token= data.get('user_token')
            api_client.set_default_header('Authorization', 'Bearer ' +token)
            try:
    # Get list of exposure types
                my_competencies = repApi.repository_mgmt_controller_load_resolved_repository (repository_id=1)
                print(my_competencies)
            except ApiException as e:
                print("Exception when calling Api-> %s\n" % e)
            
            try:
                my_lo = loApi.lo_repository_controller_load_repository(repository_id=1)
                print(my_lo)
            except ApiException as e:
                print("Exception when calling Api-> %s\n" % e)
            
            my_LO_complete = []   
            for lo in my_lo.learning_objects:    
                try:
                    print(lo.id)
                    my_LO_complete.append(loApi.lo_repository_controller_load_learning_object(learning_object_id=lo.id))
                except ApiException as e:
                    print("Exception when calling Api-> %s\n" % e)
            print(my_LO_complete)
            for comp in my_competencies.competencies:
                gr.add_node(comp.id, name=comp.description, art='Kompetenz')
            for comp in my_competencies.ueber_competencies:
                gr.add_node(comp.id+'ueber', name=comp.description, art='Ueber_Kompetenz')
                addEdgeforList(comp, gr )
            grLO = nx.DiGraph()
            grLO.add_node('Know nothing', subset='Start')
            for comp in my_competencies.competencies:
                grLO.add_node(comp.id, name=comp.description, subset='Kompetenz')
           #for comp in my_competencies.ueber_competencies:
             #   grLO.add_node(comp.id+'ueber', name=comp.description, subset='Ueber_Kompetenz')
          #  addEdgeforList(comp, grLO )
            for lo in my_LO_complete:
                grLO.add_node(lo.id+'Lo', name=lo.description, subset='LO')
                if not lo.required_competencies:
                    if not lo.required_ueber_competencies: 
                        grLO.add_edge( 'Know nothing',lo.id+'Lo', art = 'required_comp')
                for nestcomp in lo.offered_competencies:
                    grLO.add_edge(lo.id+'Lo', nestcomp, art = 'offered_comp')
                for nestcomp in lo.required_competencies:
                    grLO.add_edge(nestcomp,lo.id+'Lo', art = 'required_comp')    
                for nestcomp in lo.offered_ueber_competencies:
                    grLO.add_edge(lo.id+'Lo', nestcomp+'ueber', art = 'offered_ueber_comp')
                for nestcomp in lo.required_ueber_competencies:
                    grLO.add_edge(nestcomp+'ueber',lo.id+'Lo', art = 'required_ueber_comp')  
                mylist=list(nx.bfs_tree(grLO, source='Know nothing', depth_limit=20).edges())
                print(mylist)
                G=nx.from_edgelist(list(nx.bfs_tree(grLO, source='Know nothing', depth_limit=20).edges()))
                G1 = nx.DiGraph()
                G1.add_edges_from(G.edges) 
                lst=[]
                for x,y in mylist: 
                    if x.find('Lo') != -1:
        
                        lst.append(x) if x not in lst else lst
                print(lst) 
            return lst, 200
        return {"Error": "Request must be JSON"}, 415 # 415 means Unsupported media type