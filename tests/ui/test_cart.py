from demowebshop_tests.pages.main_page import MainPage
from tests.conftest import cookie
from demowebshop_tests.pages.main_page import COOKIE_NAME


def test_update_total_price(add_item_with_api):
    main_page = MainPage()
    main_page.open_browser_with_cookie(cookie)
    main_page.open_cart_with_item()
    main_page.change_count()
    main_page.check_total_price()


def test_remove_item_from_cart():
    main_page = MainPage()
    main_page.add_item_to_cart(COOKIE_NAME, cookie)

    main_page.open_browser_with_cookie(cookie)
    main_page.open_cart_with_item()
    main_page.delete_item()

    main_page.check_empty_cart()
