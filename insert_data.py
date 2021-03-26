# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from create_driver import SeleniumLibraryExt
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

# from robot.libraries.BuiltIn import BuiltIn

class InsertData:

    # def __init__(self):
        # self.driver = SeleniumLibraryExt.create_driver()

    @classmethod
    def setup(cls):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome('./chromedriver', options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get('https://demoqa.com/text-box')
        return cls.driver

    def insert_full_name(self, full_name=None):
        text_box = self.driver.find_element_by_id("userName")
        text_box.clear()
        text_box.send_keys(full_name)

    def insert_email(self, email=None):
        text_box = self.driver.find_element_by_id("userEmail")
        text_box.clear()
        text_box.send_keys(email)

    def insert_current_address(self, current_address=None):
        text_box = self.driver.find_element_by_id("currentAddress")
        text_box.clear()
        text_box.send_keys(current_address)

    def insert_permanent_address(self, permanent_address=None):
        text_box = self.driver.find_element_by_id("permanentAddress")
        text_box.clear()
        text_box.send_keys(permanent_address)

    def retrieve_text_boxes(self):
        label_dict = dict()
        form = self.driver.find_element_by_xpath("//form[@id='userForm']")
        labels = form.find_elements_by_xpath("div")
        for elem in labels:
            print(elem.get_attribute('id'))

InsertData.setup()
a = InsertData()
a.retrieve_text_boxes()





