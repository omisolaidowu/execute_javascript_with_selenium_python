from selenium import webdriver
class Setting:    
    def __init__(self):
        self.driver = webdriver.Chrome()
  
    def setUp(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        if (self.driver != None):
            self.driver.quit()