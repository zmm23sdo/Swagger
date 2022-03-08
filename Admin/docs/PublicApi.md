# swagger_admin.PublicApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_system_permission**](PublicApi.md#clear_system_permission) | **POST** /d/clear/permissions | 清除系统所有权限
[**init_system_permission**](PublicApi.md#init_system_permission) | **POST** /d/init/permissions | 初始化系统所有权限

# **clear_system_permission**
> EmptySystemPermission clear_system_permission(body)

清除系统所有权限

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
api_instance = swagger_admin.PublicApi(swagger_admin.ApiClient(configuration))
body = swagger_admin.ClearSystemPermissionReq() # ClearSystemPermissionReq | 

try:
    # 清除系统所有权限
    api_response = api_instance.clear_system_permission(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->clear_system_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClearSystemPermissionReq**](ClearSystemPermissionReq.md)|  | 

### Return type

[**EmptySystemPermission**](EmptySystemPermission.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_system_permission**
> EmptySystemPermission init_system_permission(body)

初始化系统所有权限

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
api_instance = swagger_admin.PublicApi(swagger_admin.ApiClient(configuration))
body = swagger_admin.InitSystemPermissionReq() # InitSystemPermissionReq | 

try:
    # 初始化系统所有权限
    api_response = api_instance.init_system_permission(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->init_system_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InitSystemPermissionReq**](InitSystemPermissionReq.md)|  | 

### Return type

[**EmptySystemPermission**](EmptySystemPermission.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

