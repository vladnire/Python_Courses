import time
import pytest

from page_objects.login_page import LoginPage
from page_objects.add_customer_page import AddCustomer
from page_objects.search_customer_page import SearchCustomer
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):
        self.logger.info("***** SearchCustomerByName_005 *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("***** Login successful *****")

        self.logger.info("***** Starting Search Customer By Name *****")

        self.add_cst = AddCustomer(self.driver)
        self.add_cst.click_on_customers_menu()
        self.add_cst.click_on_customers_menu_item()

        self.logger.info("***** searching customer by name *****")
        search_cst = SearchCustomer(self.driver)
        search_cst.set_first_name("Victoria")
        search_cst.set_last_name("Terces")
        search_cst.click_search()

        time.sleep(5)
        status = search_cst.search_customer_by_name("Victoria Terces")
        self.driver.close()
        self.logger.info("*****  TC_SearchCustomerByName_005 Finished  *****")
        assert status is True
