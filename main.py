from __future__ import print_function
import time
import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
from pprint import pprint

config = cloudmersive_validate_api_client.Configuration()
config.api_key['Apikey'] = '5cd1cb83-8cda-4238-be5e-6a500f9ef702'

api_instance = cloudmersive_validate_api_client.IPAddressApi(cloudmersive_validate_api_client.ApiClient(config))
value = '\"120.106.179.169\"'

try:
    #geolocate an Ip address
    api_response = api_instance.i_p_address_post(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAddressAPI->i_p_address_post:%s\n" % e)
