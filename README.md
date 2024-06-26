# dynamicdnsapi
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Generator version: 7.6.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/dynamicdns-pro/python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/dynamicdns-pro/python.git`)

Then import the package:
```python
import dynamicdnsapi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dynamicdnsapi
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import dynamicdnsapi
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
    except ApiException as e:
        print("Exception when calling SubdomainApi->update: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://dynamicdns.pro/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SubdomainApi* | [**update**](docs/SubdomainApi.md#update) | **POST** /{subdomain}/record | 
*SubdomainApi* | [**updateip**](docs/SubdomainApi.md#updateip) | **POST** /{subdomain} | update the ip address with the connecting ip address


## Documentation For Models

 - [Update200Response](docs/Update200Response.md)
 - [Update200ResponseAnyOf](docs/Update200ResponseAnyOf.md)
 - [Update400Response](docs/Update400Response.md)
 - [Update403Response](docs/Update403Response.md)
 - [UpdateRequest](docs/UpdateRequest.md)
 - [Updateip200Response](docs/Updateip200Response.md)
 - [Updateip200ResponseAnyOf](docs/Updateip200ResponseAnyOf.md)
 - [Updateip400Response](docs/Updateip400Response.md)
 - [Updateip403Response](docs/Updateip403Response.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="http"></a>
### http

- **Type**: Bearer authentication ()


## Author




