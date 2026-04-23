from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.basket_title), "basket is not empty"

    def should_be_message_if_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.message_basket_is_empty), "message not found"
