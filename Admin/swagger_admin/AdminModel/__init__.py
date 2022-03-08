# coding: utf-8

# flake8: noqa
"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_admin.AdminModel.all_permission_resp import AllPermissionResp
from swagger_admin.AdminModel.arrange_shipment_req import ArrangeShipmentReq
from swagger_admin.AdminModel.change_group_products_req import ChangeGroupProductsReq
from swagger_admin.AdminModel.change_order_total_req import ChangeOrderTotalReq
from swagger_admin.AdminModel.change_publish_status_products_req import ChangePublishStatusProductsReq
from swagger_admin.AdminModel.clear_system_permission_req import ClearSystemPermissionReq
from swagger_admin.AdminModel.create_freight_template_req import CreateFreightTemplateReq
from swagger_admin.AdminModel.create_group_req import CreateGroupReq
from swagger_admin.AdminModel.create_product_req import CreateProductReq
from swagger_admin.AdminModel.create_role_req import CreateRoleReq
from swagger_admin.AdminModel.create_user_req import CreateUserReq
from swagger_admin.AdminModel.customer import Customer
from swagger_admin.AdminModel.delete_customer_req import DeleteCustomerReq
from swagger_admin.AdminModel.delete_freight_template_req import DeleteFreightTemplateReq
from swagger_admin.AdminModel.delete_group_req import DeleteGroupReq
from swagger_admin.AdminModel.delete_products_req import DeleteProductsReq
from swagger_admin.AdminModel.delete_role_req import DeleteRoleReq
from swagger_admin.AdminModel.delete_user_req import DeleteUserReq
from swagger_admin.AdminModel.detail import Detail
from swagger_admin.AdminModel.edit_desc_customer_req import EditDescCustomerReq
from swagger_admin.AdminModel.empty import Empty
from swagger_admin.AdminModel.empty_customer import EmptyCustomer
from swagger_admin.AdminModel.empty_freight_template import EmptyFreightTemplate
from swagger_admin.AdminModel.empty_group import EmptyGroup
from swagger_admin.AdminModel.empty_order import EmptyOrder
from swagger_admin.AdminModel.empty_product import EmptyProduct
from swagger_admin.AdminModel.empty_role import EmptyRole
from swagger_admin.AdminModel.empty_system_permission import EmptySystemPermission
from swagger_admin.AdminModel.exist_role_by_name_req import ExistRoleByNameReq
from swagger_admin.AdminModel.export_order_req import ExportOrderReq
from swagger_admin.AdminModel.freight_region import FreightRegion
from swagger_admin.AdminModel.freight_template import FreightTemplate
from swagger_admin.AdminModel.get_all_permission_req import GetAllPermissionReq
from swagger_admin.AdminModel.get_customer_req import GetCustomerReq
from swagger_admin.AdminModel.get_order_req import GetOrderReq
from swagger_admin.AdminModel.get_product_req import GetProductReq
from swagger_admin.AdminModel.get_role_req import GetRoleReq
from swagger_admin.AdminModel.get_user_req import GetUserReq
from swagger_admin.AdminModel.group import Group
from swagger_admin.AdminModel.init_system_permission_req import InitSystemPermissionReq
from swagger_admin.AdminModel.list_customer_req import ListCustomerReq
from swagger_admin.AdminModel.list_customer_resp import ListCustomerResp
from swagger_admin.AdminModel.list_freight_region_req import ListFreightRegionReq
from swagger_admin.AdminModel.list_freight_region_resp import ListFreightRegionResp
from swagger_admin.AdminModel.list_freight_template_req import ListFreightTemplateReq
from swagger_admin.AdminModel.list_freight_template_resp import ListFreightTemplateResp
from swagger_admin.AdminModel.list_group_req import ListGroupReq
from swagger_admin.AdminModel.list_group_resp import ListGroupResp
from swagger_admin.AdminModel.list_order_req import ListOrderReq
from swagger_admin.AdminModel.list_order_resp import ListOrderResp
from swagger_admin.AdminModel.list_product_child import ListProductChild
from swagger_admin.AdminModel.list_product_info import ListProductInfo
from swagger_admin.AdminModel.list_products_req import ListProductsReq
from swagger_admin.AdminModel.list_products_resp import ListProductsResp
from swagger_admin.AdminModel.list_role_req import ListRoleReq
from swagger_admin.AdminModel.list_role_resp import ListRoleResp
from swagger_admin.AdminModel.list_users_req import ListUsersReq
from swagger_admin.AdminModel.list_users_resp import ListUsersResp
from swagger_admin.AdminModel.order import Order
from swagger_admin.AdminModel.order_history import OrderHistory
from swagger_admin.AdminModel.order_product import OrderProduct
from swagger_admin.AdminModel.permission_by_uuid_req import PermissionByUuidReq
from swagger_admin.AdminModel.permission_by_uuid_resp import PermissionByUuidResp
from swagger_admin.AdminModel.product import Product
from swagger_admin.AdminModel.product_info import ProductInfo
from swagger_admin.AdminModel.reset_password_user_req import ResetPasswordUserReq
from swagger_admin.AdminModel.role import Role
from swagger_admin.AdminModel.role_detail import RoleDetail
from swagger_admin.AdminModel.sku_item import SkuItem
from swagger_admin.AdminModel.update_freight_template_req import UpdateFreightTemplateReq
from swagger_admin.AdminModel.update_group_req import UpdateGroupReq
from swagger_admin.AdminModel.update_order_note_req import UpdateOrderNoteReq
from swagger_admin.AdminModel.update_price_product_req import UpdatePriceProductReq
from swagger_admin.AdminModel.update_product_req import UpdateProductReq
from swagger_admin.AdminModel.update_role_req import UpdateRoleReq
from swagger_admin.AdminModel.update_stock_product_req import UpdateStockProductReq
from swagger_admin.AdminModel.update_user_req import UpdateUserReq
from swagger_admin.AdminModel.user import User
from swagger_admin.AdminModel.user_role import UserRole
from swagger_admin.AdminModel.variation import Variation
