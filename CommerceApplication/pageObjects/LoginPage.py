from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_name = "username"
    textbox_password_name = "password"
    button_login_xpath = "//button[@type = 'submit']"
    image_logoutoption_xpath = "(//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon'])[1]"
    link_logout_linktext = "Logout"


    def __init__(self, driver):
        self.driver = driver


    def setUserName(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)
        # self.driver.find_element_by_name(self.textbox_username_name).clear()
        # self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)



    def setPasword(self, password):
        # self.driver.find_element_by_name(self.textbox_username_name).clear()
        # self.driver.find_element_by_name(self.textbox_username_name).send_keys(password)
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)


    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()





