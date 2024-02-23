import logging

import curlify
import requests
import allure
from allure_commons._allure import step
from allure_commons.types import AttachmentType

BASE_URL = "https://demowebshop.tricentis.com"


def post_request(endpoint, data, cookie_name=None, cookie=None):
    if endpoint == "/login":
        response = requests.post(BASE_URL + endpoint, data=data, allow_redirects=False)
    else:
        response = requests.post(BASE_URL + endpoint, data=data, cookies={cookie_name: cookie}, allow_redirects=False)
    with step(f"POST request {BASE_URL + endpoint}"):
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
    return response
