from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('offer_number', ["0","1","2","3","4","5","6",pytest.param("7",marks=pytest.mark.xfail),"8","9"])
def test_guest_can_add_product_to_basket(browser,offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    page = ProductPage(browser,link)
    page.open()
    page.add_product()
    page.solve_quiz_and_get_code()
    page.should_be_right_book()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser,link)
    page.open()
    page.add_product()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    page.solve_quiz_and_get_code()
    page.buy_message_should_disappeared()