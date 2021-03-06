# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Order(object):
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
        'order_total': 'str',
        'status': 'str',
        'merchandise_subtotal': 'str',
        'shipping_fee': 'str',
        'order_discount': 'str',
        'message': 'str',
        'create_time': 'str',
        'payment_time': 'str',
        'delivery_time': 'str',
        'completed_time': 'str',
        'cancelled_time': 'str',
        'products': 'list[OrderProduct]',
        'customer': 'Customer',
        'note': 'str',
        'order_histroy': 'list[OrderHistory]'
    }

    attribute_map = {
        'id': 'id',
        'order_total': 'order_total',
        'status': 'status',
        'merchandise_subtotal': 'merchandise_subtotal',
        'shipping_fee': 'shipping_fee',
        'order_discount': 'order_discount',
        'message': 'message',
        'create_time': 'create_time',
        'payment_time': 'payment_time',
        'delivery_time': 'delivery_time',
        'completed_time': 'completed_time',
        'cancelled_time': 'cancelled_time',
        'products': 'products',
        'customer': 'customer',
        'note': 'note',
        'order_histroy': 'order_histroy'
    }

    def __init__(self, id=None, order_total=None, status=None, merchandise_subtotal=None, shipping_fee=None, order_discount=None, message=None, create_time=None, payment_time=None, delivery_time=None, completed_time=None, cancelled_time=None, products=None, customer=None, note=None, order_histroy=None):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._order_total = None
        self._status = None
        self._merchandise_subtotal = None
        self._shipping_fee = None
        self._order_discount = None
        self._message = None
        self._create_time = None
        self._payment_time = None
        self._delivery_time = None
        self._completed_time = None
        self._cancelled_time = None
        self._products = None
        self._customer = None
        self._note = None
        self._order_histroy = None
        self.discriminator = None
        self.id = id
        self.order_total = order_total
        self.status = status
        self.merchandise_subtotal = merchandise_subtotal
        self.shipping_fee = shipping_fee
        self.order_discount = order_discount
        self.message = message
        self.create_time = create_time
        self.payment_time = payment_time
        self.delivery_time = delivery_time
        self.completed_time = completed_time
        self.cancelled_time = cancelled_time
        self.products = products
        self.customer = customer
        self.note = note
        self.order_histroy = order_histroy

    @property
    def id(self):
        """Gets the id of this Order.  # noqa: E501

         ??????ID  # noqa: E501

        :return: The id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.

         ??????ID  # noqa: E501

        :param id: The id of this Order.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def order_total(self):
        """Gets the order_total of this Order.  # noqa: E501

         ?????????????????? ??????????????? = Merchandise Subtotal + Shipping Fee + Order Discount + ????????????  # noqa: E501

        :return: The order_total of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_total

    @order_total.setter
    def order_total(self, order_total):
        """Sets the order_total of this Order.

         ?????????????????? ??????????????? = Merchandise Subtotal + Shipping Fee + Order Discount + ????????????  # noqa: E501

        :param order_total: The order_total of this Order.  # noqa: E501
        :type: str
        """
        if order_total is None:
            raise ValueError("Invalid value for `order_total`, must not be `None`")  # noqa: E501

        self._order_total = order_total

    @property
    def status(self):
        """Gets the status of this Order.  # noqa: E501

         ???????????? ?????????:Unpaid,?????????:To Ship,?????????:Shipped,?????????:Completed,?????????:Cancelled  # noqa: E501

        :return: The status of this Order.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.

         ???????????? ?????????:Unpaid,?????????:To Ship,?????????:Shipped,?????????:Completed,?????????:Cancelled  # noqa: E501

        :param status: The status of this Order.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def merchandise_subtotal(self):
        """Gets the merchandise_subtotal of this Order.  # noqa: E501

         ??????????????????  # noqa: E501

        :return: The merchandise_subtotal of this Order.  # noqa: E501
        :rtype: str
        """
        return self._merchandise_subtotal

    @merchandise_subtotal.setter
    def merchandise_subtotal(self, merchandise_subtotal):
        """Sets the merchandise_subtotal of this Order.

         ??????????????????  # noqa: E501

        :param merchandise_subtotal: The merchandise_subtotal of this Order.  # noqa: E501
        :type: str
        """
        if merchandise_subtotal is None:
            raise ValueError("Invalid value for `merchandise_subtotal`, must not be `None`")  # noqa: E501

        self._merchandise_subtotal = merchandise_subtotal

    @property
    def shipping_fee(self):
        """Gets the shipping_fee of this Order.  # noqa: E501

         ????????????  # noqa: E501

        :return: The shipping_fee of this Order.  # noqa: E501
        :rtype: str
        """
        return self._shipping_fee

    @shipping_fee.setter
    def shipping_fee(self, shipping_fee):
        """Sets the shipping_fee of this Order.

         ????????????  # noqa: E501

        :param shipping_fee: The shipping_fee of this Order.  # noqa: E501
        :type: str
        """
        if shipping_fee is None:
            raise ValueError("Invalid value for `shipping_fee`, must not be `None`")  # noqa: E501

        self._shipping_fee = shipping_fee

    @property
    def order_discount(self):
        """Gets the order_discount of this Order.  # noqa: E501

         ??????????????????  # noqa: E501

        :return: The order_discount of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_discount

    @order_discount.setter
    def order_discount(self, order_discount):
        """Sets the order_discount of this Order.

         ??????????????????  # noqa: E501

        :param order_discount: The order_discount of this Order.  # noqa: E501
        :type: str
        """
        if order_discount is None:
            raise ValueError("Invalid value for `order_discount`, must not be `None`")  # noqa: E501

        self._order_discount = order_discount

    @property
    def message(self):
        """Gets the message of this Order.  # noqa: E501

         ??????????????????  # noqa: E501

        :return: The message of this Order.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Order.

         ??????????????????  # noqa: E501

        :param message: The message of this Order.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def create_time(self):
        """Gets the create_time of this Order.  # noqa: E501

         ????????????  # noqa: E501

        :return: The create_time of this Order.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Order.

         ????????????  # noqa: E501

        :param create_time: The create_time of this Order.  # noqa: E501
        :type: str
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def payment_time(self):
        """Gets the payment_time of this Order.  # noqa: E501

         ????????????  # noqa: E501

        :return: The payment_time of this Order.  # noqa: E501
        :rtype: str
        """
        return self._payment_time

    @payment_time.setter
    def payment_time(self, payment_time):
        """Sets the payment_time of this Order.

         ????????????  # noqa: E501

        :param payment_time: The payment_time of this Order.  # noqa: E501
        :type: str
        """
        if payment_time is None:
            raise ValueError("Invalid value for `payment_time`, must not be `None`")  # noqa: E501

        self._payment_time = payment_time

    @property
    def delivery_time(self):
        """Gets the delivery_time of this Order.  # noqa: E501

         ????????????  # noqa: E501

        :return: The delivery_time of this Order.  # noqa: E501
        :rtype: str
        """
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, delivery_time):
        """Sets the delivery_time of this Order.

         ????????????  # noqa: E501

        :param delivery_time: The delivery_time of this Order.  # noqa: E501
        :type: str
        """
        if delivery_time is None:
            raise ValueError("Invalid value for `delivery_time`, must not be `None`")  # noqa: E501

        self._delivery_time = delivery_time

    @property
    def completed_time(self):
        """Gets the completed_time of this Order.  # noqa: E501

         ????????????  # noqa: E501

        :return: The completed_time of this Order.  # noqa: E501
        :rtype: str
        """
        return self._completed_time

    @completed_time.setter
    def completed_time(self, completed_time):
        """Sets the completed_time of this Order.

         ????????????  # noqa: E501

        :param completed_time: The completed_time of this Order.  # noqa: E501
        :type: str
        """
        if completed_time is None:
            raise ValueError("Invalid value for `completed_time`, must not be `None`")  # noqa: E501

        self._completed_time = completed_time

    @property
    def cancelled_time(self):
        """Gets the cancelled_time of this Order.  # noqa: E501

         ????????????, ???????????????????????????????????????, ??????????????????  # noqa: E501

        :return: The cancelled_time of this Order.  # noqa: E501
        :rtype: str
        """
        return self._cancelled_time

    @cancelled_time.setter
    def cancelled_time(self, cancelled_time):
        """Sets the cancelled_time of this Order.

         ????????????, ???????????????????????????????????????, ??????????????????  # noqa: E501

        :param cancelled_time: The cancelled_time of this Order.  # noqa: E501
        :type: str
        """
        if cancelled_time is None:
            raise ValueError("Invalid value for `cancelled_time`, must not be `None`")  # noqa: E501

        self._cancelled_time = cancelled_time

    @property
    def products(self):
        """Gets the products of this Order.  # noqa: E501

         ????????????????????????  # noqa: E501

        :return: The products of this Order.  # noqa: E501
        :rtype: list[OrderProduct]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this Order.

         ????????????????????????  # noqa: E501

        :param products: The products of this Order.  # noqa: E501
        :type: list[OrderProduct]
        """
        if products is None:
            raise ValueError("Invalid value for `products`, must not be `None`")  # noqa: E501

        self._products = products

    @property
    def customer(self):
        """Gets the customer of this Order.  # noqa: E501


        :return: The customer of this Order.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Order.


        :param customer: The customer of this Order.  # noqa: E501
        :type: Customer
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def note(self):
        """Gets the note of this Order.  # noqa: E501

         ?????????????????????????????????????????????????????????  # noqa: E501

        :return: The note of this Order.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Order.

         ?????????????????????????????????????????????????????????  # noqa: E501

        :param note: The note of this Order.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def order_histroy(self):
        """Gets the order_histroy of this Order.  # noqa: E501

         ?????????????????????????????????????????????????????????????????????  # noqa: E501

        :return: The order_histroy of this Order.  # noqa: E501
        :rtype: list[OrderHistory]
        """
        return self._order_histroy

    @order_histroy.setter
    def order_histroy(self, order_histroy):
        """Sets the order_histroy of this Order.

         ?????????????????????????????????????????????????????????????????????  # noqa: E501

        :param order_histroy: The order_histroy of this Order.  # noqa: E501
        :type: list[OrderHistory]
        """
        if order_histroy is None:
            raise ValueError("Invalid value for `order_histroy`, must not be `None`")  # noqa: E501

        self._order_histroy = order_histroy

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
