import time
import pytest

from pages.product_page import ProductPage
from pages.urls import CatalogueUrls


@pytest.mark.parametrize('link', *CatalogueUrls.promo_offer_urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_book_at_basket()
    page.solve_quiz_and_get_code()
    page.name_book_should_be_equal()
    page.price_book_should_be_equal()
