from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.skip 
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.skip 
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip     
def test_guest_can_to_see_page_login_and_reg(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser,link)
    page.open()
    page.should_be_login_page()

   
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_without_books()
    page.should_be_basket_without_books_with_wait()
    page.should_be_basket_empty_with_text()
    
    
# def test_guest_can_to_see_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    # page = LoginPage(browser, link)
    # page.open()
    # page.should_be_login_url()

# def test_guest_can_to_see_form_login(browser):
    # link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    # page = LoginPage(browser,link)
    # page.open()
    # page.should_be_login_form()

# def test_guest_can_to_see_form_registration(browser):
    # link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    # page = LoginPage(browser,link)
    # page.open()
    # page.should_be_register_form()