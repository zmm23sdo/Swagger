# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FreightTemplate(object):
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
        'id': 'int',
        'unit': 'str',
        'start_price': 'str',
        'start_quantity': 'str',
        'add_price': 'str',
        'add_quantity': 'str',
        'name': 'str',
        'version': 'str',
        'regions': 'str',
        'item_count': 'str',
        'update_time': 'str',
        'created_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'unit': 'unit',
        'start_price': 'start_price',
        'start_quantity': 'start_quantity',
        'add_price': 'add_price',
        'add_quantity': 'add_quantity',
        'name': 'name',
        'version': 'version',
        'regions': 'regions',
        'item_count': 'item_count',
        'update_time': 'update_time',
        'created_time': 'created_time'
    }

    def __init__(self, id=None, unit=None, start_price=None, start_quantity=None, add_price=None, add_quantity=None, name=None, version=None, regions=None, item_count=None, update_time=None, created_time=None):  # noqa: E501
        """FreightTemplate - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._unit = None
        self._start_price = None
        self._start_quantity = None
        self._add_price = None
        self._add_quantity = None
        self._name = None
        self._version = None
        self._regions = None
        self._item_count = None
        self._update_time = None
        self._created_time = None
        self.discriminator = None
        self.id = id
        self.unit = unit
        self.start_price = start_price
        self.start_quantity = start_quantity
        self.add_price = add_price
        self.add_quantity = add_quantity
        self.name = name
        self.version = version
        self.regions = regions
        self.item_count = item_count
        self.update_time = update_time
        self.created_time = created_time

    @property
    def id(self):
        """Gets the id of this FreightTemplate.  # noqa: E501

         货运模板ID  # noqa: E501

        :return: The id of this FreightTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FreightTemplate.

         货运模板ID  # noqa: E501

        :param id: The id of this FreightTemplate.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def unit(self):
        """Gets the unit of this FreightTemplate.  # noqa: E501

         单位 库存扣件方式 piece:件数 , weight:重量  # noqa: E501

        :return: The unit of this FreightTemplate.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this FreightTemplate.

         单位 库存扣件方式 piece:件数 , weight:重量  # noqa: E501

        :param unit: The unit of this FreightTemplate.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def start_price(self):
        """Gets the start_price of this FreightTemplate.  # noqa: E501

         start_price  # noqa: E501

        :return: The start_price of this FreightTemplate.  # noqa: E501
        :rtype: str
        """
        return self._start_price

    @start_price.setter
    def start_price(self, start_price):
        """Sets the start_price of this FreightTemplate.

         start_price  # noqa: E501

        :param start_price: The start_price of this FreightTemplate.  # noqa: E501
        :type: str
        """
        if start_price is None:
            raise ValueError("Invalid value for `start_price`, must not be `None`")  # noqa: E501

        self._start_price = start_price

    @property
    def start_quantity(self):
        """Gets the start_quantity of this FreightTemplate.  # noqa: E501

         start_quantity  # noqa: E501

        :return: The start_quantity of this FreightTemplate.  # noqa: E501
        :rtype: str
        """
        return self._start_quantity

    @start_quantity.setter
    def start_quantity(self, start_quantity):
        """Sets the start_quantity of this FreightTemplate.

         start_quantity  # noqa: E501

        :param start_quantity: The start_quantity of this FreightTemplate.  # noqa: E501
        :type: str
        """
        if start_quantity is None:
            raise ValueError("Invalid value for `start_quantity`, must not be `None`")  # noqa: E501

        self._start_quantity = start_quantity

    @property
    def add_price(self):
        """Gets the add_price of this FreightTemplate.  # noqa: E501

         add_price  # noqa: E501

        :return: The add_price of this FreightTemplate.  # noqa: E501
        :rtype: str
        """
        return self._add_price

    @add_price.setter
    def add_price(self, add_price):
        """Sets the add_price of this FreightTemplate.

         add_price  # noqa: E501

        :param add_price: The add_price of this FreightTemplate.  # noqa: E501
        :type: str
        """
        if add_price is None:
            raise ValueError("Invalid value for `add_price`, must not be `None`")  # noqa: E501

        self._add_price = add_price

    @property
    def add_quantity(self):
        """Gets the add_quantity of this FreightTemplate.  # noqa: E501

         add_quantity  # noqa: E501

        :return: The add_quantity of this FreightTemplate.  # noqa: E501
        :rtype: str
        """
        return self._add_quantity

    @add_quantity.setter
    def add_quantity(self, add_quantity):
        """Sets the add_quantity of this FreightTemplate.

         add_quantity  # noqa: E501

        :param add_quantity: The add_quantity of this FreightTemplate.  # noqa: E501
        :type: str
        """
        if add_quantity is None:
            raise ValueError("Invalid value for `add_quantity`, must not be `None`")  # noqa: E501

        self._add_quantity = add_quantity

    @property
    def name(self):
        """Gets the name of this FreightTemplate.  # noqa: E501

         货运模板名称  # noqa: E501

        :return: The name of this FreightTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FreightTemplate.

         货运模板名称  # noqa: E501

        :param name: The name of this FreightTemplate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this FreightTemplate.  # noqa: E501

         version  # noqa: E501

        :return: The version of this FreightTemplate.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FreightTemplate.

         version  # noqa: E501

        :param version: The version of this FreightTemplate.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def regions(self):
        """Gets the regions of this FreightTemplate.  # noqa: E501

         可配送区域  # noqa: E501

        :return: The regions of this FreightTemplate.  # noqa: E501
        :rtype: str
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this FreightTemplate.

         可配送区域  # noqa: E501

        :param regions: The regions of this FreightTemplate.  # noqa: E501
        :type: str
        """
        if regions is None:
            raise ValueError("Invalid value for `regions`, must not be `None`")  # noqa: E501

        self._regions = regions

    @property
    def item_count(self):
        """Gets the item_count of this FreightTemplate.  # noqa: E501

         关联商品数量  # noqa: E501

        :return: The item_count of this FreightTemplate.  # noqa: E501
        :rtype: str
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """Sets the item_count of this FreightTemplate.

         关联商品数量  # noqa: E501

        :param item_count: The item_count of this FreightTemplate.  # noqa: E501
        :type: str
        """
        if item_count is None:
            raise ValueError("Invalid value for `item_count`, must not be `None`")  # noqa: E501

        self._item_count = item_count

    @property
    def update_time(self):
        """Gets the update_time of this FreightTemplate.  # noqa: E501

         更新时间  # noqa: E501

        :return: The update_time of this FreightTemplate.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this FreightTemplate.

         更新时间  # noqa: E501

        :param update_time: The update_time of this FreightTemplate.  # noqa: E501
        :type: str
        """
        if update_time is None:
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def created_time(self):
        """Gets the created_time of this FreightTemplate.  # noqa: E501

         创建时间  # noqa: E501

        :return: The created_time of this FreightTemplate.  # noqa: E501
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this FreightTemplate.

         创建时间  # noqa: E501

        :param created_time: The created_time of this FreightTemplate.  # noqa: E501
        :type: str
        """
        if created_time is None:
            raise ValueError("Invalid value for `created_time`, must not be `None`")  # noqa: E501

        self._created_time = created_time

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
        if issubclass(FreightTemplate, dict):
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
        if not isinstance(other, FreightTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other