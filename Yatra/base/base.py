from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 70, ignored_exceptions=[TimeoutException], poll_frequency=2)

    def wait_until_element_is_clickable(self, locator_type, locator):
        return self.wait.until(EC.element_to_be_clickable((locator_type, locator)))

    def wait_until_presence_of_all_elements(self, locator_type, locator):
        return self.wait.until(EC.presence_of_all_elements_located((locator_type, locator)))

    # def wait_for_visibility_of_element(self, locator_type, locator):
    #     return self.wait.until(EC.visibility_of_element_located((locator_type, locator)))



