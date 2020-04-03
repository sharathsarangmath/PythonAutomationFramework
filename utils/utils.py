#CONSTANTS

URL = "http://tutorialsninja.com/demo/index.php?route=common/home"

#REGISTRATION DETAILS

FIRSTNAME = "Sharath"
LASTNAME = "Sarangmath"
EMAIL = "sharathsa@gmail.com"
PHONE = "8971101030"
PASSWORD = "12345"
CONFIRM_PWD = "12345"

#Login details

LogEMAIL="sharathsa@gmail.com"
PWD="12345"

import inspect
def whoami():
    return inspect.stack()[1][3]