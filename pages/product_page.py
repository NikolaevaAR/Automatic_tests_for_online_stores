from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Кнопка добавления в корзину не найдена"
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button_add_to_cart.click()
        
    def should_be_message_adding_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADDING_TO_CART), "Сообщение о добавлении в корзину отсутствует"
        self.should_be_match_in_the_product_names()
        
    def should_be_message_cost_of_the_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_COST_PRODUCT), "Сообщение о стоимости корзины отсутствует"
        self.should_be_match_in_the_cost_product()
        
    def should_be_match_in_the_product_names(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_in_message = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE).text
        assert name_product == name_product_in_message, "Название книги не совпадает"
        
    def should_be_match_in_the_cost_product(self):
        cost_product = self.browser.find_element(*ProductPageLocators.COST_PRODUCT).text
        cost_product_in_message = self.browser.find_element(*ProductPageLocators.COST_PRODUCT_IN_MESSAGE).text
        assert cost_product == cost_product_in_message, "Цена товара не совпадает"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADDING_TO_CART), "Сообщение о добавлении товара не должно было появиться"
        
    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADDING_TO_CART), "Сообщение о добавлении товара не исчезло, хотя должно было исчезнуть"
    