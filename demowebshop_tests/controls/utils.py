import requests

BASE_URL = "https://demowebshop.tricentis.com"


def post_request(endpoint, data, cookie_name=None, cookie=None):
    if endpoint == "/login":
        response = requests.post(BASE_URL + endpoint, data=data, allow_redirects=False)
        return response
    response = requests.post(BASE_URL + endpoint, data=data, cookies={cookie_name: cookie}, allow_redirects=False)
    return response
