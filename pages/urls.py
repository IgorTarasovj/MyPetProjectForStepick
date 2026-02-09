import pytest


class CatalogueUrls:
    promo_offer_urls = [["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                         pytest.param(
                             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                             marks=pytest.mark.xfail),
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]]
