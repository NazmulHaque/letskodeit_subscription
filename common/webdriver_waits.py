from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverWaits(object):

    def __init__(self, driver, timeout=30):
        self.driver_wait = WebDriverWait(driver, timeout)

    def wait_till_element_visible(self, element_locator, error_msg=None):
        if error_msg is None:
            error_msg = 'Desired element is not visible on time'

        self.driver_wait.until(EC.visibility_of_element_located(element_locator), error_msg)

    def wait_till_element_is_invisible(self, element_locator, error_msg=None):
        if error_msg is None:
            error_msg = 'Desired element did not invisible on time'

        self.driver_wait.until(EC.invisibility_of_element_located(element_locator), error_msg)
