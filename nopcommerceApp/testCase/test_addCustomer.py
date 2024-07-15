import logging
import time

import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import setup_logging
from pageObject.AddCustomerPage import AddCustomer

logger = setup_logging()
logger.info("Logger object created successfully..")



class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_AddCustomer(self, setup):
        # self.logger.  info("***********Test_003_AddCustomer*************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # self.logger.info("**********Login Succesful************")

        self.addcust=AddCustomer(self.driver)
        time.sleep(5)
        self.addcust.clickonCustomerMenu()
        time.sleep(5)
        self.addcust.clickonExportbtn()
        time.sleep(3)
        self.addcust.clickonCustomerItemMenu()
        time.sleep(5)
        self.addcust.clickAddnew()
        self.logger.info("**********providing customer info **********")