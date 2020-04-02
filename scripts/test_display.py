import os, sys
sys.path.append(os.getcwd())

from base.base_driver import BaseDriver
from page.display_page import DisplayPage


class TestDisplay:

    def setup(self):
        baseDriver = BaseDriver()
        driver = baseDriver.init_driver()
        self.display = DisplayPage(driver)

    def test_search(self):
        self.display.click_search()
        self.display.input_text('s')
        self.display.click_back()


