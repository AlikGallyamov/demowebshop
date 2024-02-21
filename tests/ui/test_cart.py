from demowebshop_tests.pages.main_page import MainPage
from tests.conftest import cookie


def test_update_total_price(add_item_with_api):
    main_page = MainPage()
    main_page.open_browser_with_cookie(cookie)
    main_page.open_cart_with_item()
