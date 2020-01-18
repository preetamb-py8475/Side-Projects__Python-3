
import requests


def select_http_method(m):
	"""
                    My Python Script : HTTP Method Selection Tool
                    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	"""
	
    m = m.lower()
    print(f"HTTP Method : {m}")

    if m == 'get':
        return requests.get

    elif m == 'post':
        return requests.post

    elif m == 'put':
        return requests.put

    elif m == 'delete':
        return requests.delete

    elif m == 'head':
        return requests.head

    elif m == 'options':
        return requests.options

    elif m == 'patch':
        return requests.patch
