class LoginPage():

    def __init__(self, driver):
        self.driver= driver

        self.email_txt_id="input-email"
        self.pwd_txt_id="input-password"
        self.login_btn_xp="//*[@id='content']/div/div[2]/div/form/input"

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_txt_id).clear()
        self.driver.find_element_by_id(self.email_txt_id).send_keys(email)

    def enter_pwd(self, pwd):
        self.driver.find_element_by_id(self.pwd_txt_id).clear()
        self.driver.find_element_by_id(self.pwd_txt_id).send_keys(pwd)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_btn_xp).click()


