from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_linc_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    EMAIL_ADDRESS = (By.ID, "id_registration-email")
    PASSWORD = (By.ID, "id_registration-password1")
    PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")
    
class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_ADDING_TO_CART = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    NAME_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong")
    MESSAGE_COST_PRODUCT = (By.CSS_SELECTOR, "#messages :nth-child(3) p")
    COST_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    COST_PRODUCT_IN_MESSAGE = (By. CSS_SELECTOR, "#messages :nth-child(3) p strong")
    
class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")