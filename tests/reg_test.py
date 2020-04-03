from selenium import webdriver
import pytest
import allure
import moment
from pages.homePage import HomePage
from pages.accPage import AccountPage
from pages.registerPage import RegisterPage
from pages.loginPage import LoginPage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestUserRegistration():

    def test_registration(self):
        try:
            driver=self.driver
            driver.get(utils.URL)

            home=HomePage(driver)
            home.click_myacc_btn()
            home.click_register_btn()

            register=RegisterPage(driver)
            register.enter_firstname(utils.FIRSTNAME)
            register.enter_lastname(utils.LASTNAME)
            register.enter_email(utils.EMAIL)
            register.enter_phone(utils.PHONE)
            register.enter_password(utils.PASSWORD)
            register.enter_confirmpwd(utils.CONFIRM_PWD)
            register.click_newsletter_btn()
            register.click_agree_btn()
            register.click_continue()

            #driver.implicitly_wait(10)

            assert "Your Account Has Been Created" in driver.title

            print("Account created")

            account=AccountPage(driver)
            account.click_continue()
            account.click_logout()


        except AssertionError as error:

            print("There was an exception error\n")
            print(error)
            currTime=moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName=utils.whoami()

            screenshotName=testName+"_"+currTime

            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/Users/sharathsarangmath/Desktop/Test_Automation_Projects/New_Automation/screenshots/"+screenshotName+".png")

            raise
        except:
            print("Some exception occured")
        else:
            print("No exception occured")
        finally:
            print("Final block")

    def test_login(self):
        try:
            driver = self.driver

            home=HomePage(driver)
            home.click_myacc_btn()
            home.click_login()

            login=LoginPage(driver)
            login.enter_email(utils.LogEMAIL)
            login.enter_pwd(utils.PWD)
            driver.implicitly_wait(10)
            login.click_login()
            driver.implicitly_wait(10)

            assert "My Account" in driver.title
            print("Login successful")
            account = AccountPage(driver)
            account.click_logout()

        except AssertionError as error:
            print("There was an exception error\n")
            print(error)

            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()

            screenshotName = testName + "_" + currTime

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("/Users/sharathsarangmath/Desktop/Test_Automation_Projects/New_Automation/screenshots/"+screenshotName+".png")
            raise

        except:
            print("Some exception occured")
        else:
            print("No exception occured")
        finally:
            print("Final block")













