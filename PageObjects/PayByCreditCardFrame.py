from time import sleep
import random
from PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PayByCrediCardFrame(BasePage):

    # locators

    frame = 'iFrameCC'  
    cardnumber = (By.ID, 'paymentNumber')
    cvv = (By.ID, 'paymentCVC')
    expmonth = (By.ID, 'paymentExpiryMonth')
    expyear = (By.ID,'paymentExpiryYear')
    sandbox = (By.ID, 'cbxAuthorization')
    contbtn = (By.ID, 'btnSaveCard')


    # constructor

    def __init__(self, driver):
        super().__init__(driver)

    # actions

    def switchframe(self):
        self.switch(self.frame)

    def entercreditcardnumber(self, number):
        self.send_keys(self.cardnumber, number)

    def entercvv(self, number):
        self.send_keys(self.cvv, number)

    def enterexpirymonth(self, number):
        self.send_keys(self.expmonth, number)

    def enterexpiryyear(self, number):
        self.send_keys(self.expyear, number)

    def checkauthorization(self):
        self.click(self.sandbox)

    def continuebutton(self):
        self.click(self.contbtn)
    


