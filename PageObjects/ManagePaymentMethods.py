from PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By
from PageObjects.MakeAPayment import MakeAPayment
from selenium.webdriver.support.ui import Select


class ManagePaymentMethods(BasePage):

    # locators

    authcheckbox = (By.ID, "CheckAgreeTerms")
    mpm_continue = (By.ID, "ContinueButton")
    mpm_cancel = (By.CLASS_NAME, 'btn.btn-default')
    mpm_paymentmethod = (By.CSS_SELECTOR, "select[name='SelectedPaymentMethod']")
    paylaterbutton = (By.XPATH, '//*[@id="modalAutopayRequest"]/div/div/div[3]/button')
    stoppymt = (By.XPATH, '//*[@id="automatic-payments"]/div/div/div[4]/div/a')
  

    # constructor

    def __init__(self, driver):
        super().__init__(driver)

    # actions

    def click_agreeterms(self):
        self.click(self.authcheckbox)

    def click_on_continuebutton(self):
        self.click(self.mpm_continue)

    def click_on_cancelbutton(self):
        self.click(self.mpm_cancel)

    def selectpaymentmethod(self, index):
        dropdown = Select(self.driver.find_element(*self.mpm_paymentmethod))
        dropdown.select_by_index(index)

    def click_on_paylaterbutton(self):
        self.click(self.paylaterbutton)
    
    def click_on_stoppaybutton(self):
        self.click(self.stoppymt)
        
        
      


