import os
import pytest
from demowebshop_tests.controls.utils import post_request, BASE_URL
from demowebshop_tests.pages.main_page import MainPage
from demowebshop_tests.pages.main_page import COOKIE_NAME
from selene import browser
from dotenv import load_dotenv
from demowebshop_tests.controls import attach


def load_env():
    load_dotenv()


def get_cookie():
    load_env()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    endpoint = "/login"
    response = post_request(endpoint, data={"Email": f"{email}", "Password": f"{password}"})
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
    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
