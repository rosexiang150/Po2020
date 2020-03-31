from selenium.webdriver.common.by import By

class NetworkPage:

    more_button = By.XPATH, '//*[@text="更多"]'
    network_button = By.XPATH, '//*[@text="移动网络"]'
    net2G_button = By.XPATH, '//*[@text="2G"]'
    net3G_button = By.XPATH, '//*[@text="3G"]'
    firstNet_button = By.ID, 'android:id/title'


    def __init__(self, driver):
        self.driver = driver

    def click_3g(self):
        # self.driver.find_element_by_xpath('//*[@text="更多"]').click()
        self.find_element(self.more_button).click()
        # self.driver.find_element_by_xpath('//*[@text="移动网络"]').click()
        self.find_element(self.network_button).click()
        list1 = self.find_elements(self.firstNet_button)
        for i in list1:
            if i.get_attribute('text') == "首选网络类型":
                i.click()
                break
        self.find_element(self.net3G_button).click()


    def click_2g(self):
        # self.driver.find_element_by_xpath('//*[@text="更多"]').click()
        self.find_element(self.more_button).click()
        # self.driver.find_element_by_xpath('//*[@text="移动网络"]').click()
        self.find_element(self.network_button).click()
        # list1 = self.driver.find_elements_by_id('android:id/title')
        list1 = self.find_elements(self.firstNet_button)
        for i in list1:
            if i.get_attribute('text') == "首选网络类型":
                i.click()
                break
        # self.driver.find_element_by_xpath('//*[@text="2G"]').click()
        self.find_element(self.net2G_button).click()

    def find_element(self, loc):
        return self.driver.find_element(loc[0], loc[1])

    def find_elements(self, loc):
        return self.driver.find_elements(loc[0], loc[1])
