import pytest

from pages.locators import ProductPageLocators
from pages.product_page import ProductPage

URL = 'http://selenium1py.pythonanywhere.com/ru' \
      '/catalogue/the-shellcoders-handbook_209'


@pytest.mark.parametrize(
    'offer_id', [
        0, 1, 2, 3, 4, 5, 6,
        pytest.param('7', marks=pytest.mark.xfail),
        8, 9
    ]
)
def t(driver, offer_id):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/' \
           f'coders-at-work_207/?promo=offer{offer_id}'
    page = ProductPage(driver, link)
    page.open()
    page.should_be_add_to_basket_button()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_basket_msg(ProductPageLocators.BASKET_SUCCESS_MSG)
    page.should_be_basket_total_msg(ProductPageLocators.BASKET_TOTAL_MSG)
    page.should_be_expected_product_name_in_msg(product_name)
    page.should_be_expected_total_in_msg(product_price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    page = ProductPage(driver, URL)
    page.open()
    page.should_be_add_to_basket_button()
    page.click_add_to_basket_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    page = ProductPage(driver, URL)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    page = ProductPage(driver, URL)
    page.open()
    page.should_be_add_to_basket_button()
    page.click_add_to_basket_button()
    page.should_be_success_message_disappear()


def test_guest_should_see_login_link_on_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue' \
           '/the-city-and-the-stars_95/'
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_from_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue' \
           '/the-city-and-the-stars_95/'
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()
