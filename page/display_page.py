
class DisplayPage:

    def __init__(self, driver):
        self.driver = driver
        print(id(driver))


    def click_search(self):
        ele = self.driver.find_element_by_id('com.android.settings:id/search')
        ele.click()

    def input_text(self, text):
        ele = self.driver.find_element_by_id('android:id/search_src_text')
        ele.click()
        ele.clear()
        ele.send_keys(text)

    def click_back(self):
        self.driver.find_element_by_class_name('android.widget.ImageButton').click()
