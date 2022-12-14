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

class RepositoryCreationDto(object):
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
        'description': 'str',
        'taxonomy': 'str',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'description': 'description',
        'taxonomy': 'taxonomy',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, description=None, taxonomy=None, name=None, version=None):  # noqa: E501
        """RepositoryCreationDto - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._taxonomy = None
        self._name = None
        self._version = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if taxonomy is not None:
            self.taxonomy = taxonomy
        self.name = name
        if version is not None:
            self.version = version

    @property
    def description(self):
        """Gets the description of this RepositoryCreationDto.  # noqa: E501


        :return: The description of this RepositoryCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RepositoryCreationDto.


        :param description: The description of this RepositoryCreationDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def taxonomy(self):
        """Gets the taxonomy of this RepositoryCreationDto.  # noqa: E501


        :return: The taxonomy of this RepositoryCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._taxonomy

    @taxonomy.setter
    def taxonomy(self, taxonomy):
        """Sets the taxonomy of this RepositoryCreationDto.


        :param taxonomy: The taxonomy of this RepositoryCreationDto.  # noqa: E501
        :type: str
        """

        self._taxonomy = taxonomy

    @property
    def name(self):
        """Gets the name of this RepositoryCreationDto.  # noqa: E501


        :return: The name of this RepositoryCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepositoryCreationDto.


        :param name: The name of this RepositoryCreationDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this RepositoryCreationDto.  # noqa: E501


        :return: The version of this RepositoryCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RepositoryCreationDto.


        :param version: The version of this RepositoryCreationDto.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(RepositoryCreationDto, dict):
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
        if not isinstance(other, RepositoryCreationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
