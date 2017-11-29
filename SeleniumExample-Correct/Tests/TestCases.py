import unittest
from PageObjects.HomeScreen import HomeScreen
from PageObjects.ResultScreen import ResultScreen
from PageObjects.WelcomeScreen import WelcomeScreen
from Driver import Driver


class TestWikipedia(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_search_for_result(self):
        welcomeScreen = WelcomeScreen(self.driver)
        welcomeScreen.go_to_home_screen()

        homeScreen = HomeScreen(self.driver)
        homeScreen.search_for_results("Python")
        homeScreen.click_desired_result("Python (programming language)")

        resultScreen = ResultScreen(self.driver)
        assert resultScreen.articleHeader.text == "Python (programming language)"


if __name__ == '__main__':
    unittest.main()
