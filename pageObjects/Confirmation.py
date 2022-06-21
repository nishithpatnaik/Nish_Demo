from selenium.webdriver.common.by import By


class Confirmation:
    obj_country = (By.ID, "country")
    obj_country_list = (By.CSS_SELECTOR, "div[class='suggestions'] a")
    obj_agree_checkbox = (By.XPATH, "//label[@for='checkbox2']")
    obj_purchase_button = (By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']")
    obj_success_label = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def country(self):
        return self.driver.find_element(*Confirmation.obj_country)

    def country_list(self):
        return self.driver.find_elements(*Confirmation.obj_country_list)

    def i_agree_checkbox(self):
        return self.driver.find_element(*Confirmation.obj_agree_checkbox)

    def purchase_button(self):
        return self.driver.find_element(*Confirmation.obj_purchase_button)

    def successful_purchase(self):
        return self.driver.find_element(*Confirmation.obj_success_label)
