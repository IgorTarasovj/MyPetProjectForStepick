from selenium.webdriver.common.by import By


class MainPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    register_form = (By.CSS_SELECTOR, "#register_form")
    login_form = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators():
    add_to_basket_form = (By.CSS_SELECTOR, "#add_to_basket_form")
    message_add_product = (By.PARTIAL_LINK_TEXT, "has been added to your basket")
    message_cost = (By.PARTIAL_LINK_TEXT, "Your basket total is now")
    price_in_message_cost = (By.CSS_SELECTOR, "div #messages .alertinner :nth-child(1) strong")
    price_book = (By.CSS_SELECTOR, ".product_main .price_color")
    name_book = (By.CSS_SELECTOR, ".product_main h1")
    name_book_in_msg_add_product = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong ")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    button_open_basket = (By.CSS_SELECTOR, ".btn-group a")

class BasketPageLocators():
    basket_title = (By.CSS_SELECTOR, ".basket-title")
    message_basket_is_empty = (By.CSS_SELECTOR, "#content_inner > p")

