from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from PageObjects.MakeAPayment import MakeAPayment
from PageObjects.ManagePaymentMethods import ManagePaymentMethods


class AccountSummary(BasePage):

    # locators

    accountnumber = (By.CLASS_NAME, "row-group-value")
    pastdueamt = (By.XPATH, '//*[@id="current-balance"]/div/div/div[1]/dl/dd[2]')
    dueamt = (By.XPATH, '//*[@id="current-balance"]/div/div/div[1]/dl/dd[3]')
    totaldueamt = (By.XPATH, '//*[@id="current-balance"]/div/div/div[1]/dl/dd[4]/b')
    makeapaymentlink = (By.LINK_TEXT, "Make a Payment")
    billspaymenthistorylink = (By.LINK_TEXT, "Bills & Payment History")
    usagehistorylink = (By.LINK_TEXT, "Usage history")
    paymentmethodslink = (By.LINK_TEXT, "Payment Methods")
    automaticpaymentslink = (By.LINK_TEXT, "Automatic Payments")
    poweroutageslink = (By.LINK_TEXT, "Power Outages")
    accountpreferenceslink = (By.LINK_TEXT, "Account Preferences")
    myaccountslink = (By.LINK_TEXT, "My Accounts")
    contactuslink = (By.LINK_TEXT, "Contact Us")
    autopaylink = (By.LINK_TEXT, "Auto Pay")
    paynowbutton = (By.CLASS_NAME, 'btn.btn-md.btn-default')
    manageautopaybutton = (By.CLASS_NAME, 'btn.btn-sm.btn-primary')

    # constructor

    def __init__(self, driver):
        super().__init__(driver)

    # actions

    def get_account_number(self):
        if self.is_visible(self.accountnumber):
            return self.get_element_text(self.accountnumber)
    
    def get_past_due_amount(self):
        if self.is_visible(self.pastdueamt):
            return self.get_element_text(self.pastdueamt)
    
    def get_due_amount(self):
        if self.is_visible(self.dueamt):
            return self.get_element_text(self.dueamt)
        
    def get_total_due_amount(self):
        if self.is_visible(self.totaldueamt):
            return self.get_element_text(self.totaldueamt)

    def click_on_makeapaymentlink(self):
        self.click(self.makeapaymentlink)
        return MakeAPayment(self.driver)

    def click_on_autopaylink(self):
        self.click(self.autopaylink)
        return ManagePaymentMethods(self.driver)

    def click_on_manageautopaybutton(self):
        self.click(self.manageautopaybutton)
        return ManagePaymentMethods(self.driver) 

    def click_on_paynowbutton(self):
        self.click(self.paynowbutton)
        return MakeAPayment(self.driver)

    def page_refresh(self):
        self.refresh()