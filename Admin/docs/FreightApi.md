# swagger_admin.FreightApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_freight_template**](FreightApi.md#create_freight_template) | **POST** /freightTemplates | 创建运费策略
[**delete_freight_template**](FreightApi.md#delete_freight_template) | **DELETE** /freightTemplates/{id} | 删除运费策略
[**list_freight_region**](FreightApi.md#list_freight_region) | **GET** /freightRegions | 所有配送区域
[**list_freight_template**](FreightApi.md#list_freight_template) | **GET** /freightTemplates | 运费策略列表
[**update_freight_template**](FreightApi.md#update_freight_template) | **PUT** /freightTemplates/{id} | 更新运费策略

# **create_freight_template**
> EmptyFreightTemplate create_freight_template(body)

创建运费策略

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
api_instance = swagger_admin.FreightApi(swagger_admin.ApiClient(configuration))
body = swagger_admin.CreateFreightTemplateReq() # CreateFreightTemplateReq | 

try:
    # 创建运费策略
    api_response = api_instance.create_freight_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreightApi->create_freight_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFreightTemplateReq**](CreateFreightTemplateReq.md)|  | 

### Return type

[**EmptyFreightTemplate**](EmptyFreightTemplate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_freight_template**
> EmptyFreightTemplate delete_freight_template(body, id)

删除运费策略

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
api_instance = swagger_admin.FreightApi(swagger_admin.ApiClient(configuration))
body = swagger_admin.DeleteFreightTemplateReq() # DeleteFreightTemplateReq | 
id = 'id_example' # str | 

try:
    # 删除运费策略
    api_response = api_instance.delete_freight_template(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreightApi->delete_freight_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteFreightTemplateReq**](DeleteFreightTemplateReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**EmptyFreightTemplate**](EmptyFreightTemplate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_freight_region**
> ListFreightRegionResp list_freight_region()

所有配送区域

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
api_instance = swagger_admin.FreightApi(swagger_admin.ApiClient(configuration))

try:
    # 所有配送区域
    api_response = api_instance.list_freight_region()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreightApi->list_freight_region: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListFreightRegionResp**](ListFreightRegionResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_freight_template**
> ListFreightTemplateResp list_freight_template(page, page_size=page_size, name=name)

运费策略列表

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
api_instance = swagger_admin.FreightApi(swagger_admin.ApiClient(configuration))
page = 789 # int |  当前页码
page_size = 15 # int |  展示数量,默认 15 (optional) (default to 15)
name = 'name_example' # str |  货运模板名称 (optional)

try:
    # 运费策略列表
    api_response = api_instance.list_freight_template(page, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreightApi->list_freight_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  当前页码 | 
 **page_size** | **int**|  展示数量,默认 15 | [optional] [default to 15]
 **name** | **str**|  货运模板名称 | [optional] 

### Return type

[**ListFreightTemplateResp**](ListFreightTemplateResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_freight_template**
> EmptyFreightTemplate update_freight_template(body, id)

更新运费策略

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
api_instance = swagger_admin.FreightApi(swagger_admin.ApiClient(configuration))
body = swagger_admin.UpdateFreightTemplateReq() # UpdateFreightTemplateReq | 
id = 'id_example' # str | 

try:
    # 更新运费策略
    api_response = api_instance.update_freight_template(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreightApi->update_freight_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFreightTemplateReq**](UpdateFreightTemplateReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**EmptyFreightTemplate**](EmptyFreightTemplate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

