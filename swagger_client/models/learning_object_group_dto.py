# coding: utf-8

"""
    Competence Repository

    The API description of the Competence Repository.  # noqa: E501

    OpenAPI spec version: 0.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LearningObjectGroupDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'repository_id': 'str',
        'name': 'str',
        'description': 'str',
        'nested_learning_objects': 'list[LearningObjectDto]',
        'nested_groups': 'list[LearningObjectGroupDto]'
    }

    attribute_map = {
        'id': 'id',
        'repository_id': 'repositoryId',
        'name': 'name',
        'description': 'description',
        'nested_learning_objects': 'nestedLearningObjects',
        'nested_groups': 'nestedGroups'
    }

    def __init__(self, id=None, repository_id=None, name=None, description=None, nested_learning_objects=None, nested_groups=None):  # noqa: E501
        """LearningObjectGroupDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._repository_id = None
        self._name = None
        self._description = None
        self._nested_learning_objects = None
        self._nested_groups = None
        self.discriminator = None
        self.id = id
        self.repository_id = repository_id
        self.name = name
        if description is not None:
            self.description = description
        self.nested_learning_objects = nested_learning_objects
        self.nested_groups = nested_groups

    @property
    def id(self):
        """Gets the id of this LearningObjectGroupDto.  # noqa: E501


        :return: The id of this LearningObjectGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LearningObjectGroupDto.


        :param id: The id of this LearningObjectGroupDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def repository_id(self):
        """Gets the repository_id of this LearningObjectGroupDto.  # noqa: E501


        :return: The repository_id of this LearningObjectGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this LearningObjectGroupDto.


        :param repository_id: The repository_id of this LearningObjectGroupDto.  # noqa: E501
        :type: str
        """
        if repository_id is None:
            raise ValueError("Invalid value for `repository_id`, must not be `None`")  # noqa: E501

        self._repository_id = repository_id

    @property
    def name(self):
        """Gets the name of this LearningObjectGroupDto.  # noqa: E501


        :return: The name of this LearningObjectGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LearningObjectGroupDto.


        :param name: The name of this LearningObjectGroupDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this LearningObjectGroupDto.  # noqa: E501


        :return: The description of this LearningObjectGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LearningObjectGroupDto.


        :param description: The description of this LearningObjectGroupDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def nested_learning_objects(self):
        """Gets the nested_learning_objects of this LearningObjectGroupDto.  # noqa: E501


        :return: The nested_learning_objects of this LearningObjectGroupDto.  # noqa: E501
        :rtype: list[LearningObjectDto]
        """
        return self._nested_learning_objects

    @nested_learning_objects.setter
    def nested_learning_objects(self, nested_learning_objects):
        """Sets the nested_learning_objects of this LearningObjectGroupDto.


        :param nested_learning_objects: The nested_learning_objects of this LearningObjectGroupDto.  # noqa: E501
        :type: list[LearningObjectDto]
        """
        if nested_learning_objects is None:
            raise ValueError("Invalid value for `nested_learning_objects`, must not be `None`")  # noqa: E501

        self._nested_learning_objects = nested_learning_objects

    @property
    def nested_groups(self):
        """Gets the nested_groups of this LearningObjectGroupDto.  # noqa: E501


        :return: The nested_groups of this LearningObjectGroupDto.  # noqa: E501
        :rtype: list[LearningObjectGroupDto]
        """
        return self._nested_groups

    @nested_groups.setter
    def nested_groups(self, nested_groups):
        """Sets the nested_groups of this LearningObjectGroupDto.


        :param nested_groups: The nested_groups of this LearningObjectGroupDto.  # noqa: E501
        :type: list[LearningObjectGroupDto]
        """
        if nested_groups is None:
            raise ValueError("Invalid value for `nested_groups`, must not be `None`")  # noqa: E501

        self._nested_groups = nested_groups

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LearningObjectGroupDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LearningObjectGroupDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
