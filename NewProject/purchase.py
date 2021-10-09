from selenium.webdriver.common.by import By


class purchase:
    def __init__(self,driver):
        self.driver=driver
    listse= (By.XPATH,"//div[@class='suggestions']/ul/li/a")
    country =(By.ID,"country")
    accept = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    purchasebutt= (By.XPATH,"//input[@type='submit']")
    success=(By.CLASS_NAME,"alert-success")

    def listloc(self):
        return self.driver.find_elements(*purchase.listse)

    def countryselect(self):
        return self.driver.find_element(*purchase.country)
    def accepttandc(self):
        return self.driver.find_element(*purchase.accept)

    def clickpurchase(self):
        return self.driver.find_element(*purchase.purchasebutt)
    def successalert(self):
        return self.driver.find_element(*purchase.success)
