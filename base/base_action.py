from selenium.webdriver.common.by import By

class BaseAction:

    def __init__(self, driver):
        self.driver = driver
        print("BaseAction有driver")

    def queryDriver(self, driver):
        self.driver = driver


    def click(self,loc):
        self.find_element(loc).click()

    def input(self, loc, text):
        self.find_element(loc).send_keys(text)

    #自定义查找元素的方法
    def find_element(self, loc):
        return self.driver.find_element(loc[0], loc[1])