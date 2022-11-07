# swagger_client.CompetenciesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repository_mgmt_controller_add_competence**](CompetenciesApi.md#repository_mgmt_controller_add_competence) | **POST** /repositories/{repositoryId}/competencies/add_competence | 
[**repository_mgmt_controller_add_ueber_competence**](CompetenciesApi.md#repository_mgmt_controller_add_ueber_competence) | **POST** /repositories/{repositoryId}/competencies/add_uebercompetence | 
[**repository_mgmt_controller_create_repository**](CompetenciesApi.md#repository_mgmt_controller_create_repository) | **POST** /repositories/create | 
[**repository_mgmt_controller_list_repositories**](CompetenciesApi.md#repository_mgmt_controller_list_repositories) | **GET** /repositories/showOwn | 
[**repository_mgmt_controller_load_repository**](CompetenciesApi.md#repository_mgmt_controller_load_repository) | **GET** /repositories/{repositoryId} | 
[**repository_mgmt_controller_load_resolved_repository**](CompetenciesApi.md#repository_mgmt_controller_load_resolved_repository) | **GET** /repositories/resolve/{repositoryId} | 
[**repository_mgmt_controller_modify**](CompetenciesApi.md#repository_mgmt_controller_modify) | **PATCH** /repositories/{repositoryId}/competencies/modify_uebercompetence | 
[**repository_mgmt_controller_resolve_to_competencies**](CompetenciesApi.md#repository_mgmt_controller_resolve_to_competencies) | **POST** /repositories/{repositoryId}/resolveUberCompetencies | 
[**repository_mgmt_controller_search_for_repositories**](CompetenciesApi.md#repository_mgmt_controller_search_for_repositories) | **POST** /repositories | 

# **repository_mgmt_controller_add_competence**
> CompetenceDto repository_mgmt_controller_add_competence(body, repository_id)



Creates a new competence at the specified repository and returns the created competence.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompetenciesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompetenceCreationDto() # CompetenceCreationDto | 
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.repository_mgmt_controller_add_competence(body, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompetenciesApi->repository_mgmt_controller_add_competence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompetenceCreationDto**](CompetenceCreationDto.md)|  | 
 **repository_id** | **str**|  | 

### Return type

[**CompetenceDto**](CompetenceDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_mgmt_controller_add_ueber_competence**
> UnResolvedUeberCompetenceDto repository_mgmt_controller_add_ueber_competence(body, repository_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompetenciesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UeberCompetenceCreationDto() # UeberCompetenceCreationDto | 
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.repository_mgmt_controller_add_ueber_competence(body, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompetenciesApi->repository_mgmt_controller_add_ueber_competence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UeberCompetenceCreationDto**](UeberCompetenceCreationDto.md)|  | 
 **repository_id** | **str**|  | 

### Return type

[**UnResolvedUeberCompetenceDto**](UnResolvedUeberCompetenceDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_mgmt_controller_create_repository**
> RepositoryDto repository_mgmt_controller_create_repository(body)



Creates a new competence repository for the specified user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompetenciesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RepositoryCreationDto() # RepositoryCreationDto | 

try:
    api_response = api_instance.repository_mgmt_controller_create_repository(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompetenciesApi->repository_mgmt_controller_create_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepositoryCreationDto**](RepositoryCreationDto.md)|  | 

### Return type

[**RepositoryDto**](RepositoryDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_mgmt_controller_list_repositories**
> RepositoryListDto repository_mgmt_controller_list_repositories()



Lists all repositories of the specified user, without showing its content.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompetenciesApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.repository_mgmt_controller_list_repositories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompetenciesApi->repository_mgmt_controller_list_repositories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RepositoryListDto**](RepositoryListDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_mgmt_controller_load_repository**
> UnresolvedRepositoryDto repository_mgmt_controller_load_repository(repository_id)



Returns one repository and its unresolved elements. Competences and their relations are handled as IDs and need to be resolved on the client-side.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompetenciesApi(swagger_client.ApiClient(configuration))
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.repository_mgmt_controller_load_repository(repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompetenciesApi->repository_mgmt_controller_load_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**|  | 

### Return type

[**UnresolvedRepositoryDto**](UnresolvedRepositoryDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_mgmt_controller_load_resolved_repository**
> ResolvedRepositoryDto repository_mgmt_controller_load_resolved_repository(repository_id)



Returns one resolved repository and its elements. Competencies and their relations are resolved at the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompetenciesApi(swagger_client.ApiClient(configuration))
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.repository_mgmt_controller_load_resolved_repository(repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompetenciesApi->repository_mgmt_controller_load_resolved_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**|  | 

### Return type

[**ResolvedRepositoryDto**](ResolvedRepositoryDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_mgmt_controller_modify**
> UnResolvedUeberCompetenceDto repository_mgmt_controller_modify(body, repository_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompetenciesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UeberCompetenceModificationDto() # UeberCompetenceModificationDto | 
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.repository_mgmt_controller_modify(body, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompetenciesApi->repository_mgmt_controller_modify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UeberCompetenceModificationDto**](UeberCompetenceModificationDto.md)|  | 
 **repository_id** | **str**|  | 

### Return type

[**UnResolvedUeberCompetenceDto**](UnResolvedUeberCompetenceDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_mgmt_controller_resolve_to_competencies**
> CompetenceListDto repository_mgmt_controller_resolve_to_competencies(body, repository_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompetenciesApi()
body = swagger_client.UberCompetenceResolveRequestDto() # UberCompetenceResolveRequestDto | 
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.repository_mgmt_controller_resolve_to_competencies(body, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompetenciesApi->repository_mgmt_controller_resolve_to_competencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UberCompetenceResolveRequestDto**](UberCompetenceResolveRequestDto.md)|  | 
 **repository_id** | **str**|  | 

### Return type

[**CompetenceListDto**](CompetenceListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_mgmt_controller_search_for_repositories**
> RepositoryListDto repository_mgmt_controller_search_for_repositories(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompetenciesApi()
body = swagger_client.RepositorySearchDto() # RepositorySearchDto | 

try:
    api_response = api_instance.repository_mgmt_controller_search_for_repositories(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompetenciesApi->repository_mgmt_controller_search_for_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepositorySearchDto**](RepositorySearchDto.md)|  | 

### Return type

[**RepositoryListDto**](RepositoryListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

