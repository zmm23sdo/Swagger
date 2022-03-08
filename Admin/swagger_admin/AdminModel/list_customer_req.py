# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ListCustomerReq(object):
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
        'page': 'int',
        'page_size': 'int',
        'orderby': 'str',
        'sort': 'str',
        'name': 'str',
        'is_deleted_at': 'str',
        'created_at_start': 'str',
        'created_at_end': 'str',
        'last_at_start': 'str',
        'last_at_end': 'str'
    }

    attribute_map = {
        'page': 'page',
        'page_size': 'page_size',
        'orderby': 'orderby',
        'sort': 'sort',
        'name': 'name',
        'is_deleted_at': 'is_deleted_at',
        'created_at_start': 'created_at_start',
        'created_at_end': 'created_at_end',
        'last_at_start': 'last_at_start',
        'last_at_end': 'last_at_end'
    }

    def __init__(self, page=None, page_size=15, orderby='created_at', sort='desc', name=None, is_deleted_at=None, created_at_start=None, created_at_end=None, last_at_start=None, last_at_end=None):  # noqa: E501
        """ListCustomerReq - a model defined in Swagger"""  # noqa: E501
        self._page = None
        self._page_size = None
        self._orderby = None
        self._sort = None
        self._name = None
        self._is_deleted_at = None
        self._created_at_start = None
        self._created_at_end = None
        self._last_at_start = None
        self._last_at_end = None
        self.discriminator = None
        self.page = page
        if page_size is not None:
            self.page_size = page_size
        if orderby is not None:
            self.orderby = orderby
        if sort is not None:
            self.sort = sort
        if name is not None:
            self.name = name
        if is_deleted_at is not None:
            self.is_deleted_at = is_deleted_at
        if created_at_start is not None:
            self.created_at_start = created_at_start
        if created_at_end is not None:
            self.created_at_end = created_at_end
        if last_at_start is not None:
            self.last_at_start = last_at_start
        if last_at_end is not None:
            self.last_at_end = last_at_end

    @property
    def page(self):
        """Gets the page of this ListCustomerReq.  # noqa: E501

         当前页码  # noqa: E501

        :return: The page of this ListCustomerReq.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListCustomerReq.

         当前页码  # noqa: E501

        :param page: The page of this ListCustomerReq.  # noqa: E501
        :type: int
        """
        if page is None:
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ListCustomerReq.  # noqa: E501

         展示数量 默认15  # noqa: E501

        :return: The page_size of this ListCustomerReq.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListCustomerReq.

         展示数量 默认15  # noqa: E501

        :param page_size: The page_size of this ListCustomerReq.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def orderby(self):
        """Gets the orderby of this ListCustomerReq.  # noqa: E501

         排序字段,默认 created_at  # noqa: E501

        :return: The orderby of this ListCustomerReq.  # noqa: E501
        :rtype: str
        """
        return self._orderby

    @orderby.setter
    def orderby(self, orderby):
        """Sets the orderby of this ListCustomerReq.

         排序字段,默认 created_at  # noqa: E501

        :param orderby: The orderby of this ListCustomerReq.  # noqa: E501
        :type: str
        """

        self._orderby = orderby

    @property
    def sort(self):
        """Gets the sort of this ListCustomerReq.  # noqa: E501

         排序方式(asc,desc), 默认 desc  # noqa: E501

        :return: The sort of this ListCustomerReq.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListCustomerReq.

         排序方式(asc,desc), 默认 desc  # noqa: E501

        :param sort: The sort of this ListCustomerReq.  # noqa: E501
        :type: str
        """

        self._sort = sort

    @property
    def name(self):
        """Gets the name of this ListCustomerReq.  # noqa: E501

         用户昵称搜索  # noqa: E501

        :return: The name of this ListCustomerReq.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCustomerReq.

         用户昵称搜索  # noqa: E501

        :param name: The name of this ListCustomerReq.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_deleted_at(self):
        """Gets the is_deleted_at of this ListCustomerReq.  # noqa: E501

         用户状态 , \"true\":已注销, \"false\":正常  # noqa: E501

        :return: The is_deleted_at of this ListCustomerReq.  # noqa: E501
        :rtype: str
        """
        return self._is_deleted_at

    @is_deleted_at.setter
    def is_deleted_at(self, is_deleted_at):
        """Sets the is_deleted_at of this ListCustomerReq.

         用户状态 , \"true\":已注销, \"false\":正常  # noqa: E501

        :param is_deleted_at: The is_deleted_at of this ListCustomerReq.  # noqa: E501
        :type: str
        """

        self._is_deleted_at = is_deleted_at

    @property
    def created_at_start(self):
        """Gets the created_at_start of this ListCustomerReq.  # noqa: E501

         创建时间起始时间  # noqa: E501

        :return: The created_at_start of this ListCustomerReq.  # noqa: E501
        :rtype: str
        """
        return self._created_at_start

    @created_at_start.setter
    def created_at_start(self, created_at_start):
        """Sets the created_at_start of this ListCustomerReq.

         创建时间起始时间  # noqa: E501

        :param created_at_start: The created_at_start of this ListCustomerReq.  # noqa: E501
        :type: str
        """

        self._created_at_start = created_at_start

    @property
    def created_at_end(self):
        """Gets the created_at_end of this ListCustomerReq.  # noqa: E501

         创建时间结束时间  # noqa: E501

        :return: The created_at_end of this ListCustomerReq.  # noqa: E501
        :rtype: str
        """
        return self._created_at_end

    @created_at_end.setter
    def created_at_end(self, created_at_end):
        """Sets the created_at_end of this ListCustomerReq.

         创建时间结束时间  # noqa: E501

        :param created_at_end: The created_at_end of this ListCustomerReq.  # noqa: E501
        :type: str
        """

        self._created_at_end = created_at_end

    @property
    def last_at_start(self):
        """Gets the last_at_start of this ListCustomerReq.  # noqa: E501

         最后购买时间起始时间  # noqa: E501

        :return: The last_at_start of this ListCustomerReq.  # noqa: E501
        :rtype: str
        """
        return self._last_at_start

    @last_at_start.setter
    def last_at_start(self, last_at_start):
        """Sets the last_at_start of this ListCustomerReq.

         最后购买时间起始时间  # noqa: E501

        :param last_at_start: The last_at_start of this ListCustomerReq.  # noqa: E501
        :type: str
        """

        self._last_at_start = last_at_start

    @property
    def last_at_end(self):
        """Gets the last_at_end of this ListCustomerReq.  # noqa: E501

         最后购买时间结束时间  # noqa: E501

        :return: The last_at_end of this ListCustomerReq.  # noqa: E501
        :rtype: str
        """
        return self._last_at_end

    @last_at_end.setter
    def last_at_end(self, last_at_end):
        """Sets the last_at_end of this ListCustomerReq.

         最后购买时间结束时间  # noqa: E501

        :param last_at_end: The last_at_end of this ListCustomerReq.  # noqa: E501
        :type: str
        """

        self._last_at_end = last_at_end

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
        if issubclass(ListCustomerReq, dict):
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
        if not isinstance(other, ListCustomerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other