import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def set_up():
    print("START TEST")
    options = Options()
    options.add_argument("--window-size=1920,800")
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(executable_path="C:\\Users\\Ришат\\PycharmProjects\\Chromedriver\\chromedriver.exe"), options=options)
    url = "https://www.wildberries.ru/"
    driver.get(url)
    driver.maximize_window()

    yield driver

    driver.quit()
    print(" FINISH TEST")
