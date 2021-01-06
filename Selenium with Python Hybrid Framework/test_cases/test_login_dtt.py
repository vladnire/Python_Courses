import time
import pytest

from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities import excel_utils


class Test_002_DTT_Login:
    base_url = ReadConfig.get_app_url()
    path = ".\\test_data\\login_data.xlsx"
    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_login_dtt(self, setup):
        self.logger.info("***** Test_002_DTT_Login *****")
        self.logger.info("***** Verifying Login DTT *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)

        # Get data from excel file
        self.rows = excel_utils.get_row_count(self.path, 'Sheet1')
        print(f"Number of rows in Excel: {self.rows}")

        status_list = []

        for r in range(2, self.rows + 1):
            self.username = excel_utils.read_data(self.path, 'Sheet1', r, 1)
            self.password = excel_utils.read_data(self.path, 'Sheet1', r, 2)
            self.expected = excel_utils.read_data(self.path, 'Sheet1', r, 3)

            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)

            actual_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if actual_title == exp_title:
                if self.expected == "Passed":
                    self.logger.info("***** Test Passed *****")
                    status_list.append("Passed")
                elif self.expected == "Failed":
                    self.logger.info("***** Test Failed *****")
                    status_list.append("Failed")
                self.lp.click_logout()
            elif actual_title != exp_title:
                if self.expected == "Passed":
                    self.logger.info("***** Test Failed *****")
                    status_list.append("Failed")
                elif self.expected == "Failed":
                    self.logger.info("***** Test Passed *****")
                    status_list.append("Passed")

        if "Failed" in status_list:
            self.logger.info("***** Login DTT Failed *****")
            self.driver.close()
            assert False
        else:
            self.logger.info("***** Login DTT Passed *****")
            self.driver.close()
            assert True

        self.logger.info("***** End of Login DTT Test *****")
