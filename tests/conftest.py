import pytest
from demowebshop_tests.controls.utils import post_request, BASE_URL
from demowebshop_tests.pages.main_page import MainPage
from demowebshop_tests.pages.main_page import COOKIE_NAME
from selene import browser

EMAIL = "demotestqaguru@mail.ru"
LOGIN = "123456789"


def get_cookie():
    endpoint = "/login"
    response = post_request(endpoint, data={"Email": f"{EMAIL}", "Password": f"{LOGIN}"})
    cookie = response.cookies.get(f"{COOKIE_NAME}")
    return cookie


cookie = get_cookie()


@pytest.fixture()
def add_item_with_api():
    main_page = MainPage()
    main_page.add_item_to_cart(COOKIE_NAME, cookie)

    yield

    main_page.delete_item_from_cart(COOKIE_NAME, cookie)


@pytest.fixture(autouse=True)
def browser_settings():
    browser.config.window_width = '1900'
    browser.config.window_height = '1028'
