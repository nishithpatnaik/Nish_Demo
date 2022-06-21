import time
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestWorkflow(BaseClass):

    def test_workflow1(self):
        print("Git Demo")

        log = self.get_logger()

        # Create object for each pageObject
        home_page = HomePage(self.driver)
        # checkout_page = Checkout(self.driver)
        # confirmation_page = Confirmation(self.driver)
        self.driver.implicitly_wait(1)
        # Click on Shop link and return next page (checkout Page object)
        checkout_page = home_page.shop_link()
        # self.driver.find_element(by=By.LINK_TEXT, value="Shop").click()

        # Click on Add to Cart for Blackberry phone
        log.info("Adding Blackberry Phone to Cart")
        checkout_page.add_to_cart().click()
        # Traversing parent and child elements to find the Add button
        # self.driver.find_element_by_link_text("Blackberry").find_element_by_xpath(
        #   "parent::h4/parent::div/parent::div/div/button").click()

        # Click on the Checkout button
        # self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
        checkout_page.checkout().click()

        # Validate Cart
        assert "Blackberry" == checkout_page.validate_cart().text
        # assert "Blackberry" == self.driver.find_element_by_link_text("Blackberry").text

        time.sleep(2)
        # Click on Checkout button
        # self.driver.find_element_by_css_selector("button[class='btn btn-success']").click()
        confirmation_page = checkout_page.final_checkout()

        #  Enter country code
        confirmation_page.country().click()
        log.info("Entering Country Name as India")
        confirmation_page.country().send_keys("Ind")
        # self.driver.find_element_by_id("country").send_keys("Ind")
        # wait = WebDriverWait(driver, 5)
        # wait.until(expected_conditions.presence_of_element_located())
        # time.sleep(4)
        # Verify presence of India. This function is being called from the BaseClass
        self.verify_link_presence("India")
        # countries = self.driver.find_elements_by_css_selector("div[class='suggestions'] a")
        countries = confirmation_page.country_list()

        for country in countries:
            if country.text == "India":
                country.click()
                break

        # Click on I agree checkbox
        # self.driver.find_element_by_xpath("//label[@for='checkbox2']").click()
        confirmation_page.i_agree_checkbox().click()

        time.sleep(2)
        # Click on Purchase Button
        # self.driver.find_element_by_css_selector("input[class='btn btn-success btn-lg']").click()
        confirmation_page.purchase_button().click()

        time.sleep(2)
        # Validate Success Message
        # assert "Success! Thank you!" in self.driver.find_element_by_class_name("alert-success").text
        assert "Success! Thank you!" in confirmation_page.successful_purchase().text
        log.info("Successful Purchase")
