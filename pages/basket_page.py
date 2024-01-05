from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), (
            'Items in basket is presented, but should not be'
        )

    def should_be_basket_is_empy_msg(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MSG), (
            'Expected "basket is empty" message not found'
        )
