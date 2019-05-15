class signin():

    def __init__(self,driver):

        self.driver = driver
        self.signin_button_xpath = "// a[contains(text(), 'Sign in')]"
        self.ebaydeals_link_xpath = "//a[@class='gh-p']"
        self.item_link_xpath = "//span[@class='ebayui-ellipsis-3']"
        self.addtocart_link_xpath= "// a[ @ id = 'isCartBtn_btn']"
        self.nothanks_button_xpath = "// button[contains(text(), 'No thanks')]"
        self.name_link_xpath ="//b[@class='gh-eb-arw gh-sprRetina']"
        self.signout_link_xpath = "//a[contains(text(),'Sign out')]"


    def click_signin(self):
        self.driver.find_element_by_xpath(self.signin_button_xpath).click()

    def add_cartitems(self):
        self.driver.find_element_by_xpath(self.ebaydeals_link_xpath).click()
        self.driver.find_element_by_xpath(self.item_link_xpath).click()
        self.driver.find_element_by_xpath(self.addtocart_link_xpath).click()
        self.driver.find_element_by_xpath(self.nothanks_button_xpath).click()

    def click_signout(self):
        self.driver.find_element_by_xpath(self.name_link_xpath).click()
        self.driver.find_element_by_xpath(self.signout_link_xpath).click()


