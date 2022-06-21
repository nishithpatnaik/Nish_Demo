import pytest

from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from testdata.HomePage_data import HomePageData


class TestHomePage(BaseClass):

    def test_homepage_form_submit(self, get_data):
        log = self.get_logger()
        log.info("Enter HomePage Form Details for: "+get_data["Name"])
        homepage = HomePage(self.driver)
        homepage.enter_name().send_keys(get_data["Name"])
        homepage.enter_email().send_keys(get_data["Email"])
        homepage.enter_password().send_keys(get_data["Password"])
        homepage.select_icecream_checkbox().click()
        # gender = Select(homepage.select_gender())
        # gender.select_by_visible_text("Female")
        # Below we created a dynamic select where we are passing a locator object and value to select from
        self.select_option_by_text(homepage.select_gender(), get_data["Gender"])
        # homepage.select_emp_status()
        # homepage.enter_dob("")
        homepage.click_submit().click()
        assert "Success!" in homepage.validate_success_label().text

        self.driver.refresh()  # to refresh the browser since submit doesnt clear the form

    # Parameterize form
    # @pytest.fixture(
    #     params=[{"Name": "Nishith Patnaik", "Email": "nishith@gmail.com", "Password": "ohno-ohno", "Gender": "Male"},
    #          {"Name": "Cristiano Ronaldo", "Email": "CR7@gmail.com", "Password": "ohyes-ohyes", "Gender": "Female"}])
    @pytest.fixture(params=HomePageData.get_excel_data())  # data is being stored in under another class variable
    def get_data(self, request):
        return request.param
 