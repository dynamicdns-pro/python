# Updateip200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**ip** | **str** |  | 

## Example

```python
from dynamicdnsapi.models.updateip200_response import Updateip200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Updateip200Response from a JSON string
updateip200_response_instance = Updateip200Response.from_json(json)
# print the JSON string representation of the object
print(Updateip200Response.to_json())

# convert the object into a dict
updateip200_response_dict = updateip200_response_instance.to_dict()
# create an instance of Updateip200Response from a dict
updateip200_response_from_dict = Updateip200Response.from_dict(updateip200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


