import pytest
import unittest
# import allure
from pageobjects.homescreen import HomeScreen
from pageobjects.resultscreen import ResultScreen
from pageobjects.welcomescreen import WelcomeScreen
from driver import Driver


class TestWikipedia(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    # @allure.testcase('Test Search Results of Wikipedia')
    def test_search_for_result(self):
        # with pytest.allure.step('step one'):
        welcome_screen = WelcomeScreen(self.driver)
        welcome_screen.go_to_home_screen()

        # with pytest.allure.step('step two'):
        home_screen = HomeScreen(self.driver)
        home_screen.search_for_results("Python")
        home_screen.click_desired_result("Python (programming language)")

        # with pytest.allure.step('step three'):
        result_screen = ResultScreen(self.driver)
        assert result_screen.articleHeader.text == "Python (programming language)"


if __name__ == '__main__':
    unittest.main()
