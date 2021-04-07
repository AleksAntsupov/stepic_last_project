from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    #Текст Корзина пуста.
    def should_be_basket_empty_with_text(self):
        assert self.is_element_present(*BasePageLocators.BASKET_IS_EMPTY), "Basket is not empty"
    
    #Корзина без книг
    def should_be_basket_without_books(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_WITH_BOOKS), "Basket have books"
    
    #Корзина без книг с ожиданием
    def should_be_basket_without_books_with_wait(self):
        assert self.is_disappeared(*BasePageLocators.BASKET_WITH_BOOKS), "Basket have books. Helped disappeared"