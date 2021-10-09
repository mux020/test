from selenium.webdriver.common.by import By

from purchase import purchase


class buy:

    def __init__(self,driver):
        self.driver=driver

    quantity = (By.ID,"exampleInputEmail1")
    asscheckprod= (By.XPATH,"//h4[@class='media-heading']/a")
    pricecheck=(By.XPATH,"//tr/td[4]/strong")
    checkoutb=(By.CSS_SELECTOR,".btn-success")

    def buyprod(self):
        return self.driver.find_element(*buy.quantity)
    def asscheck(self):
        return self.driver.find_element(*buy.asscheckprod)
    def cprice(self):
        return self.driver.find_element(*buy.pricecheck)
    def checkout(self):
        self.driver.find_element(*buy.checkoutb).click()
        purchaseprod = purchase(self.driver)
        return purchaseprod

    def newmeth(self):
        print("new meth added")
        print("addne new comment ")

        print("changes made")
print("added to staging branch")