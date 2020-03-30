from appium import webdriver

class TestDisplay:

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

    def test_search(self):
        self.driver.find_element_by_id('com.android.settings:id/search').click()
        ele = self.driver.find_element_by_id('android:id/search_src_text')
        ele.click()
        ele.clear()
        ele.send_keys('s')
        self.driver.find_element_by_class_name('android.widget.ImageButton').click()


