import sys
sys.path.append(sys.path[0] + "/..")
from setup.Setup import Setting
from selenium.webdriver.common.by import By

setting = Setting("Attribute change test")
driver = setting.driver

class TestChangeElementAttr:
    def test_should_change_class_attr(self):
        setting.setUp()
        url = "https://ecommerce-playground.lambdatest.io/"
        driver.get(url)
        
        #Print the original class attribute since we wanted to see what it was before changing it.
        element = driver.find_element(By.XPATH, '//img[@alt="HTC Touch HD"]')
        print(element.get_attribute('class'))

        #Change the document attribute. 
        script = """
        var element = document.querySelector('img[alt="HTC Touch HD"]');
        element.classList.remove('lazy-load')
        element.classList.add('HTC-touch-smartphone')
        """
        driver.execute_script(script)

        #Confirm that the attribute has changed successfully
        element_new = driver.find_element(By.XPATH, '//img[@alt="HTC Touch HD"]')
        print(element_new.get_attribute('class'))
        setting.tearDown()