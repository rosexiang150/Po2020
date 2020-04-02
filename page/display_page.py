from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class DisplayPage(BaseAction):

    search_button = By.ID, 'com.android.settings:id/search'
    input_text_view = By.ID, 'android:id/search_src_text'
    back_button = By.CLASS_NAME, 'android.widget.ImageButton'

    def __init__(self, driver):
        BaseAction.__init__(self,driver)

    def click_search(self):
        # ele = self.find_element(self.search_button)
        # ele.click()
        self.click(self.search_button)

    def input_text(self, text):
        # ele = self.find_element(self.input_text_view)
        # ele.click()
        # ele.clear()
        # ele.send_keys(text)
        self.click(self.input_text_view)


    def click_back(self):
        # self.find_element(self.back_button).click()
        self.click(self.back_button)



