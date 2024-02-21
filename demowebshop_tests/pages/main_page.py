from selene import browser, query, have

from demowebshop_tests.controls.utils import post_request, BASE_URL
from demowebshop_tests.data.cards import get_data_for_adding_a_card, get_data_for_deleting_a_card

COOKIE_NAME = "NOPCOMMERCE.AUTH"


class MainPage:
    def __init__(self):
        self.search_input = browser.element('#searchInput')
        self.basket = browser.element('[class*=item-basket]')

    def add_item_to_cart(self, cookie_name, cookie):
        endpoint = "/addproducttocart/details/75/1"
        data = get_data_for_adding_a_card()
        post_request(endpoint, data, cookie_name, cookie)

    def delete_item_from_cart(self, cookie_name, cookie):
        endpoint = "/addproducttocart/details/75/1"
        data = get_data_for_deleting_a_card()
        data['addtocart_75.UpdatedShoppingCartItemId'] = browser.element('[class="remove-from-cart"] > input').get(query.attribute('value'))
        post_request(endpoint, data, cookie_name, cookie)

    def open_cart_with_item(self):
        browser.element('#topcartlink').click()
        browser.element('[class="product-name"]').should(have.text("Simple Computer"))

    def open_browser_with_cookie(self, cookie):
        browser.open(BASE_URL).driver.add_cookie({"name": COOKIE_NAME, "value": cookie})
        browser.open(BASE_URL)
