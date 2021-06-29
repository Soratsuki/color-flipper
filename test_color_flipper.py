import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class Color_Flipper_Tests(unittest.TestCase):

    file_path = os.path.abspath("./index.html")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get(Color_Flipper_Tests.file_path)
        time.sleep(5)

    def test_title(self):
        assert "Color Flipper" in self.driver.title 
        

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()