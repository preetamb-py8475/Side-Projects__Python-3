
import urllib3
import time


from HTTP_Method_Selection_Tool import select_http_method

from Obj_JSON_Input_Attack import IP
from Obj_JSON_Input_Attack import Host
from Obj_JSON_Input_Attack import CDN_Header
from Obj_JSON_Input_Attack import CDN_IP
from Obj_JSON_Input_Attack import params_QueryParameters_Param
from Obj_JSON_Input_Attack import params_QueryParameters_Value
from Obj_JSON_Input_Attack import json_BodyJSON_Param
from Obj_JSON_Input_Attack import json_BodyJSON_Value
from Obj_JSON_Input_Attack import data_BodyURLEncoded_Param
from Obj_JSON_Input_Attack import data_BodyURLEncoded_Value
from Obj_JSON_Input_Attack import Request_Type
from Obj_JSON_Input_Attack import HTTP_Method
from Obj_JSON_Input_Attack import Attack


def ingenious_attack():
	"""
                    My Python Script : An Intelligent Attack Tool
                    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	"""
	
    url_traffic = None
    if Host == "":
        url_traffic = f'{Request_Type}://{IP}/{Attack}'
    elif Host != "":
        url_traffic = f'{Request_Type}://{Host}/{Attack}'
    print("\n")
    print(url_traffic)

    print()
    headers = {
        # "Content-Type": "application/json",
        # "Content-Type": "application/x-www-form-urlencoded",
        CDN_Header: CDN_IP
    }
    print(headers)

    print()
    params = {params_QueryParameters_Param: params_QueryParameters_Value}
    print(params)

    print()
    json_payload = {json_BodyJSON_Param: json_BodyJSON_Value}
    print(json_payload)

    print()
    data_payload = {data_BodyURLEncoded_Param: data_BodyURLEncoded_Value}
    print(data_payload)

    time.sleep(5)

    m = HTTP_Method.lower()

    response = None
    if m == "post":
        if json_payload != {'': ''}:
            urllib3.disable_warnings()
            response = select_http_method(HTTP_Method)(
                url_traffic,
                verify=False,
                json=json_payload,
                headers=headers
            )
        elif data_payload != {'': ''}:
            urllib3.disable_warnings()
            response = select_http_method(HTTP_Method)(
                url_traffic,
                verify=False,
                data=data_payload,
                headers=headers
            )
        elif json_payload and data_payload == {'': ''}:
            urllib3.disable_warnings()
            response = select_http_method(HTTP_Method)(
                url_traffic,
                verify=False,
                params=params,
                headers=headers
            )
    elif m != "post":
		if CDN_IP == "":
			urllib3.disable_warnings()
			response = select_http_method(HTTP_Method)(
				url_traffic,
				verify=False,
				params=params
			)
		elif CDN_IP != "":
			urllib3.disable_warnings()
			response = select_http_method(HTTP_Method)(
				url_traffic,
				verify=False,
				params=params,
                headers=headers
			)

    print(response.status_code)
    print(response.headers)
    print(response.content)

    return response


# print(ingenious_attack())
