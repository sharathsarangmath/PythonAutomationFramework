import pytest

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Type in browser name chrome OR firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser=request.config.getoption("--browser")
    if browser=='chrome':
        driver = webdriver.Chrome(executable_path="/Users/sharathsarangmath/Desktop/Test_Automation_Projects/New_Automation/drivers/chromedriver_2")
    elif browser=='firefox':
        driver =webdriver.Firefox(executable_path="/Users/sharathsarangmath/Desktop/Test_Automation_Projects/New_Automation/drivers/geckodriver 2")

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver= driver
    yield
    driver.close()
    driver.quit()
    print("Test complete")