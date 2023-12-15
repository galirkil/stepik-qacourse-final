import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


@pytest.mark.parametrize(
    'offer_id', [
        0, 1, 2, 3, 4, 5, 6,
        pytest.param('7', marks=pytest.mark.xfail),
        8, 9
    ]
)
def test_guest_can_add_product_to_basket(driver, offer_id):
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
