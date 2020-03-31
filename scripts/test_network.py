import os, sys
sys.path.append(os.getcwd())

from appium import webdriver
from base.base_driver import BaseDriver


class TestNetwork:

    def setup(self):
        basedriver = BaseDriver()
        self.driver = basedriver.init_driver()


    def test_net_3G(self):
        self.driver.find_element_by_xpath('//*[@text="更多"]').click()
        self.driver.find_element_by_xpath('//*[@text="移动网络"]').click()
        list1 = self.driver.find_elements_by_id('android:id/title')
        for i in list1:
            if i.get_attribute('text') == "首选网络类型":
                i.click()
                break
        self.driver.find_element_by_xpath('//*[@text="3G"]').click()

    def test_net_2G(self):
        self.driver.find_element_by_xpath('//*[@text="更多"]').click()
        self.driver.find_element_by_xpath('//*[@text="移动网络"]').click()
        list1 = self.driver.find_elements_by_id('android:id/title')
        for i in list1:
            if i.get_attribute('text') == "首选网络类型":
                i.click()
                break
        self.driver.find_element_by_xpath('//*[@text="2G"]').click()








