from time import sleep
import random
from PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PageObjects.PayByCreditCardFrame import PayByCrediCardFrame


class MakeAPayment(BasePage):

    # locators

    accountnumber = (
        By.XPATH, "//*[@id='MMA_Content']/div[1]/div/div/div/dl/dd[1]/b")
    pastdueamt = ( By.XPATH, '//*[@id="MMA_Content"]/div[1]/div/div/div/dl/dd[2]')
    dueamt = (By.XPATH, '//*[@id="MMA_Content"]/div[1]/div/div/div/dl/dd[3]')
    totaldueamt = (By.XPATH, '//*[@id="MMA_Content"]/div[1]/div/div/div/dl/dd[4]/b')
    paymentmethod = (By.CSS_SELECTOR, "select[name='SelectedPaymentMethod']")
    paymentdt = (By.ID, 'ScheduledDate')
    paymentamount = (By.ID, "AmountToPay")
    cancelbtn = (By.XPATH, '//*[@id="payment-form"]/div[4]/div/div/a')
    continuebtn = (By.ID, "Payment_Create_btn")
    popupmsg = (By.XPATH, '//*[@id="swal2-content"]/p')
    okbtn = (By.CLASS_NAME, "swal2-confirm.swal2-styled")
    confirmationlabel = (
        By.XPATH, '//*[@id="MMA_Content"]/div/div/div[1]/label')
    addpaymethodbtn = (By.CSS_SELECTOR, 'button[data-target="#addPaymentMethodModal"]')
    paymentradiocreditcard = (By.XPATH, '//input[@type="radio" and @value="CC"]')
    addbtn = (By.XPATH, '//button[@onclick="submitPaymentMethod()"]')


    # constructor

    def __init__(self, driver):
        super().__init__(driver)

    # actions

    def get_account_number_makeapayment(self):
        if self.is_visible(self.accountnumber):
            return self.get_element_text(self.accountnumber)
    
    def get_past_due_makeapayment(self):
        if self.is_visible(self.pastdueamt):
            return self.get_element_text(self.pastdueamt)
        
    def get_due_makeapayment(self):
        if self.is_visible(self.dueamt):
            return self.get_element_text(self.dueamt)
        
    def get_total_due_makeapayment(self):
        if self.is_visible(self.totaldueamt):
            return self.get_element_text(self.totaldueamt)
        
    def get_default_date(self):
        if self.is_visible(self.paymentdt):
            return self.get_attribute_value(self.paymentdt,"value")
        
    def get_payment_amount(self):
        if self.is_visible(self.paymentamount):
            return self.get_attribute_value(self.paymentamount,"value")

    def selectpaymentmethod(self, index):
        dropdown = Select(self.driver.find_element(*self.paymentmethod))
        dropdown.select_by_index(index)

    def getselectpaymentmethod(self):
        dropdownlist = self.driver.find_elements(*self.paymentmethod)
        return dropdownlist
        

    def amounttopay(self, amt):
        self.click(self.paymentamount)
        self.clear(self.paymentamount)
        sleep(5)
        self.send_keys(self.paymentamount, amt)

    def cancelbutton(self):
        self.click(self.cancelbtn)

    def continuebutton(self):
        self.click(self.continuebtn)

    def get_pop_up_msg_makeapayment(self):
        if self.is_visible(self.popupmsg):
            return self.get_element_text(self.popupmsg)

    def okbutton(self):
        self.click(self.okbtn)

    def confirmation(self):
        return self.get_element_text(self.confirmationlabel)
    
    def addpaymethod(self):
        self.click(self.addpaymethodbtn)

    def addcreditcard(self):
        self.click(self.paymentradiocreditcard)

    def addbutton(self):
        self.click(self.addbtn)
        return PayByCrediCardFrame(self.driver)

