import os, sys
sys.path.append(os.getcwd())

from appium import webdriver
from base.base_driver import BaseDriver


class TestDisplay:

    def setup(self):
        baseDriver = BaseDriver()
        self.driver = baseDriver.init_driver()

    def test_search(self):
        self.driver.find_element_by_id('com.android.settings:id/search').click()
        ele = self.driver.find_element_by_id('android:id/search_src_text')
        ele.click()
        ele.clear()
        ele.send_keys('s')
        self.driver.find_element_by_class_name('android.widget.ImageButton').click()
