from selenium.webdriver.common.by import By

from NewProject.buy import buy


class selectproduct:
    def __init__(self,driver):
        self.driver=driver
    getlis = (By.CSS_SELECTOR,".card-title a")
    button = (By.CSS_SELECTOR, ".btn-info")
    checkout =(By.XPATH,"//a[@class='nav-link btn btn-primary']")
    def selectpro(self):
        return self.driver.find_elements(*selectproduct.getlis)

    '''def pro(self):
        return self.driver.find_element(*selectproduct.getpro)'''
    def buttons(self):
        return self.driver.find_elements(*selectproduct.button)
    def check(self):
        self.driver.find_element(*selectproduct.checkout).click()
        buypage = buy(self.driver)
        return buypage

#find_element_by_xpath("div/button")


'''li = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for i in li:
            if i.find_element_by_xpath("div/h4/a").text == "Blackberry":
                i.find_element_by_xpath("div/button").click()
                break'''