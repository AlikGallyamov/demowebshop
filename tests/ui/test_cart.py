from selene import browser, be
import requests

BASE_URL = "https://demowebshop.tricentis.com"
EMAIL = "demotestqaguru@mail.ru"
LOGIN = "123456789"
COOKIE_NAME = "NOPCOMMERCE.AUTH"


def get_cookie():
    response = requests.post(BASE_URL + "/login", json={"Email": f"{EMAIL}", "Password": f"{LOGIN}"},
                             allow_redirects=False)
    cookie = response.cookies.get(f"{COOKIE_NAME}")
    return cookie
    # browser.open(BASE_URL).driver.add_cookie({"name": COOKIE_NAME, "value": cookie})
    # browser.open(BASE_URL)


def add_item_to_cart(cookie):
    method_name = "/addproducttocart/details/75/1"
    data = {
        "product_attribute_75_5_31": 96,
        "product_attribute_75_6_32": 100,
        "product_attribute_75_3_33": 102,
        "addtocart_75.EnteredQuantity": 1
    }
    response = requests.post(BASE_URL + method_name, data=data, cookies={"name": COOKIE_NAME, "value": cookie},
                             allow_redirects=False)
    print(response.text)


def test_open_cart_with_item():
    cookie = get_cookie()
    add_item_to_cart(cookie)
    browser.open(BASE_URL).driver.add_cookie({"name": COOKIE_NAME, "value": cookie})

    browser.open(BASE_URL)
    browser.element('#topcartlink').click()
    browser.element(['[class="product-name"]']).should(be.visible)
