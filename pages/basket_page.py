from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    
    def should_be_not_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Товары есть в корзине, хотя их не должно быть"
        
    def should_be_a_text_the_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Отсутствует сообщение о том, что корзина пуста" 
        basket_empty_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert "Your basket is empty" in basket_empty_text, "Cообщение о том, что корзина пуста, неверное" 