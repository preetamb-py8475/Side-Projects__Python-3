
import json


"""
                    JSON Values from User-Input JSON file
                    *************************************
"""


with open('JSON_Input_Attack.json') as x:
    json_attack = json.load(x)

IP = json_attack['DUT'][0]['Attacks'][0]['IP']
Host = json_attack['DUT'][0]['Attacks'][0]['Host']
CDN_Header = json_attack['DUT'][0]['Attacks'][0]['CDN_Header']
CDN_IP = json_attack['DUT'][0]['Attacks'][0]['CDN_IP']
params_QueryParameters_Param = json_attack['DUT'][0]['Attacks'][0]['params_QueryParameters_Param']
params_QueryParameters_Value = json_attack['DUT'][0]['Attacks'][0]['params_QueryParameters_Value']
json_BodyJSON_Param = json_attack['DUT'][0]['Attacks'][0]['json_BodyJSON_Param']
json_BodyJSON_Value = json_attack['DUT'][0]['Attacks'][0]['json_BodyJSON_Value']
data_BodyURLEncoded_Param = json_attack['DUT'][0]['Attacks'][0]['data_BodyURLEncoded_Param']
data_BodyURLEncoded_Value = json_attack['DUT'][0]['Attacks'][0]['data_BodyURLEncoded_Value']
Request_Type = json_attack['DUT'][0]['Attacks'][0]['Request_Type']
HTTP_Method = json_attack['DUT'][0]['Attacks'][0]['HTTP_Method']
Attack = json_attack['DUT'][0]['Attacks'][0]['Attack']
