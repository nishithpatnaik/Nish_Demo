from selenium.webdriver.common.by import By
from pageObjects.Confirmation import Confirmation


class Checkout:
    obj_phone_name = (By.LINK_TEXT, "Blackberry")
    obj_addToCart_button = (By.XPATH, "parent::h4/parent::div/parent::div/div/button")
    obj_checkout_button = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    obj_final_checkout_button = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        return self.driver.find_element(*Checkout.obj_phone_name).find_element(*Checkout.obj_addToCart_button)

    def checkout(self):
        return self.driver.find_element(*Checkout.obj_checkout_button)

    def validate_cart(self):
        return self.driver.find_element(*Checkout.obj_phone_name)

    def final_checkout(self):
        self.driver.find_element(*Checkout.obj_final_checkout_button).click()
        return Confirmation(self.driver)  # creates object for Confirmation Page and returns to the test_
