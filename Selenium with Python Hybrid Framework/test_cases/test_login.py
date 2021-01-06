import pytest

from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class Test_001_Login:
    base_url = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_home_page_title(self, setup):
        self.logger.info("***** Test_001_Login *****")
        self.logger.info("***** Verifying Home Page Title *****")
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            self.driver.close()
            self.logger.info("***** Home Page Title Passed *****")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_home_page_title.png")
            self.driver.close()
            self.logger.error("***** Home Page Title Failed *****")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***** Test_002_Login *****")
        self.logger.info("***** Verifying Login *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("***** Login Passed *****")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.logger.error("***** Login Failed *****")
            self.driver.close()
            assert False
