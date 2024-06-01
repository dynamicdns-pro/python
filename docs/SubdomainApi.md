# dynamicdnsapi.SubdomainApi

All URIs are relative to *https://dynamicdns.pro/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update**](SubdomainApi.md#update) | **POST** /{subdomain}/record | 
[**updateip**](SubdomainApi.md#updateip) | **POST** /{subdomain} | update the ip address with the connecting ip address


# **update**
> Update200Response update(subdomain, update_request=update_request)



### Example

* Bearer () Authentication (http):

```python
import dynamicdnsapi
from dynamicdnsapi.models.update200_response import Update200Response
from dynamicdnsapi.models.update_request import UpdateRequest
from dynamicdnsapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dynamicdns.pro/api
# See configuration.py for a list of all supported configuration parameters.
configuration = dynamicdnsapi.Configuration(
    host = "https://dynamicdns.pro/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (): http
configuration = dynamicdnsapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dynamicdnsapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dynamicdnsapi.SubdomainApi(api_client)
    subdomain = 'subdomain_example' # str | 
    update_request = dynamicdnsapi.UpdateRequest() # UpdateRequest |  (optional)

    try:
        api_response = api_instance.update(subdomain, update_request=update_request)
        print("The response of SubdomainApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubdomainApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subdomain** | **str**|  | 
 **update_request** | [**UpdateRequest**](UpdateRequest.md)|  | [optional] 

### Return type

[**Update200Response**](Update200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | An error |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**422** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateip**
> Updateip200Response updateip(subdomain, body=body)

update the ip address with the connecting ip address

### Example

* Bearer () Authentication (http):

```python
import dynamicdnsapi
from dynamicdnsapi.models.updateip200_response import Updateip200Response
from dynamicdnsapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dynamicdns.pro/api
# See configuration.py for a list of all supported configuration parameters.
configuration = dynamicdnsapi.Configuration(
    host = "https://dynamicdns.pro/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (): http
configuration = dynamicdnsapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dynamicdnsapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dynamicdnsapi.SubdomainApi(api_client)
    subdomain = 'subdomain_example' # str | 
    body = None # object |  (optional)

    try:
        # update the ip address with the connecting ip address
        api_response = api_instance.updateip(subdomain, body=body)
        print("The response of SubdomainApi->updateip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubdomainApi->updateip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subdomain** | **str**|  | 
 **body** | **object**|  | [optional] 

### Return type

[**Updateip200Response**](Updateip200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | An error |  -  |
**401** |  |  -  |
**403** | An error |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

