from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, '.pull-right.hidden-xs a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_EMPTY_MSG = (By.CSS_SELECTOR, '#content_inner>p')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_FORM_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_FORM_PASS1 = (By.ID, 'id_registration-password1')
    REGISTER_FORM_PASS2 = (By.ID, 'id_registration-password2')
    REGISTER_SUBMIT = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages strong')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alertinner p strong')
    BASKET_SUCCESS_MSG = 'has been added to your basket'
    BASKET_TOTAL_MSG = 'Your basket total is now'
    MESSAGES_BLOCK = (By.ID, 'messages')
    SUCCESS_MSG = (By.CSS_SELECTOR, '.alert-success')
