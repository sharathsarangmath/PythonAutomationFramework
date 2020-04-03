class RegisterPage():

    def __init__(self, driver):
        self.driver=driver

        self.firstname_txt_id="input-firstname"
        self.lastname_txt_id="input-lastname"
        self.email_txt_id="input-email"
        self.phone_txt_id="input-telephone"
        self.password_txt_id="input-password"
        self.confirm_txt_id="input-confirm"
        self.newsltr_rdbtn_xp="//label[2]/input[@name='newsletter']"
        self.agree_chkbx_xp="//input[@name='agree']"
        self.cntn_btn_xp="//input[@class='btn btn-primary']"

    def enter_firstname(self, firstname):
        self.driver.find_element_by_id(self.firstname_txt_id).clear()
        self.driver.find_element_by_id(self.firstname_txt_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_id(self.lastname_txt_id).clear()
        self.driver.find_element_by_id(self.lastname_txt_id).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_txt_id).clear()
        self.driver.find_element_by_id(self.email_txt_id).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element_by_id(self.phone_txt_id).clear()
        self.driver.find_element_by_id(self.phone_txt_id).send_keys(phone)

    def enter_password(self,pwd):
        self.driver.find_element_by_id(self.password_txt_id).clear()
        self.driver.find_element_by_id(self.password_txt_id).send_keys(pwd)

    def enter_confirmpwd(self,cnfpwd):
        self.driver.find_element_by_id(self.confirm_txt_id).clear()
        self.driver.find_element_by_id(self.confirm_txt_id).send_keys(cnfpwd)

    def click_newsletter_btn(self):
        self.driver.find_element_by_xpath(self.newsltr_rdbtn_xp).click()

    def click_agree_btn(self):
        self.driver.find_element_by_xpath(self.agree_chkbx_xp).click()

    def click_continue(self):
        self.driver.find_element_by_xpath(self.cntn_btn_xp).click()










