from Driver import Driver
from selenium.webdriver.common.by import By


class WelcomeScreen:

    def __init__(self, driver):
        self.driver = driver
        self.englishLanguageBox = self.driver.instance.find_element(By.ID, "js-link-box-en")

    def go_to_home_screen(self):
        self.englishLanguageBox.click()
