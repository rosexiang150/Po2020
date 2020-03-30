from appium import webdriver

class TestNetwork:

    def setup(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 解决输入中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        # 声明我们的driver对象
        self.driver =  webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

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




