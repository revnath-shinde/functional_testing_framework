import logging
import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import setup_logging
from selenium.webdriver.chrome.service import Service

logger = setup_logging()
logger.info("Logger object created successfully..")
class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()


    def test_homePageTitle(self, setup):
        # self.logger.info("****** Test_001_login *******")
        # self.logger.info("****** Verify Home Page Title *******")
        # logger.info("****** Verify Home Page Title *******")
        self.driver = setup
        self.driver.get(self.baseURL)

        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            # self.logger.info("****** Home page title is passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            # self.logger.error("****** Home Page title is failed *******")
            assert False

    def test_login(self, setup):

        # self.logger.info("****** Verify login test *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            # self.logger.info("******** Login test is passed *******")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            # self.logger.error("****** Login test is failed *******")
            assert False




