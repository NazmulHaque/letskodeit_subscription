import unittest

import settings
from selenium import webdriver
from pages.home.actions import HomePageActions


class FunctionalTest(unittest.TestCase):
    driver = None
    login_required = False

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.home_page = HomePageActions(cls.driver)

        cls.driver.get(settings.BASE_URL)

        if cls.home_page.is_friday_sale_popup_appeared():
            cls.home_page.dismiss_friday_sale_popup()


        # if cls.login_required:
        #     # do login

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()