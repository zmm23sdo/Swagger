# swagger_service.PasswordApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_forget_pwd**](PasswordApi.md#email_forget_pwd) | **POST** /d/email/forget_pwd | 忘记密码step1-发送邮件
[**reset_password**](PasswordApi.md#reset_password) | **PUT** /d/password | 忘记密码step3-修改密码
[**sms_forget_pwd**](PasswordApi.md#sms_forget_pwd) | **POST** /d/sms/forget_pwd | 忘记密码step1-发送手机短信
[**update_password**](PasswordApi.md#update_password) | **PUT** /account/password | 个人中心修改密码
[**verify_email_code**](PasswordApi.md#verify_email_code) | **GET** /d/password/email | 忘记密码step2-验证邮件验证码
[**verify_phone_code**](PasswordApi.md#verify_phone_code) | **GET** /d/password/phone_code | 忘记密码step2-验证手机验证码

# **email_forget_pwd**
> EmptyResp email_forget_pwd(body)

忘记密码step1-发送邮件

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
api_instance = swagger_service.PasswordApi(swagger_service.ApiClient(configuration))
body = swagger_service.EmailForgetPwdReq() # EmailForgetPwdReq | 

try:
    # 忘记密码step1-发送邮件
    api_response = api_instance.email_forget_pwd(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordApi->email_forget_pwd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailForgetPwdReq**](EmailForgetPwdReq.md)|  | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> EmptyResp reset_password(body)

忘记密码step3-修改密码

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
api_instance = swagger_service.PasswordApi(swagger_service.ApiClient(configuration))
body = swagger_service.ResetPasswordReq() # ResetPasswordReq | 

try:
    # 忘记密码step3-修改密码
    api_response = api_instance.reset_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetPasswordReq**](ResetPasswordReq.md)|  | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_forget_pwd**
> EmptyResp sms_forget_pwd(body)

忘记密码step1-发送手机短信

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
api_instance = swagger_service.PasswordApi(swagger_service.ApiClient(configuration))
body = swagger_service.SmsForgetPwdReq() # SmsForgetPwdReq | 

try:
    # 忘记密码step1-发送手机短信
    api_response = api_instance.sms_forget_pwd(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordApi->sms_forget_pwd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmsForgetPwdReq**](SmsForgetPwdReq.md)|  | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> EmptyResp update_password(body)

个人中心修改密码

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
api_instance = swagger_service.PasswordApi(swagger_service.ApiClient(configuration))
body = swagger_service.UpdatePassword() # UpdatePassword | 

try:
    # 个人中心修改密码
    api_response = api_instance.update_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePassword**](UpdatePassword.md)|  | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email_code**
> VerifyPhoneCodeResp verify_email_code(email, code)

忘记密码step2-验证邮件验证码

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
api_instance = swagger_service.PasswordApi(swagger_service.ApiClient(configuration))
email = 'email_example' # str | 
code = 'code_example' # str |  邮件验证码

try:
    # 忘记密码step2-验证邮件验证码
    api_response = api_instance.verify_email_code(email, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordApi->verify_email_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **code** | **str**|  邮件验证码 | 

### Return type

[**VerifyPhoneCodeResp**](VerifyPhoneCodeResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_phone_code**
> VerifyPhoneCodeResp verify_phone_code(phone_number, code)

忘记密码step2-验证手机验证码

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
api_instance = swagger_service.PasswordApi(swagger_service.ApiClient(configuration))
phone_number = 'phone_number_example' # str | 
code = 'code_example' # str |  短信验证码

try:
    # 忘记密码step2-验证手机验证码
    api_response = api_instance.verify_phone_code(phone_number, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordApi->verify_phone_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 
 **code** | **str**|  短信验证码 | 

### Return type

[**VerifyPhoneCodeResp**](VerifyPhoneCodeResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

