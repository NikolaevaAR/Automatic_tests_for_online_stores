# Шаги:
    # 1. Открыть страницу товара
    # 2. Нажать кнопку "Добавить в корзину"
    # 3. Посчитать математическое выражение и ввести его в алерт
    # 4. Проверить:
        # есть сообщение о том, что товар добавлен в корзину:
            # название товара совпдает с тем, что было добавлено
        # есть сообщение со стоимостью корзины:
            # стоимость корзины совпадает с ценой товара

import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('n', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_cart(browser, n):
    
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}"
    print(f"Проверяется ссылка {link}")
    page = ProductPage(browser,link)
    page.open()
    
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_adding_to_cart()
    page.should_be_message_cost_of_the_cart()