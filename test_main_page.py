from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

LINK = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_basket_is_empy_msg()
