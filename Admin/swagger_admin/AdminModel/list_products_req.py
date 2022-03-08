# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ListProductsReq(object):
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
        'state': 'str',
        'search': 'str',
        'group_id': 'list[str]',
        'category_id': 'list[str]',
        'sold_out': 'str',
        'price': 'str',
        'created_at_start': 'str',
        'created_at_end': 'str'
    }

    attribute_map = {
        'page': 'page',
        'page_size': 'page_size',
        'orderby': 'orderby',
        'sort': 'sort',
        'state': 'state',
        'search': 'search',
        'group_id': 'group_id',
        'category_id': 'category_id',
        'sold_out': 'sold_out',
        'price': 'price',
        'created_at_start': 'created_at_start',
        'created_at_end': 'created_at_end'
    }

    def __init__(self, page=None, page_size=15, orderby='created_at', sort='desc', state='all', search=None, group_id=None, category_id=None, sold_out=None, price=None, created_at_start=None, created_at_end=None):  # noqa: E501
        """ListProductsReq - a model defined in Swagger"""  # noqa: E501
        self._page = None
        self._page_size = None
        self._orderby = None
        self._sort = None
        self._state = None
        self._search = None
        self._group_id = None
        self._category_id = None
        self._sold_out = None
        self._price = None
        self._created_at_start = None
        self._created_at_end = None
        self.discriminator = None
        self.page = page
        if page_size is not None:
            self.page_size = page_size
        if orderby is not None:
            self.orderby = orderby
        if sort is not None:
            self.sort = sort
        if state is not None:
            self.state = state
        if search is not None:
            self.search = search
        if group_id is not None:
            self.group_id = group_id
        if category_id is not None:
            self.category_id = category_id
        if sold_out is not None:
            self.sold_out = sold_out
        if price is not None:
            self.price = price
        if created_at_start is not None:
            self.created_at_start = created_at_start
        if created_at_end is not None:
            self.created_at_end = created_at_end

    @property
    def page(self):
        """Gets the page of this ListProductsReq.  # noqa: E501

         当前页码  # noqa: E501

        :return: The page of this ListProductsReq.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListProductsReq.

         当前页码  # noqa: E501

        :param page: The page of this ListProductsReq.  # noqa: E501
        :type: int
        """
        if page is None:
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ListProductsReq.  # noqa: E501

         展示数量 默认15  # noqa: E501

        :return: The page_size of this ListProductsReq.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListProductsReq.

         展示数量 默认15  # noqa: E501

        :param page_size: The page_size of this ListProductsReq.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def orderby(self):
        """Gets the orderby of this ListProductsReq.  # noqa: E501

         排序字段(支持:created_at|price|stock|sold_out),默认 created_at  # noqa: E501

        :return: The orderby of this ListProductsReq.  # noqa: E501
        :rtype: str
        """
        return self._orderby

    @orderby.setter
    def orderby(self, orderby):
        """Sets the orderby of this ListProductsReq.

         排序字段(支持:created_at|price|stock|sold_out),默认 created_at  # noqa: E501

        :param orderby: The orderby of this ListProductsReq.  # noqa: E501
        :type: str
        """

        self._orderby = orderby

    @property
    def sort(self):
        """Gets the sort of this ListProductsReq.  # noqa: E501

         排序方式(asc,desc), 默认 desc  # noqa: E501

        :return: The sort of this ListProductsReq.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListProductsReq.

         排序方式(asc,desc), 默认 desc  # noqa: E501

        :param sort: The sort of this ListProductsReq.  # noqa: E501
        :type: str
        """

        self._sort = sort

    @property
    def state(self):
        """Gets the state of this ListProductsReq.  # noqa: E501

         状态  all:全部, on:上架 , active:下架 , out:售罄 ,  inactive: 删除默认 all  # noqa: E501

        :return: The state of this ListProductsReq.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListProductsReq.

         状态  all:全部, on:上架 , active:下架 , out:售罄 ,  inactive: 删除默认 all  # noqa: E501

        :param state: The state of this ListProductsReq.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def search(self):
        """Gets the search of this ListProductsReq.  # noqa: E501

         用户名模糊搜索  # noqa: E501

        :return: The search of this ListProductsReq.  # noqa: E501
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this ListProductsReq.

         用户名模糊搜索  # noqa: E501

        :param search: The search of this ListProductsReq.  # noqa: E501
        :type: str
        """

        self._search = search

    @property
    def group_id(self):
        """Gets the group_id of this ListProductsReq.  # noqa: E501

         商品分组ID搜索  # noqa: E501

        :return: The group_id of this ListProductsReq.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListProductsReq.

         商品分组ID搜索  # noqa: E501

        :param group_id: The group_id of this ListProductsReq.  # noqa: E501
        :type: list[str]
        """

        self._group_id = group_id

    @property
    def category_id(self):
        """Gets the category_id of this ListProductsReq.  # noqa: E501

         商品分类ID搜索  # noqa: E501

        :return: The category_id of this ListProductsReq.  # noqa: E501
        :rtype: list[str]
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ListProductsReq.

         商品分类ID搜索  # noqa: E501

        :param category_id: The category_id of this ListProductsReq.  # noqa: E501
        :type: list[str]
        """

        self._category_id = category_id

    @property
    def sold_out(self):
        """Gets the sold_out of this ListProductsReq.  # noqa: E501

         商品起始销量搜索  # noqa: E501

        :return: The sold_out of this ListProductsReq.  # noqa: E501
        :rtype: str
        """
        return self._sold_out

    @sold_out.setter
    def sold_out(self, sold_out):
        """Sets the sold_out of this ListProductsReq.

         商品起始销量搜索  # noqa: E501

        :param sold_out: The sold_out of this ListProductsReq.  # noqa: E501
        :type: str
        """

        self._sold_out = sold_out

    @property
    def price(self):
        """Gets the price of this ListProductsReq.  # noqa: E501

         商品起始价格搜索  # noqa: E501

        :return: The price of this ListProductsReq.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ListProductsReq.

         商品起始价格搜索  # noqa: E501

        :param price: The price of this ListProductsReq.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def created_at_start(self):
        """Gets the created_at_start of this ListProductsReq.  # noqa: E501

         商品创建时间起始时间  # noqa: E501

        :return: The created_at_start of this ListProductsReq.  # noqa: E501
        :rtype: str
        """
        return self._created_at_start

    @created_at_start.setter
    def created_at_start(self, created_at_start):
        """Sets the created_at_start of this ListProductsReq.

         商品创建时间起始时间  # noqa: E501

        :param created_at_start: The created_at_start of this ListProductsReq.  # noqa: E501
        :type: str
        """

        self._created_at_start = created_at_start

    @property
    def created_at_end(self):
        """Gets the created_at_end of this ListProductsReq.  # noqa: E501

         商品创建时间结束时间  # noqa: E501

        :return: The created_at_end of this ListProductsReq.  # noqa: E501
        :rtype: str
        """
        return self._created_at_end

    @created_at_end.setter
    def created_at_end(self, created_at_end):
        """Sets the created_at_end of this ListProductsReq.

         商品创建时间结束时间  # noqa: E501

        :param created_at_end: The created_at_end of this ListProductsReq.  # noqa: E501
        :type: str
        """

        self._created_at_end = created_at_end

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
        if issubclass(ListProductsReq, dict):
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
        if not isinstance(other, ListProductsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
