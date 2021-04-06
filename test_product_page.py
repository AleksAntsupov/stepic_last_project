from .pages.main_page import MainPage
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    page.should_be_button_add_to_backet()
    page.go_to_add_bascket()
    page.solve_quiz_and_get_code()
    page.should_be_namebook_equal_book_in_basket()
    page.should_be_price_equal_price_book()