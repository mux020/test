from selenium import webdriver
from selenium.webdriver.common.by import By


class homepage:
    def __init__(self,driver):
        self.driver = driver
    shop = (By.LINK_TEXT,"Shop")

    def callit(self):

        return self.driver.find_element(*homepage.shop) # * used for getting the value of tuple