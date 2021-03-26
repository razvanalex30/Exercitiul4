from create_driver import create_driver


class VerifyData:



    # def find_output(self):
    #     output = self.driver.find_element_by_xpath("//*[@id='output']/div")
    #     output_elements = output.find_element_by_tag_name("p")

    def __init__(self):
        self.driver = create_driver()

    def find_name(self):
        output_name = self.driver.find_element_by_xpath("//*[@id='output']/div//p[@id='name']")
        name = output_name.text
        if name != "":
            return True

    def find_email(self):
        output_email = self.driver.find_element_by_xpath("//*[@id='output']/div//p[@id='email']")
        email = output_email.text
        if email != "":
            return True

    def find_current_address(self):
        output_current_address = self.driver.find_element_by_xpath("//*[@id='output']/div//p[@id='currentAddress']")
        current_address = output_current_address.text
        if current_address != "":
            return True

    def find_permanent_address(self):
        output_permanent_address = self.driver.find_element_by_xpath("//*[@id='output']/div//p[@id='permanentAddress']")
        permanent_address = output_permanent_address.text
        if permanent_address != "":
            return True
