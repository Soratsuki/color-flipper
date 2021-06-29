import unittest
from selenium import webdriver

class Color_Flipper_Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("index.html")

    def test_title(self):
        assert self.driver.title == "Color Flipper"

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()