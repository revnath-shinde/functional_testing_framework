import logging
import time

import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import setup_logging
from utilities import XLUtils
logger = setup_logging()
logger.info("Logger object created successfully..")

class Test_002_DDT_login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger=setup_logging()

    def test_login_ddt(self, setup):
        self.logger.info("****** Test_002_DDT_login *******")
        self.logger.info("****** Verify Login DDT Test *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows=XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows i a Excel:",self.rows)
        lst_status=[]
        for r in range(2, self.rows+1):
            self.user=XLUtils.readData(self.path,"Sheet1", r, 1)
            self.password = XLUtils.readData(self.path,'Sheet1', r,2 )
            self.exp=XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("**** Passed ****")
                    self.lp.clickLogout();
                    lst_status.append("pass")
                elif self.exp=="Fail":
                    self.logger.info("**** Failed****")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp=='pass':
                    self.logger.info("***** Failed****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**** passed ****")
                    lst_status.append("pass")

        if "Fail " not in lst_status:
           self.logger.info("*****Login DDT test passed******")
           self.driver.close()
        else:
           self.logger.info("*****Login DDT test failed ******")
           self.driver.close()
           assert False
        self.logger.info("****** End of Login DDT Test *******")
        self.logger.info("****** Completed TC_LoginDDT_002 *******");











