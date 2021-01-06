import pytest
import string
import random

from page_objects.login_page import LoginPage
from page_objects.add_customer_page import AddCustomer
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



class Test_003_AddCustomer:
    base_url = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_add_customer(self, setup):
        self.logger.info("***** Test_003_AddCustomer *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("***** Login successful *****")

        self.logger.info("***** Starting Add Customer Test *****")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.click_on_customers_menu()
        self.add_cust.click_on_customers_menu_item()

        self.add_cust.click_on_add_new()

        self.logger.info("***** Providing customer info *****")

        self.email = random_generator() + "@gmail.com"
        self.add_cust.set_email(self.email)
        self.add_cust.set_password("test123")
        self.add_cust.set_customer_roles("Guests")
        self.add_cust.set_manager_of_vendor("Vendor 2")
        self.add_cust.set_gender("Male")
        self.add_cust.set_first_name("Vlad")
        self.add_cust.set_last_name("Nire")
        self.add_cust.set_dob("7/05/1989")  # Format: D / MM / YYYY
        self.add_cust.set_company_name("QA")
        self.add_cust.set_admin_content("This is for testing.")
        self.add_cust.click_on_save()

        self.logger.info("***** Saving customer info *****")

        self.logger.info("***** Add customer validation started *****")

        self.msg = self.driver.find_element_by_tag_name("body").text

        #print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            self.logger.info("***** Add customer Test Passed *****")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_customer_scr.png")
            self.logger.error("***** Add customer Test Failed *****")
            assert False

        self.driver.close()
        self.logger.info("***** Ending Add customer test *****")
