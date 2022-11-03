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

class UeberCompetenceModificationDto(object):
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
        'ueber_competence_id': 'str',
        'nested_competencies': 'list[str]',
        'nested_ueber_competencies': 'list[str]'
    }

    attribute_map = {
        'ueber_competence_id': 'ueberCompetenceId',
        'nested_competencies': 'nestedCompetencies',
        'nested_ueber_competencies': 'nestedUeberCompetencies'
    }

    def __init__(self, ueber_competence_id=None, nested_competencies=None, nested_ueber_competencies=None):  # noqa: E501
        """UeberCompetenceModificationDto - a model defined in Swagger"""  # noqa: E501
        self._ueber_competence_id = None
        self._nested_competencies = None
        self._nested_ueber_competencies = None
        self.discriminator = None
        self.ueber_competence_id = ueber_competence_id
        self.nested_competencies = nested_competencies
        self.nested_ueber_competencies = nested_ueber_competencies

    @property
    def ueber_competence_id(self):
        """Gets the ueber_competence_id of this UeberCompetenceModificationDto.  # noqa: E501


        :return: The ueber_competence_id of this UeberCompetenceModificationDto.  # noqa: E501
        :rtype: str
        """
        return self._ueber_competence_id

    @ueber_competence_id.setter
    def ueber_competence_id(self, ueber_competence_id):
        """Sets the ueber_competence_id of this UeberCompetenceModificationDto.


        :param ueber_competence_id: The ueber_competence_id of this UeberCompetenceModificationDto.  # noqa: E501
        :type: str
        """
        if ueber_competence_id is None:
            raise ValueError("Invalid value for `ueber_competence_id`, must not be `None`")  # noqa: E501

        self._ueber_competence_id = ueber_competence_id

    @property
    def nested_competencies(self):
        """Gets the nested_competencies of this UeberCompetenceModificationDto.  # noqa: E501


        :return: The nested_competencies of this UeberCompetenceModificationDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._nested_competencies

    @nested_competencies.setter
    def nested_competencies(self, nested_competencies):
        """Sets the nested_competencies of this UeberCompetenceModificationDto.


        :param nested_competencies: The nested_competencies of this UeberCompetenceModificationDto.  # noqa: E501
        :type: list[str]
        """
        if nested_competencies is None:
            raise ValueError("Invalid value for `nested_competencies`, must not be `None`")  # noqa: E501

        self._nested_competencies = nested_competencies

    @property
    def nested_ueber_competencies(self):
        """Gets the nested_ueber_competencies of this UeberCompetenceModificationDto.  # noqa: E501


        :return: The nested_ueber_competencies of this UeberCompetenceModificationDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._nested_ueber_competencies

    @nested_ueber_competencies.setter
    def nested_ueber_competencies(self, nested_ueber_competencies):
        """Sets the nested_ueber_competencies of this UeberCompetenceModificationDto.


        :param nested_ueber_competencies: The nested_ueber_competencies of this UeberCompetenceModificationDto.  # noqa: E501
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
        if issubclass(UeberCompetenceModificationDto, dict):
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
        if not isinstance(other, UeberCompetenceModificationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other