# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_admin
from swagger_admin.AdminApi.product_api import ProductApi  # noqa: E501
from swagger_admin.rest import ApiException


class TestProductApi(unittest.TestCase):
    """ProductApi unit test stubs"""

    def setUp(self):
        self.api = ProductApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_group_products(self):
        """Test case for change_group_products

        批量设置商品分组  # noqa: E501
        """
        pass

    def test_change_publish_status_products(self):
        """Test case for change_publish_status_products

        批量上架/下架商品  # noqa: E501
        """
        pass

    def test_create_product(self):
        """Test case for create_product

        发布商品  # noqa: E501
        """
        pass

    def test_delete_products(self):
        """Test case for delete_products

        批量删除商品  # noqa: E501
        """
        pass

    def test_get_product(self):
        """Test case for get_product

        商品详情  # noqa: E501
        """
        pass

    def test_list_products(self):
        """Test case for list_products

        商品列表  # noqa: E501
        """
        pass

    def test_update_price_product(self):
        """Test case for update_price_product

        编辑价格  # noqa: E501
        """
        pass

    def test_update_product(self):
        """Test case for update_product

        修改商品  # noqa: E501
        """
        pass

    def test_update_stock_product(self):
        """Test case for update_stock_product

        编辑库存  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()