# swagger_admin.OrderApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**arrange_shipment**](OrderApi.md#arrange_shipment) | **PUT** /orders/arrangeShipment | 待发货订单,安排发货完善物流信息
[**change_order_total**](OrderApi.md#change_order_total) | **PUT** /orders/total | 未支付订单,修改一口价/邮费
[**export_order**](OrderApi.md#export_order) | **GET** /orders/export | 订单导出
[**get_order**](OrderApi.md#get_order) | **GET** /orders/{id} | 订单详情
[**list_order**](OrderApi.md#list_order) | **GET** /orders | 订单列表
[**update_order_note**](OrderApi.md#update_order_note) | **PUT** /orders/note | 修改订单note

# **arrange_shipment**
> EmptyOrder arrange_shipment(body)

待发货订单,安排发货完善物流信息

### Example
```python
from __future__ import print_function
import time
import swagger_admin
from swagger_admin.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_admin.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_admin.OrderApi(swagger_admin.ApiClient(configuration))
body = swagger_admin.ArrangeShipmentReq() # ArrangeShipmentReq | 

try:
    # 待发货订单,安排发货完善物流信息
    api_response = api_instance.arrange_shipment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->arrange_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArrangeShipmentReq**](ArrangeShipmentReq.md)|  | 

### Return type

[**EmptyOrder**](EmptyOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_order_total**
> EmptyOrder change_order_total(body)

未支付订单,修改一口价/邮费

### Example
```python
from __future__ import print_function
import time
import swagger_admin
from swagger_admin.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_admin.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_admin.OrderApi(swagger_admin.ApiClient(configuration))
body = swagger_admin.ChangeOrderTotalReq() # ChangeOrderTotalReq | 

try:
    # 未支付订单,修改一口价/邮费
    api_response = api_instance.change_order_total(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->change_order_total: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeOrderTotalReq**](ChangeOrderTotalReq.md)|  | 

### Return type

[**EmptyOrder**](EmptyOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_order**
> EmptyOrder export_order(search=search, type=type)

订单导出

### Example
```python
from __future__ import print_function
import time
import swagger_admin
from swagger_admin.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_admin.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_admin.OrderApi(swagger_admin.ApiClient(configuration))
search = 'search_example' # str |  (optional)
type = 'all' # str |  列表数据类型支持: all|unpaid|to_ship|shipped|completed|cancelled 默认 all (optional) (default to all)

try:
    # 订单导出
    api_response = api_instance.export_order(search=search, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->export_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 
 **type** | **str**|  列表数据类型支持: all|unpaid|to_ship|shipped|completed|cancelled 默认 all | [optional] [default to all]

### Return type

[**EmptyOrder**](EmptyOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> Order get_order(id)

订单详情

### Example
```python
from __future__ import print_function
import time
import swagger_admin
from swagger_admin.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_admin.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_admin.OrderApi(swagger_admin.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # 订单详情
    api_response = api_instance.get_order(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_order**
> ListOrderResp list_order(page, page_size=page_size, type=type, search=search)

订单列表

### Example
```python
from __future__ import print_function
import time
import swagger_admin
from swagger_admin.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_admin.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_admin.OrderApi(swagger_admin.ApiClient(configuration))
page = 789 # int |  当前页码
page_size = 15 # int |  展示数量 默认15 (optional) (default to 15)
type = 'all' # str |  列表数据类型支持: all|unpaid|to_ship|shipped|completed|cancelled 默认 all (optional) (default to all)
search = 'search_example' # str |  模糊搜索 (商品名称、Variation、SKU、会员昵称、会员ID、订单ID、物流公司、物流单号) (optional)

try:
    # 订单列表
    api_response = api_instance.list_order(page, page_size=page_size, type=type, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->list_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  当前页码 | 
 **page_size** | **int**|  展示数量 默认15 | [optional] [default to 15]
 **type** | **str**|  列表数据类型支持: all|unpaid|to_ship|shipped|completed|cancelled 默认 all | [optional] [default to all]
 **search** | **str**|  模糊搜索 (商品名称、Variation、SKU、会员昵称、会员ID、订单ID、物流公司、物流单号) | [optional] 

### Return type

[**ListOrderResp**](ListOrderResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_note**
> EmptyOrder update_order_note(body)

修改订单note

### Example
```python
from __future__ import print_function
import time
import swagger_admin
from swagger_admin.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_admin.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_admin.OrderApi(swagger_admin.ApiClient(configuration))
body = swagger_admin.UpdateOrderNoteReq() # UpdateOrderNoteReq | 

try:
    # 修改订单note
    api_response = api_instance.update_order_note(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->update_order_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOrderNoteReq**](UpdateOrderNoteReq.md)|  | 

### Return type

[**EmptyOrder**](EmptyOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

