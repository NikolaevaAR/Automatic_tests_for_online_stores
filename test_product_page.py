import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link1 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
link_registration = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

# @pytest.mark.parametrize('n', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()
    page.add_to_cart()
    #page.solve_quiz_and_get_code()
    page.should_be_message_adding_to_cart()
    page.should_be_message_cost_of_the_cart()
    page.should_disappeared_success_message()
    
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_to_cart()
    page.should_disappeared_success_message()
    
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.go_to_login_page()
    

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_not_items_in_the_basket()
    basket_page.should_be_a_text_the_basket_is_empty()
    

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope = "function", autouse = True)
    def setup(self, browser):
        page_registration = LoginPage(browser,link_registration)
        page_registration.open()
        email = str(time.time()) + "@fakemail.org"
        password = "ghbdtnvbh123"
        page_registration.register_new_user(email, password)
        page_registration.should_be_authorized_user()
        time.sleep(10)
        
    
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()
    
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()
        page.add_to_cart()
        page.should_be_message_adding_to_cart()
        page.should_be_message_cost_of_the_cart()
        page.should_disappeared_success_message()
    