import datetime

class Base():

    def __init__(self, driver):

        self.driver = driver

    """Method assert prices"""

    def assert_prices(self, first_price, second_price, sum_price):
        assert int(sum_price) == int(first_price) + int(second_price), "Incorrect prices"
        print("Correct prices")

    """Method screenshot"""

    def screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        screenshot_name = "business_way" + now_date + ".png"
        self.driver.save_screenshot("C:\\Users\\Ришат\\Autotest_project\\screens\\" + screenshot_name)
