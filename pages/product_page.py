from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_book_at_basket(self):
        self.should_be_button_add_product_to_basket()
        self.go_to_alert_when_click_button()

    def should_be_button_add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.add_to_basket_form), "add_to_basket_form not found"

    def go_to_alert_when_click_button(self):
        button = self.browser.find_element(*ProductPageLocators.add_to_basket_form)
        button.click()

    def should_be_message_product_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.message_add_product)

    def name_book_should_be_equal(self):
        name_book_in_msg_add_product = self.browser.find_element(*ProductPageLocators.name_book_in_msg_add_product).text
        name_book = self.browser.find_element(*ProductPageLocators.name_book).text
        assert name_book == name_book_in_msg_add_product, "name book is not equal"

    def should_be_message_cost(self):
        assert self.is_element_present(*ProductPageLocators.message_cost)

    def price_book_should_be_equal(self):
        price_book = self.browser.find_element(*ProductPageLocators.price_book).text
        price_in_message_cost = self.browser.find_element(*ProductPageLocators.price_in_message_cost).text
        assert price_book == price_in_message_cost, "price is not equal"