from selenium import webdriver
from dotenv import load_dotenv
import os
load_dotenv('.env')
LT_USERNAME = os.getenv("LT_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

options = webdriver.ChromeOptions()
options.browser_version = "latest"
options.platform_name = "Windows 10"
lt_options = {}
lt_options["username"] = os.getenv("LT_USERNAME")
lt_options["accessKey"] = os.getenv("LT_ACCESS_KEY")
lt_options["build"] = "JavaScript execution demos"
lt_options["project"] = "Elements Check Tests"
lt_options["name"] = "JavaScript demo"
lt_options["console"] = "error"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"

options.set_capability('LT:Options', lt_options)

gridURL = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub"


class Setting:    
    def __init__(self):
        self.driver = webdriver.Remote(command_executor=gridURL, options= options)
  
    def setUp(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        if (self.driver != None):
            self.driver.quit()