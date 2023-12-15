from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )

    def click_add_to_basket_button(self):
        self.driver.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ).click()

    def get_product_name(self):
        return self.driver.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

    def get_product_price(self):
        return self.driver.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

    def should_be_added_to_basket_msg(self, expected_msg: str):
        assert expected_msg in self.driver.find_element(
            *ProductPageLocators.MESSAGES_BLOCK
        ).text, f'Did not find {expected_msg!r} in messages block'

    def should_be_basket_total_msg(self, total_msg: str):
        assert total_msg in self.driver.find_element(
            *ProductPageLocators.MESSAGES_BLOCK
        ).text, f'Did not find {total_msg!r} in messages block'

    def should_be_expected_product_name_in_msg(self, expected_name: str):
        current_name = self.driver.find_element(
            *ProductPageLocators.ADDED_PRODUCT_NAME
        ).text
        assert expected_name == current_name, (
            f'Wrong product name! Expected {expected_name!r},'
            f'got {current_name!r} instead'
        )

    def should_be_expected_total_in_msg(self, expected_total: str):
        current_total = self.driver.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text
        assert expected_total == current_total, (
            f'Wrong basket total! Expected {expected_total!r},'
            f'got {current_total!r} instead'
        )

