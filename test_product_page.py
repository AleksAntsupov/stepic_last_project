import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage


# @pytest.mark.parametrize('links', ["0","1","2","3","4","5","6",pytest.param("7",marks=pytest.mark.xfail),"8","9",])
# def test_guest_can_add_product_to_basket(browser, links):
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{links}"
    # page = ProductPage(browser,link)
    # page.open()
    # page.should_be_button_add_to_backet()
    # page.go_to_add_bascket()
    # page.solve_quiz_and_get_code()
    # page.should_be_namebook_equal_book_in_basket()
    # page.should_be_price_equal_price_book()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_bascket()
    page.should_not_be_success_message()
    page.should_not_be_success_message_two()
    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_bascket()
    page.should_not_be_success_message_two()