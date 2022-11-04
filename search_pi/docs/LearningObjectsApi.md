# swagger_client.LearningObjectsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lo_repository_controller_add_goal**](LearningObjectsApi.md#lo_repository_controller_add_goal) | **POST** /lo_repository/{repositoryId}/add_goal | 
[**lo_repository_controller_create_learning_object**](LearningObjectsApi.md#lo_repository_controller_create_learning_object) | **POST** /lo_repository/{repositoryId}/add_learning_object | 
[**lo_repository_controller_create_repository**](LearningObjectsApi.md#lo_repository_controller_create_repository) | **POST** /lo_repository/add | 
[**lo_repository_controller_list_repositories**](LearningObjectsApi.md#lo_repository_controller_list_repositories) | **GET** /lo_repository | 
[**lo_repository_controller_load_learning_object**](LearningObjectsApi.md#lo_repository_controller_load_learning_object) | **GET** /lo_repository/learning_objects/{learningObjectId} | 
[**lo_repository_controller_load_repository**](LearningObjectsApi.md#lo_repository_controller_load_repository) | **GET** /lo_repository/{repositoryId} | 
[**lo_repository_controller_modify_learning_object**](LearningObjectsApi.md#lo_repository_controller_modify_learning_object) | **PATCH** /lo_repository/{repositoryId}/{learningObjectId} | 
[**lo_repository_controller_modify_repository**](LearningObjectsApi.md#lo_repository_controller_modify_repository) | **PATCH** /lo_repository/{repositoryId} | 
[**lo_repository_controller_show_goal**](LearningObjectsApi.md#lo_repository_controller_show_goal) | **GET** /lo_repository/goals/{goalId} | 
[**lo_repository_controller_show_goals**](LearningObjectsApi.md#lo_repository_controller_show_goals) | **GET** /lo_repository/{repositoryId}/goals | 

# **lo_repository_controller_add_goal**
> LoGoalDto lo_repository_controller_add_goal(body, repository_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LearningObjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoGoalCreationDto() # LoGoalCreationDto | 
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.lo_repository_controller_add_goal(body, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningObjectsApi->lo_repository_controller_add_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoGoalCreationDto**](LoGoalCreationDto.md)|  | 
 **repository_id** | **str**|  | 

### Return type

[**LoGoalDto**](LoGoalDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lo_repository_controller_create_learning_object**
> LearningObjectDto lo_repository_controller_create_learning_object(body, repository_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LearningObjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LearningObjectCreationDto() # LearningObjectCreationDto | 
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.lo_repository_controller_create_learning_object(body, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningObjectsApi->lo_repository_controller_create_learning_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LearningObjectCreationDto**](LearningObjectCreationDto.md)|  | 
 **repository_id** | **str**|  | 

### Return type

[**LearningObjectDto**](LearningObjectDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lo_repository_controller_create_repository**
> ShallowLoRepositoryDto lo_repository_controller_create_repository(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LearningObjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoRepositoryCreationDto() # LoRepositoryCreationDto | 

try:
    api_response = api_instance.lo_repository_controller_create_repository(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningObjectsApi->lo_repository_controller_create_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoRepositoryCreationDto**](LoRepositoryCreationDto.md)|  | 

### Return type

[**ShallowLoRepositoryDto**](ShallowLoRepositoryDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lo_repository_controller_list_repositories**
> LoRepositoryListDto lo_repository_controller_list_repositories()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningObjectsApi()

try:
    api_response = api_instance.lo_repository_controller_list_repositories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningObjectsApi->lo_repository_controller_list_repositories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoRepositoryListDto**](LoRepositoryListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lo_repository_controller_load_learning_object**
> LearningObjectDto lo_repository_controller_load_learning_object(learning_object_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningObjectsApi()
learning_object_id = 'learning_object_id_example' # str | 

try:
    api_response = api_instance.lo_repository_controller_load_learning_object(learning_object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningObjectsApi->lo_repository_controller_load_learning_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learning_object_id** | **str**|  | 

### Return type

[**LearningObjectDto**](LearningObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lo_repository_controller_load_repository**
> LoRepositoryDto lo_repository_controller_load_repository(repository_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningObjectsApi()
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.lo_repository_controller_load_repository(repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningObjectsApi->lo_repository_controller_load_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**|  | 

### Return type

[**LoRepositoryDto**](LoRepositoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lo_repository_controller_modify_learning_object**
> LearningObjectDto lo_repository_controller_modify_learning_object(body, repository_id, learning_object_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LearningObjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LearningObjectModificationDto() # LearningObjectModificationDto | 
repository_id = 'repository_id_example' # str | 
learning_object_id = 'learning_object_id_example' # str | 

try:
    api_response = api_instance.lo_repository_controller_modify_learning_object(body, repository_id, learning_object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningObjectsApi->lo_repository_controller_modify_learning_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LearningObjectModificationDto**](LearningObjectModificationDto.md)|  | 
 **repository_id** | **str**|  | 
 **learning_object_id** | **str**|  | 

### Return type

[**LearningObjectDto**](LearningObjectDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lo_repository_controller_modify_repository**
> LoRepositoryDto lo_repository_controller_modify_repository(body, repository_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LearningObjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoRepositoryModifyDto() # LoRepositoryModifyDto | 
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.lo_repository_controller_modify_repository(body, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningObjectsApi->lo_repository_controller_modify_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoRepositoryModifyDto**](LoRepositoryModifyDto.md)|  | 
 **repository_id** | **str**|  | 

### Return type

[**LoRepositoryDto**](LoRepositoryDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lo_repository_controller_show_goal**
> LoGoalDto lo_repository_controller_show_goal(goal_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningObjectsApi()
goal_id = 'goal_id_example' # str | 

try:
    api_response = api_instance.lo_repository_controller_show_goal(goal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningObjectsApi->lo_repository_controller_show_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 

### Return type

[**LoGoalDto**](LoGoalDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lo_repository_controller_show_goals**
> LoGoalListDto lo_repository_controller_show_goals(repository_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningObjectsApi()
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.lo_repository_controller_show_goals(repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningObjectsApi->lo_repository_controller_show_goals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**|  | 

### Return type

[**LoGoalListDto**](LoGoalListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

