# coding: utf-8

# flake8: noqa

"""
    Competence Repository

    The API description of the Competence Repository.  # noqa: E501

    OpenAPI spec version: 0.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.authentication_api import AuthenticationApi
from swagger_client.api.competencies_api import CompetenciesApi
from swagger_client.api.learning_objects_api import LearningObjectsApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.auth_dto import AuthDto
from swagger_client.models.competence_creation_dto import CompetenceCreationDto
from swagger_client.models.competence_dto import CompetenceDto
from swagger_client.models.competence_list_dto import CompetenceListDto
from swagger_client.models.learning_object_creation_dto import LearningObjectCreationDto
from swagger_client.models.learning_object_dto import LearningObjectDto
from swagger_client.models.learning_object_group_dto import LearningObjectGroupDto
from swagger_client.models.learning_object_modification_dto import LearningObjectModificationDto
from swagger_client.models.lo_goal_creation_dto import LoGoalCreationDto
from swagger_client.models.lo_goal_dto import LoGoalDto
from swagger_client.models.lo_repository_creation_dto import LoRepositoryCreationDto
from swagger_client.models.lo_repository_dto import LoRepositoryDto
from swagger_client.models.lo_repository_list_dto import LoRepositoryListDto
from swagger_client.models.lo_repository_modify_dto import LoRepositoryModifyDto
from swagger_client.models.login_ack_dto import LoginAckDto
from swagger_client.models.login_dto import LoginDto
from swagger_client.models.repository_creation_dto import RepositoryCreationDto
from swagger_client.models.repository_dto import RepositoryDto
from swagger_client.models.repository_list_dto import RepositoryListDto
from swagger_client.models.repository_search_dto import RepositorySearchDto
from swagger_client.models.resolved_repository_dto import ResolvedRepositoryDto
from swagger_client.models.resolved_ueber_competence_dto import ResolvedUeberCompetenceDto
from swagger_client.models.shallow_lo_repository_dto import ShallowLoRepositoryDto
from swagger_client.models.uber_competence_resolve_request_dto import UberCompetenceResolveRequestDto
from swagger_client.models.ueber_competence_creation_dto import UeberCompetenceCreationDto
from swagger_client.models.ueber_competence_modification_dto import UeberCompetenceModificationDto
from swagger_client.models.un_resolved_ueber_competence_dto import UnResolvedUeberCompetenceDto
from swagger_client.models.unresolved_repository_dto import UnresolvedRepositoryDto
