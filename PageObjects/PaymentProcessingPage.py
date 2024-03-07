from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from PageObjects.MakeAPayment import MakeAPayment


class PaymentProcessingPage(BasePage):

    # locators

    backbtn = (By.ID, 'btnReturn')


    # constructor

    def __init__(self, driver):
        super().__init__(driver)

    # actions

    def backbutton(self):
        self.click(self.backbtn)
        return MakeAPayment(self.driver)
