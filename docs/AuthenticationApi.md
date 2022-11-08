# swagger_client.AuthenticationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_controller_login**](AuthenticationApi.md#auth_controller_login) | **POST** /auth/login | 
[**auth_controller_register**](AuthenticationApi.md#auth_controller_register) | **POST** /auth/register | 

# **auth_controller_login**
> LoginAckDto auth_controller_login(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.LoginDto() # LoginDto | 

try:
    api_response = api_instance.auth_controller_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_controller_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginDto**](LoginDto.md)|  | 

### Return type

[**LoginAckDto**](LoginAckDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_register**
> LoginAckDto auth_controller_register(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.AuthDto() # AuthDto | 

try:
    api_response = api_instance.auth_controller_register(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_controller_register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthDto**](AuthDto.md)|  | 

### Return type

[**LoginAckDto**](LoginAckDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

