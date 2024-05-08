from selenium import webdriver

import pytest

from selenium import *
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup

class Test_01_Login:
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"


    def test_homePageTitle(self, setup):
        self.driver = webdriver.Chrome()
        # self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        expected_title = "OrangeHRMc"
        self.driver.close()
        if actual_title == expected_title:
            assert True
        else:
            self.driver.save_screenshot(".Screenshots/test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPasword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "OrangeHRM":
            assert True
        else:
            assert False






