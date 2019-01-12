from pages.home.locators import HomePageLocators
from common.webdriver_waits import DriverWaits


class HomePageActions(object):

    def __init__(self, driver):
        self.driver = driver
        self.waits = DriverWaits(self.driver, timeout=10)

    def is_friday_sale_popup_appeared(self):

        try:
            self.waits.wait_till_element_visible(HomePageLocators.FRIDAY_SALE_POPUP)
        except:
            return False
        else:
            return True

    def dismiss_friday_sale_popup(self):
        self.driver.find_element(*HomePageLocators.FRIDAY_SALE_POPUP_CLOSE_BUTTON).click()

        self.waits.wait_till_element_is_invisible(HomePageLocators.FRIDAY_SALE_POPUP)
