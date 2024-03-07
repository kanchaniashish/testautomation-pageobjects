from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))
        return element.text
    
    def get_attribute_value(self, by_locator,value):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))
        return element.get_attribute(value)

    def is_enalbled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))
        return bool(element)

    def not_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(by_locator))
        return bool(element)

    def clear(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(by_locator)).clear()
        
    def switch(self, by_name):
        self.driver.switch_to.frame(by_name)

    def refresh(self):
        self.driver.refresh()

        
