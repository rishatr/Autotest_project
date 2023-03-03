from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
import allure


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_price_locator = "div.accordion__body.j-b-list-content > div > div > div:nth-child(4) > div > div.list-item__price > div.list-item__price-new"
    second_price_locator = "div.accordion__body.j-b-list-content > div > div > div:nth-child(7) > div > div.list-item__price > div.list-item__price-new"
    sum_price_locator = "#basketForm > div.basket-form__sidebar.sidebar > div > div > div > div.basket-order__b-top.b-top > p > span:nth-child(2) > span"

    def get_first_price(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.first_price_locator)))

    def get_second_price(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.second_price_locator)))

    def get_sum_price(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.sum_price_locator)))

    def prices(self):
        first_price = self.get_first_price().text.removesuffix(' ₽').replace(" ", "")
        second_price = self.get_second_price().text.removesuffix(' ₽').replace(" ", "")
        sum_price = self.get_sum_price().text.removesuffix(' ₽').replace(" ", "")
        self.assert_prices(first_price, second_price, sum_price)

    # Methods
    def check(self):
        self.prices()
        self.screenshot()
