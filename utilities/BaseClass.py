import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    #  define all custom utilities here
    def verify_link_presence(self, link_text):  # this can be called in your test_ using self.verify_link_presence(text)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, link_text)))

    # for radio box or check box with multiple values
    def select_option_by_text(self, locator, text):
        Select(locator).select_by_visible_text(text)

    def get_logger(self):
        loggerName = inspect.stack()[1][3]

        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("logfile_class.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(format)
        logger.addHandler(filehandler)  # complete filehandler object

        logger.setLevel(logging.DEBUG)

        # logger.info("This will also print but at the beginning of the Log. Ex: mostly used for printing information")
        # logger.debug("A debug statement is like the print statement and this prints to a file instead of the console")
        # logger.warning("Warning is an Alert")
        # logger.error("When Assertion fails, you can use this to log a failure")
        # logger.critical("Critical Issue")

        return logger
