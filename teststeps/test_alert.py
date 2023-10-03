from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append(sys.path[0] + "/..")

from setup.Setup import Setting

setting = Setting("Alert simulation async test")
class TestSimulateAlert:
    def test_should_alert_user_and_fail_if_email_exists(self):
        setting.setUp()
        url = "https://signup.sendgrid.com/"

        setting.driver.get(url)

        wait = WebDriverWait(setting.driver, 15)

        email_input = setting.driver.find_element(By.ID, 'email')
        email = 'omisolaidowu@gmail.com'

        email_input.send_keys(email)

        setting.driver.execute_script("""
            var passInput = document.getElementById('password');
            passInput.focus();
        """)

        try:
            error_message = wait.until(EC.presence_of_element_located((By.ID, 'email-info')))
            print(error_message.text)
        except:
            pass
 
        script = """
            var error_message_element = document.getElementById("email-info");
            var callback = arguments[arguments.length - 1];
            var interval = setInterval(function () {
                if (error_message_element) {
                    alert(error_message_element.innerText);
                    clearInterval(interval);
                    callback("Email already exists");
                    
                } else {
                    alert("Fresh email, valid");
                    clearInterval(interval);
                    callback("Successful, email valid");
                }
            }, 100);  
        """
        setting.driver.execute_async_script(script)
        alert = wait.until(EC.alert_is_present())
        alert.accept()      
        setting.driver.current_url
        print(setting.driver.title)
        setting.tearDown()