from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages strong')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alertinner p strong')
    BASKET_SUCCESS_MSG = 'has been added to your basket'
    BASKET_TOTAL_MSG = 'Your basket total is now'
    MESSAGES_BLOCK = (By.ID, 'messages')

