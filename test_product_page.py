import pytest
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time



#Новый класс для практики в setup/teardown
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "1"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email,password)
        self.page.should_be_authorized_user()
     
    #Юзеру не видно успешное сообщение о добавлении книги в корзину
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    #Юзер может добавить книгу в корзину
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link)
        page.open()
        page.should_be_button_add_to_backet()
        page.go_to_add_bascket()
        #page.solve_quiz_and_get_code()
        page.should_be_namebook_equal_book_in_basket()
        page.should_be_price_equal_price_book()



#Ищет баг в офферах
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


#Не может увидеть товар в корзине со страницы товара
@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_without_books()
    page.should_be_basket_without_books_with_wait()
    page.should_be_basket_empty_with_text()





#Ссылка на логин со страницы товара
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

#Можно перейти на логин со страницы товара
@pytest.mark.skip    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()

#Не видно успешное сообщение о добавлении книги в корзину
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_bascket()
    page.should_not_be_success_message()
    page.should_not_be_success_message_two()

#Не видно успешное сообщение о добавлении книги в корзину 
@pytest.mark.skip    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

#Не видно успешное сообщение о добавлении книги в корзину с ожиданием    
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_bascket()
    page.should_not_be_success_message_two()