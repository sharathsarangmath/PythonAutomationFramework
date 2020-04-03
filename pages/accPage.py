class AccountPage():

    def __init__(self,driver):
        self.driver = driver

        self.cntn_btn_ltxt="Continue"
        self.logout_btn_ltxt="Logout"

    def click_continue(self):
        self.driver.find_element_by_link_text(self.cntn_btn_ltxt).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_btn_ltxt).click()
