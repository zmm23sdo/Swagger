# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class User(object):
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
        'uuid': 'str',
        'username': 'str',
        'name': 'str',
        'email': 'str',
        'deleted_at': 'str',
        'created_at': 'str',
        'roles': 'list[UserRole]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'username': 'username',
        'name': 'name',
        'email': 'email',
        'deleted_at': 'deleted_at',
        'created_at': 'created_at',
        'roles': 'roles'
    }

    def __init__(self, uuid=None, username=None, name=None, email=None, deleted_at=None, created_at=None, roles=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._username = None
        self._name = None
        self._email = None
        self._deleted_at = None
        self._created_at = None
        self._roles = None
        self.discriminator = None
        self.uuid = uuid
        self.username = username
        self.name = name
        self.email = email
        self.deleted_at = deleted_at
        self.created_at = created_at
        self.roles = roles

    @property
    def uuid(self):
        """Gets the uuid of this User.  # noqa: E501

         用户ID  # noqa: E501

        :return: The uuid of this User.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this User.

         用户ID  # noqa: E501

        :param uuid: The uuid of this User.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501

         用户名,系统内唯一  # noqa: E501

        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.

         用户名,系统内唯一  # noqa: E501

        :param username: The username of this User.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501

         用户昵称  # noqa: E501

        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.

         用户昵称  # noqa: E501

        :param name: The name of this User.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

         用户邮箱  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

         用户邮箱  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def deleted_at(self):
        """Gets the deleted_at of this User.  # noqa: E501

         用户删除时间 , 有值:已注销, 空值:正常  # noqa: E501

        :return: The deleted_at of this User.  # noqa: E501
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this User.

         用户删除时间 , 有值:已注销, 空值:正常  # noqa: E501

        :param deleted_at: The deleted_at of this User.  # noqa: E501
        :type: str
        """
        if deleted_at is None:
            raise ValueError("Invalid value for `deleted_at`, must not be `None`")  # noqa: E501

        self._deleted_at = deleted_at

    @property
    def created_at(self):
        """Gets the created_at of this User.  # noqa: E501

         创建时间  # noqa: E501

        :return: The created_at of this User.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.

         创建时间  # noqa: E501

        :param created_at: The created_at of this User.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def roles(self):
        """Gets the roles of this User.  # noqa: E501

         角色信息集合  # noqa: E501

        :return: The roles of this User.  # noqa: E501
        :rtype: list[UserRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this User.

         角色信息集合  # noqa: E501

        :param roles: The roles of this User.  # noqa: E501
        :type: list[UserRole]
        """
        if roles is None:
            raise ValueError("Invalid value for `roles`, must not be `None`")  # noqa: E501

        self._roles = roles

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
