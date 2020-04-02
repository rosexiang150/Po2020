import os, sys
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class NetworkPage(BaseAction):

    more_button = By.XPATH, '//*[@text="更多"]'
    network_button = By.XPATH, '//*[@text="移动网络"]'
    net2G_button = By.XPATH, '//*[@text="2G"]'
    net3G_button = By.XPATH, '//*[@text="3G"]'
    firstNet_button = By.ID, 'android:id/title'

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def click_3g(self):
        self.click(self.more_button)
        self.click(self.network_button)

        ele1 = self.custom_find_ele_ById_And_content(self.firstNet_button,"首选网络类型")
        ele1.click()

        self.click(self.net3G_button)

    def click_2g(self):
        self.click(self.more_button)
        self.click(self.network_button)
        ele1 = self.custom_find_ele_ById_And_content(self.firstNet_button, "首选网络类型")
        ele1.click()
        # self.find_element(self.net2G_button).click()
        self.click(self.net2G_button)
