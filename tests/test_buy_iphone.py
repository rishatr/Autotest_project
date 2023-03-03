from pages.cart_page import Cart_page
from pages.main_page import Main_page
import allure


@allure.description("Test buy IPhone and airpods")
def test_buy_iphone(set_up):

    mp = Main_page(set_up)
    mp.buy_iphone()
    mp.buy_airpods()
    cp = Cart_page(set_up)
    cp.check()
