import pytest
from selenium import webdriver


#  This function is used to parameterize Browser from the CMD
def pytest_addoption(parser):

    # --browser_name is a variable and must match CMD variable name
    parser.addoption("--browser_name", action="store", default="chrome")
    # CMD command --> py.test --browser_name chrome/firefox/IE


@pytest.fixture(scope="class")
def setup(request):

    #  retrieve the browser_name passed from the CMD in a variable

    browser = request.config.getoption("browser_name")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser == "IE":
        driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

