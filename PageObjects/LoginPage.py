from selenium.webdriver.common.by import By
from PageObjects.AccountSummary import AccountSummary
from PageObjects.BasePage import BasePage


class LoginPage(BasePage):

    # locators
    loginlink = (By.ID, "dnn_dnnLogin_enhancedLoginLink")
    username = (By.NAME, "dnn$ctr1346$Login$Login_DNN$txtUsername")
    password = (By.NAME, "dnn$ctr1346$Login$Login_DNN$txtPassword")
    loginbutton = (By.ID, 'dnn_ctr1346_Login_Login_DNN_cmdLogin')

    # class constructor
    def __init__(self, driver):
        super().__init__(driver)

    # actions

    def click_on_loginlink(self):
        self.click(self.loginlink)

    def login(self, username, password):
        self.send_keys(self.username, username)
        self.send_keys(self.password, password)

    def click_on_loginbutton(self):
        self.click(self.loginbutton)
        return AccountSummary(self.driver)
