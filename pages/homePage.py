class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.myacc_btn_ltxt= "My Account"
        self.register_btn_ltxt="Register"
        self.login_btn_ltxt="Login"

    def click_myacc_btn(self):
        self.driver.find_element_by_link_text(self.myacc_btn_ltxt).click()

    def click_register_btn(self):
        self.driver.find_element_by_link_text(self.register_btn_ltxt).click()

    def click_login(self):
        self.driver.find_element_by_link_text(self.login_btn_ltxt).click()

