# coding: utf-8

"""
    Dynamicdns.pro

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dynamicdnsapi.models.updateip200_response import Updateip200Response

class TestUpdateip200Response(unittest.TestCase):
    """Updateip200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Updateip200Response:
        """Test Updateip200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Updateip200Response`
        """
        model = Updateip200Response()
        if include_optional:
            return Updateip200Response(
                message = 'Record updated'
            )
        else:
            return Updateip200Response(
                message = 'Record updated',
        )
        """

    def testUpdateip200Response(self):
        """Test Updateip200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()