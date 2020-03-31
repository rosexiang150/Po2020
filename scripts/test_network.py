import os, sys
sys.path.append(os.getcwd())

from appium import webdriver
from base.base_driver import BaseDriver
from page.network_page import NetworkPage


class TestNetwork:

    def setup(self):
        basedriver = BaseDriver()
        driver = basedriver.create_driver()
        self.networkpage = NetworkPage(driver)


    def test_net_3G(self):
        self.networkpage.click_3g()


    def test_net_2G(self):
        self.networkpage.click_2g()




