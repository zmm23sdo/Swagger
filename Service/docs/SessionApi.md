# swagger_service.SessionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_session_info**](SessionApi.md#get_session_info) | **GET** /d/session | 获取accesstoken用户信息
[**login_sms**](SessionApi.md#login_sms) | **POST** /d/sms/login | 手机号登录step1-发送短信
[**logout**](SessionApi.md#logout) | **DELETE** /d/session | 登出
[**password_login**](SessionApi.md#password_login) | **POST** /d/session/password | 手机号密码登录
[**phone_login**](SessionApi.md#phone_login) | **POST** /d/session/phone_number | 手机号登录step2-登录
[**session_refresh**](SessionApi.md#session_refresh) | **POST** /d/session/refresh | 使用refresh获取新的token
[**user_login**](SessionApi.md#user_login) | **POST** /d/session/username | 用户名密码登录

# **get_session_info**
> SessionInfoResp get_session_info(authorization)

获取accesstoken用户信息

### Example
```python
from __future__ import print_function
import time
import swagger_service
from swagger_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_service.SessionApi(swagger_service.ApiClient(configuration))
authorization = 'authorization_example' # str | 

try:
    # 获取accesstoken用户信息
    api_response = api_instance.get_session_info(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_session_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 

### Return type

[**SessionInfoResp**](SessionInfoResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_sms**
> EmptyResp login_sms(body)

手机号登录step1-发送短信

### Example
```python
from __future__ import print_function
import time
import swagger_service
from swagger_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_service.SessionApi(swagger_service.ApiClient(configuration))
body = swagger_service.LoginSMSReq() # LoginSMSReq | 

try:
    # 手机号登录step1-发送短信
    api_response = api_instance.login_sms(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->login_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginSMSReq**](LoginSMSReq.md)|  | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> LoginResp logout(body, authorization)

登出

### Example
```python
from __future__ import print_function
import time
import swagger_service
from swagger_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_service.SessionApi(swagger_service.ApiClient(configuration))
body = swagger_service.SessionInfoReq() # SessionInfoReq | 
authorization = 'authorization_example' # str | 

try:
    # 登出
    api_response = api_instance.logout(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionInfoReq**](SessionInfoReq.md)|  | 
 **authorization** | **str**|  | 

### Return type

[**LoginResp**](LoginResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_login**
> LoginResp password_login(body)

手机号密码登录

### Example
```python
from __future__ import print_function
import time
import swagger_service
from swagger_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_service.SessionApi(swagger_service.ApiClient(configuration))
body = swagger_service.PasswordLoginReq() # PasswordLoginReq | 

try:
    # 手机号密码登录
    api_response = api_instance.password_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->password_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordLoginReq**](PasswordLoginReq.md)|  | 

### Return type

[**LoginResp**](LoginResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phone_login**
> LoginResp phone_login(body)

手机号登录step2-登录

### Example
```python
from __future__ import print_function
import time
import swagger_service
from swagger_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_service.SessionApi(swagger_service.ApiClient(configuration))
body = swagger_service.PhoneLoginReq() # PhoneLoginReq | 

try:
    # 手机号登录step2-登录
    api_response = api_instance.phone_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->phone_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneLoginReq**](PhoneLoginReq.md)|  | 

### Return type

[**LoginResp**](LoginResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_refresh**
> LoginResp session_refresh(body)

使用refresh获取新的token

### Example
```python
from __future__ import print_function
import time
import swagger_service
from swagger_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_service.SessionApi(swagger_service.ApiClient(configuration))
body = swagger_service.SessionRefreshReq() # SessionRefreshReq | 

try:
    # 使用refresh获取新的token
    api_response = api_instance.session_refresh(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->session_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionRefreshReq**](SessionRefreshReq.md)|  | 

### Return type

[**LoginResp**](LoginResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_login**
> LoginResp user_login(body)

用户名密码登录

### Example
```python
from __future__ import print_function
import time
import swagger_service
from swagger_service.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_service.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_service.SessionApi(swagger_service.ApiClient(configuration))
body = swagger_service.UserLoginReq() # UserLoginReq | 

try:
    # 用户名密码登录
    api_response = api_instance.user_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->user_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserLoginReq**](UserLoginReq.md)|  | 

### Return type

[**LoginResp**](LoginResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

