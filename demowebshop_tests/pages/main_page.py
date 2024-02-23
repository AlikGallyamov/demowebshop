from selene import browser, query, have
import allure
from demowebshop_tests.controls.utils import post_request, BASE_URL
from demowebshop_tests.data.cards import get_data_for_adding_a_card, get_data_for_deleting_a_card

COOKIE_NAME = "NOPCOMMERCE.AUTH"


class MainPage:
    def __init__(self):
        self.search_input = browser.element('#searchInput')
        self.basket = browser.element('[class*=item-basket]')
        self.update_cart = browser.element('[name="updatecart"]')

    def add_item_to_cart(self, cookie_name, cookie):
        with allure.step("Добавляем товар в корзину через API"):
            endpoint = "/addproducttocart/details/75/1"
            data = get_data_for_adding_a_card()
            post_request(endpoint, data, cookie_name, cookie)

    def delete_item_from_cart(self, cookie_name, cookie):
        with allure.step("Удаляем товар из корзины через АПИ"):
            endpoint = "/addproducttocart/details/75/1"
            data = get_data_for_deleting_a_card()
            data['addtocart_75.UpdatedShoppingCartItemId'] = browser.element('[class="remove-from-cart"] > input').get(
                query.attribute('value'))
            post_request(endpoint, data, cookie_name, cookie)

    def open_cart_with_item(self):
        with allure.step("Открываем корзину"):
            browser.element('#topcartlink').click()
        with allure.step("Ищем товар"):
            browser.element('[class="product-name"]').should(have.text("Simple Computer"))

    def open_browser_with_cookie(self, cookie):
        with allure.step("Авторизуемся через куки"):
            browser.open(BASE_URL).driver.add_cookie({"name": COOKIE_NAME, "value": cookie})
            browser.open(BASE_URL)

    def change_count(self):
        with allure.step("Изменяем количество товаров"):
            browser.element('[name*="itemquantity"]').clear()
            browser.element('[name*="itemquantity"]').type('2')
        with allure.step("Обновляем корзину"):
            self.update_cart().click()

    def check_total_price(self):
        with allure.step("Проверем суммарную цену в корзине"):
            browser.element('[class="product-subtotal"]').should(have.text('1600.00'))

    def delete_item(self):
        with allure.step("Отмечаем чекбокс удаления товара"):
            browser.element('[name="removefromcart"]').click()
        with allure.step("Обновляем корзину"):
            self.update_cart().click()

    def check_empty_cart(self):
        with allure.step("Проверяем, что корзина пустая"):
            browser.element('[class*="summary-content"]').should(have.text('Your Shopping Cart is empty'))
