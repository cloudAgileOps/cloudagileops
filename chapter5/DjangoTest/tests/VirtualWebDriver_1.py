from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class VirtualWebDriver(object):

    def __init__(self):

        pass

    @classmethod
    def getDriver(cls):
        selfobj = cls()
        if os.environ.has_key("WEBDRIVER"):
            if os.environ["WEBDRIVER"] == "Chrome":
                chromeOptions = webdriver.ChromeOptions()
                chromeOptions.set_headless()
                selfobj.driver = webdriver.Chrome(chrome_options=chromeOptions)
            if os.environ["WEBDRIVER"] == "Firefox":
                firefoxOptions = FirefoxOptions();
                firefoxOptions.set_headless(true)
 
                selfobj.driver = webdriver.Firefox(firefox_opotions=firefoxOptions)
        else:
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.set_headless()
            selfobj.driver = webdriver.Chrome(chrome_options=chromeOptions)

        return selfobj 
     
    def get(self, url):
        return self.driver.get(url)
    
    def find_element_by_id(self, id):
        return self.driver.find_element_by_id(id)


    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def find_element_by_link_text(self, text):
        return self.driver.find_element_by_link_text(text)

    def set_window_size(self, width, hight):
        self.driver.set_window_size(width, hight)

    def implicitly_wait(self, second):
        self.driver.implicitly_wait(second)

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    driver = VirtualWebDriver.getDriver().find_elements_by_id("test is test")
    

