import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as ec
from utilities.logger import Logger
import allure


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    menu_locator = "body > div.wrapper > header > div > div.header__bottom > div.header__nav-element.nav-element > button > span"
    elektronika_locator = ".menu-burger__main-list-link.menu-burger__main-list-link--4830"
    phones_locator = "ul.menu-catalog__list-2.maincatalog-list-2 > li:nth-child(12) > a"
    smartphones_locator = "ul.menu-catalog__list-2.maincatalog-list-2 > li.deny-li.opened > ul > li:nth-child(10) > a"
    filter_locator = ".dropdown-filter__btn.dropdown-filter__btn--all"
    checkbox_locator = "div.filters-desktop__item.j-filter-container.filters-desktop__item--type-1.filters-desktop__item--fbrand.open.show > div.filter > ul > li:nth-child(3) > div"
    max_price_locator = "[name='endN']"
    ready_button_locator = ".filters-desktop__btn-main.btn-main"
    iphone_locator = "#c139448124 > div > a > div.product-card__img > div.product-card__img-wrap.img-plug.j-thumbnail-wrap"
    add_to_cart_locator = "div.product-page__aside-container.j-price-block > div:nth-child(2) > div > button:nth-child(2)"
    cart_locator = ".navbar-pc__icon.navbar-pc__icon--basket"
    search_box_locator = "#searchInput"
    airpods_locator = "#c147716518 > div > a > div.product-card__img > div.product-card__img-wrap.img-plug.j-thumbnail-wrap"
    price_locator = "div.product-page__price-block.product-page__price-block--aside > div > div > p > span > ins"

    # Getters
    def get_menu_locator(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.menu_locator)))

    def get_elektronika_locator(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.elektronika_locator)))

    def get_phones_locator(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.phones_locator)))

    def get_smartphones_locator(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.smartphones_locator)))

    def get_filter_locator(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.filter_locator)))

    def get_checkbox_locator(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.checkbox_locator)))

    def get_max_price_locator(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.max_price_locator)))

    def get_ready_button_locator(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.ready_button_locator)))

    def get_iphone_locator(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.iphone_locator)))

    def get_add_to_cart_locator(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.add_to_cart_locator)))

    def get_cart_locator(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.cart_locator)))

    def get_search_box(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.search_box_locator)))

    def get_airpods(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.airpods_locator)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.price_locator)))

    # Actions

    def click_menu(self):
        # self.get_menu_locator().click()
        ActionChains(self.driver).double_click(self.get_menu_locator()).perform()
        print("click menu")

    def click_elektronika(self):
        self.get_elektronika_locator().click()
        print("click elektronika")

    def click_phones(self):
        self.get_phones_locator().click()
        print("click phones")

    def click_smartphones(self):
        self.get_smartphones_locator().click()
        print("click smartphones")

    def click_filter(self):
        self.get_filter_locator().click()
        print("click filter")

    def click_checkbox(self):
        self.get_checkbox_locator().click()
        print("click checkbox")

    def input_max_price(self, price):
        self.get_max_price_locator().clear()
        self.get_max_price_locator().send_keys(price)
        print("input max price")

    def click_ready_button(self):
        self.get_ready_button_locator().click()
        print("click ready price button")

    def click_iphone(self):
        self.get_iphone_locator().click()
        print("click iphone")

    def click_add_to_cart(self):
        self.get_add_to_cart_locator().click()
        print("click add to cart")

    def click_cart(self):
        self.get_cart_locator().click()
        print("click cart")

    def search(self, product):
        self.get_search_box().click()
        self.get_search_box().send_keys(product)
        self.get_search_box().send_keys(Keys.ENTER)
        print("search")

    def click_airpods(self):
        self.get_airpods().click()
        print("click airpods")

    def read_price(self):
        return self.get_price().text

    # Methods
    def buy_iphone(self):
        with allure.step("Buy IPhone"):
            Logger.add_start_step(method="buy_iphone")
            self.click_menu()
            self.click_elektronika()
            self.click_phones()
            self.click_smartphones()
            self.click_filter()
            self.click_checkbox()
            time.sleep(1)
            self.input_max_price("100000")
            self.click_ready_button()
            self.click_iphone()
            self.click_add_to_cart()
            Logger.add_end_step(url=self.driver.current_url, method="buy_iphone")

    def buy_airpods(self):
        with allure.step("Buy airpods"):
            Logger.add_start_step(method="buy_airpods")
            self.search("apple airpods pro")
            self.click_airpods()
            self.click_add_to_cart()
            self.click_cart()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method="buy_airpods")
