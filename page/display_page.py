from selenium.webdriver.common.by import By

class DisplayPage:

    search_button = By.ID, 'com.android.settings:id/search'
    input_text_view = By.ID, 'android:id/search_src_text'
    back_button = By.CLASS_NAME, 'android.widget.ImageButton'


    def find_element(self, loc):
        return self.driver.find_element(loc[0], loc[1])

    def __init__(self, driver):
        self.driver = driver
        print(id(driver))


    def click_search(self):
        ele = self.find_element(self.search_button)
        ele.click()

    def input_text(self, text):
        ele = self.find_element(self.input_text_view)
        ele.click()
        ele.clear()
        ele.send_keys(text)

    def click_back(self):
        self.find_element(self.back_button).click()



