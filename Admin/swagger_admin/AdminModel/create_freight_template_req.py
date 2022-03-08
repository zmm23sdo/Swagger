# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreateFreightTemplateReq(object):
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
        'unit': 'str',
        'start_price': 'str',
        'start_quantity': 'str',
        'add_price': 'str',
        'add_quantity': 'str',
        'region_ids': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'unit': 'unit',
        'start_price': 'start_price',
        'start_quantity': 'start_quantity',
        'add_price': 'add_price',
        'add_quantity': 'add_quantity',
        'region_ids': 'region_ids'
    }

    def __init__(self, name=None, unit=None, start_price=None, start_quantity=None, add_price=None, add_quantity=None, region_ids=None):  # noqa: E501
        """CreateFreightTemplateReq - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._unit = None
        self._start_price = None
        self._start_quantity = None
        self._add_price = None
        self._add_quantity = None
        self._region_ids = None
        self.discriminator = None
        self.name = name
        self.unit = unit
        self.start_price = start_price
        self.start_quantity = start_quantity
        self.add_price = add_price
        self.add_quantity = add_quantity
        self.region_ids = region_ids

    @property
    def name(self):
        """Gets the name of this CreateFreightTemplateReq.  # noqa: E501

         货运模板名称  # noqa: E501

        :return: The name of this CreateFreightTemplateReq.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateFreightTemplateReq.

         货运模板名称  # noqa: E501

        :param name: The name of this CreateFreightTemplateReq.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def unit(self):
        """Gets the unit of this CreateFreightTemplateReq.  # noqa: E501

         库存扣件方式 piece:件数 , weight:重量  # noqa: E501

        :return: The unit of this CreateFreightTemplateReq.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this CreateFreightTemplateReq.

         库存扣件方式 piece:件数 , weight:重量  # noqa: E501

        :param unit: The unit of this CreateFreightTemplateReq.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def start_price(self):
        """Gets the start_price of this CreateFreightTemplateReq.  # noqa: E501

         start_price 运费  # noqa: E501

        :return: The start_price of this CreateFreightTemplateReq.  # noqa: E501
        :rtype: str
        """
        return self._start_price

    @start_price.setter
    def start_price(self, start_price):
        """Sets the start_price of this CreateFreightTemplateReq.

         start_price 运费  # noqa: E501

        :param start_price: The start_price of this CreateFreightTemplateReq.  # noqa: E501
        :type: str
        """
        if start_price is None:
            raise ValueError("Invalid value for `start_price`, must not be `None`")  # noqa: E501

        self._start_price = start_price

    @property
    def start_quantity(self):
        """Gets the start_quantity of this CreateFreightTemplateReq.  # noqa: E501

         start_quantity 首件/首重  # noqa: E501

        :return: The start_quantity of this CreateFreightTemplateReq.  # noqa: E501
        :rtype: str
        """
        return self._start_quantity

    @start_quantity.setter
    def start_quantity(self, start_quantity):
        """Sets the start_quantity of this CreateFreightTemplateReq.

         start_quantity 首件/首重  # noqa: E501

        :param start_quantity: The start_quantity of this CreateFreightTemplateReq.  # noqa: E501
        :type: str
        """
        if start_quantity is None:
            raise ValueError("Invalid value for `start_quantity`, must not be `None`")  # noqa: E501

        self._start_quantity = start_quantity

    @property
    def add_price(self):
        """Gets the add_price of this CreateFreightTemplateReq.  # noqa: E501

         add_price 续费  # noqa: E501

        :return: The add_price of this CreateFreightTemplateReq.  # noqa: E501
        :rtype: str
        """
        return self._add_price

    @add_price.setter
    def add_price(self, add_price):
        """Sets the add_price of this CreateFreightTemplateReq.

         add_price 续费  # noqa: E501

        :param add_price: The add_price of this CreateFreightTemplateReq.  # noqa: E501
        :type: str
        """
        if add_price is None:
            raise ValueError("Invalid value for `add_price`, must not be `None`")  # noqa: E501

        self._add_price = add_price

    @property
    def add_quantity(self):
        """Gets the add_quantity of this CreateFreightTemplateReq.  # noqa: E501

         add_quantity 续件/续重  # noqa: E501

        :return: The add_quantity of this CreateFreightTemplateReq.  # noqa: E501
        :rtype: str
        """
        return self._add_quantity

    @add_quantity.setter
    def add_quantity(self, add_quantity):
        """Sets the add_quantity of this CreateFreightTemplateReq.

         add_quantity 续件/续重  # noqa: E501

        :param add_quantity: The add_quantity of this CreateFreightTemplateReq.  # noqa: E501
        :type: str
        """
        if add_quantity is None:
            raise ValueError("Invalid value for `add_quantity`, must not be `None`")  # noqa: E501

        self._add_quantity = add_quantity

    @property
    def region_ids(self):
        """Gets the region_ids of this CreateFreightTemplateReq.  # noqa: E501

         可配送区域 ids  # noqa: E501

        :return: The region_ids of this CreateFreightTemplateReq.  # noqa: E501
        :rtype: list[int]
        """
        return self._region_ids

    @region_ids.setter
    def region_ids(self, region_ids):
        """Sets the region_ids of this CreateFreightTemplateReq.

         可配送区域 ids  # noqa: E501

        :param region_ids: The region_ids of this CreateFreightTemplateReq.  # noqa: E501
        :type: list[int]
        """
        if region_ids is None:
            raise ValueError("Invalid value for `region_ids`, must not be `None`")  # noqa: E501

        self._region_ids = region_ids

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
        if issubclass(CreateFreightTemplateReq, dict):
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
        if not isinstance(other, CreateFreightTemplateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
