# coding: utf-8

"""
    Dynamicdns.pro

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dynamicdnsapi.models.updateip403_response import Updateip403Response

class TestUpdateip403Response(unittest.TestCase):
    """Updateip403Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Updateip403Response:
        """Test Updateip403Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Updateip403Response`
        """
        model = Updateip403Response()
        if include_optional:
            return Updateip403Response(
                message = ''
            )
        else:
            return Updateip403Response(
                message = '',
        )
        """

    def testUpdateip403Response(self):
        """Test Updateip403Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()