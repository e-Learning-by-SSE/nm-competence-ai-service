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

class UnResolvedUeberCompetenceDto(object):
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
        'name': 'str',
        'description': 'str',
        'id': 'str',
        'parents': 'list[str]',
        'nested_competencies': 'list[str]',
        'nested_ueber_competencies': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'parents': 'parents',
        'nested_competencies': 'nestedCompetencies',
        'nested_ueber_competencies': 'nestedUeberCompetencies'
    }

    def __init__(self, name=None, description=None, id=None, parents=None, nested_competencies=None, nested_ueber_competencies=None):  # noqa: E501
        """UnResolvedUeberCompetenceDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._id = None
        self._parents = None
        self._nested_competencies = None
        self._nested_ueber_competencies = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.id = id
        self.parents = parents
        self.nested_competencies = nested_competencies
        self.nested_ueber_competencies = nested_ueber_competencies

    @property
    def name(self):
        """Gets the name of this UnResolvedUeberCompetenceDto.  # noqa: E501


        :return: The name of this UnResolvedUeberCompetenceDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UnResolvedUeberCompetenceDto.


        :param name: The name of this UnResolvedUeberCompetenceDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this UnResolvedUeberCompetenceDto.  # noqa: E501


        :return: The description of this UnResolvedUeberCompetenceDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UnResolvedUeberCompetenceDto.


        :param description: The description of this UnResolvedUeberCompetenceDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this UnResolvedUeberCompetenceDto.  # noqa: E501


        :return: The id of this UnResolvedUeberCompetenceDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnResolvedUeberCompetenceDto.


        :param id: The id of this UnResolvedUeberCompetenceDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def parents(self):
        """Gets the parents of this UnResolvedUeberCompetenceDto.  # noqa: E501


        :return: The parents of this UnResolvedUeberCompetenceDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this UnResolvedUeberCompetenceDto.


        :param parents: The parents of this UnResolvedUeberCompetenceDto.  # noqa: E501
        :type: list[str]
        """
        if parents is None:
            raise ValueError("Invalid value for `parents`, must not be `None`")  # noqa: E501

        self._parents = parents

    @property
    def nested_competencies(self):
        """Gets the nested_competencies of this UnResolvedUeberCompetenceDto.  # noqa: E501


        :return: The nested_competencies of this UnResolvedUeberCompetenceDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._nested_competencies

    @nested_competencies.setter
    def nested_competencies(self, nested_competencies):
        """Sets the nested_competencies of this UnResolvedUeberCompetenceDto.


        :param nested_competencies: The nested_competencies of this UnResolvedUeberCompetenceDto.  # noqa: E501
        :type: list[str]
        """
        if nested_competencies is None:
            raise ValueError("Invalid value for `nested_competencies`, must not be `None`")  # noqa: E501

        self._nested_competencies = nested_competencies

    @property
    def nested_ueber_competencies(self):
        """Gets the nested_ueber_competencies of this UnResolvedUeberCompetenceDto.  # noqa: E501


        :return: The nested_ueber_competencies of this UnResolvedUeberCompetenceDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._nested_ueber_competencies

    @nested_ueber_competencies.setter
    def nested_ueber_competencies(self, nested_ueber_competencies):
        """Sets the nested_ueber_competencies of this UnResolvedUeberCompetenceDto.


        :param nested_ueber_competencies: The nested_ueber_competencies of this UnResolvedUeberCompetenceDto.  # noqa: E501
        :type: list[str]
        """
        if nested_ueber_competencies is None:
            raise ValueError("Invalid value for `nested_ueber_competencies`, must not be `None`")  # noqa: E501

        self._nested_ueber_competencies = nested_ueber_competencies

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
        if issubclass(UnResolvedUeberCompetenceDto, dict):
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
        if not isinstance(other, UnResolvedUeberCompetenceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
