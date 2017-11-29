from driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomeScreen:

    def __init__(self, driver):
        self.driver = driver
        self.searchInput = self.driver.instance.find_element(By.ID, "searchInput")
        self.desiredResult = 0

    def search_for_results(self, value):
        if isinstance(value, str):
            self.searchInput.send_keys(value + Keys.RETURN)
        else:
            raise TypeError("Value must be a string")

    def click_desired_result(self, value):
        if isinstance(value, str):
            self.desiredResult = self.driver.instance.find_element(By.LINK_TEXT, value)
            self.desiredResult.click()
        else:
            raise TypeError("Value must be a string")
