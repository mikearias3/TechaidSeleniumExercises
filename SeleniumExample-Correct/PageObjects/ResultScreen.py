from Driver import Driver
from selenium.webdriver.common.by import By


class ResultScreen:

    def __init__(self, driver):
        self.driver = driver
        self.articleHeader = self.driver.instance.find_element(By.XPATH, "//h1[text()='Python (programming language)']")
