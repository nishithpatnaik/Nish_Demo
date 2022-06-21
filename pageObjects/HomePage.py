from selenium.webdriver.common.by import By

from pageObjects.Checkout import Checkout


class HomePage:

    # Constructor for driver object
    def __init__(self, driver):
        self.driver = driver

    # define all objects under Home Page
    obj_shop_link = (By.LINK_TEXT, "Shop")
    obj_name_txt = (By.NAME, "name")
    obj_email_txt = (By.NAME, "email")
    obj_password_txt = (By.ID, "exampleInputPassword1")
    obj_ice_chkbox = (By.ID, "exampleCheck1")
    obj_gender_drpdwn = (By.ID, "exampleFormControlSelect1")
    obj_empstatus_radio = (By.NAME, "inlineRadioOptions")
    obj_dob_calendar = (By.NAME, "bday")
    obj_submit_button = (By.XPATH, "//input[@value='Submit']")
    obj_success_label = (By.CSS_SELECTOR, "[class*='alert-success']")

    # define Methods for appending driver.find_elements(for each defined object)
    def shop_link(self):
        self.driver.find_element(*HomePage.obj_shop_link).click()
        #  The above click takes you to Checkout Page. Therefore create Checkout page object and return
        return Checkout(self.driver)

    def enter_name(self):
        return self.driver.find_element(*HomePage.obj_name_txt)

    def enter_email(self):
        return self.driver.find_element(*HomePage.obj_email_txt)

    def enter_password(self):
        return self.driver.find_element(*HomePage.obj_password_txt)

    def select_icecream_checkbox(self):
        return self.driver.find_element(*HomePage.obj_ice_chkbox)

    def select_gender(self):
        return self.driver.find_element(*HomePage.obj_gender_drpdwn)

    def select_emp_status(self):
        return self.driver.find_element(*HomePage.obj_empstatus_radio)

    def enter_dob(self):
        return self.driver.find_element(*HomePage.obj_dob_calendar)

    def click_submit(self):
        return self.driver.find_element(*HomePage.obj_submit_button)

    def validate_success_label(self):
        return self.driver.find_element(*HomePage.obj_success_label)

