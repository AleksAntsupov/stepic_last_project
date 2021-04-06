from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_button_add_to_backet(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button for add to basket not found"
    
    def go_to_add_bascket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click(), "Click is not button basket"
    
    def should_be_namebook_equal_book_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.NAME_BOOK_FOR_BASKET), "Name book is not found"
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK_FOR_BASKET).text
        assert self.is_element_present(*ProductPageLocators.BOOK_ADDED_IN_BASKET), "Name book for add to basket is not found"
        book_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_ADDED_IN_BASKET).text
        assert name_book == book_in_basket, "Name book and name book added in basket are not equal"
    
    def should_be_price_equal_price_book(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Book price is not found"
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        # book_price_t = book_price.text
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_ADDED_IN_BASKET), "Book price book added in basket is not found"
        book_price_added_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ADDED_IN_BASKET).text
        # book_price_added_in_basket_t = book_price_added_in_basket.text
        assert book_price == book_price_added_in_basket, "Prices are not equal"