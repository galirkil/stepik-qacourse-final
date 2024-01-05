import time

import pytest

from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage

URL = 'http://selenium1py.pythonanywhere.com/ru' \
      '/catalogue/the-shellcoders-handbook_209'


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(driver, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, 'password123456789')
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/' \
               'coders-at-work_207/'
        page = ProductPage(driver, link)
        page.open()
        page.should_be_add_to_basket_button()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.click_add_to_basket_button()
        page.should_be_added_to_basket_msg(
            ProductPageLocators.BASKET_SUCCESS_MSG)
        page.should_be_basket_total_msg(ProductPageLocators.BASKET_TOTAL_MSG)
        page.should_be_expected_product_name_in_msg(product_name)
        page.should_be_expected_total_in_msg(product_price)

    def test_user_cant_see_success_message(self, driver):
        page = ProductPage(driver, URL)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/' \
           'coders-at-work_207/'
    page = ProductPage(driver, link)
    page.open()
    page.should_be_add_to_basket_button()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.click_add_to_basket_button()
    page.should_be_added_to_basket_msg(
        ProductPageLocators.BASKET_SUCCESS_MSG)
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


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue' \
           '/the-city-and-the-stars_95/'
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    page = ProductPage(driver, URL)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_basket_is_empy_msg()
