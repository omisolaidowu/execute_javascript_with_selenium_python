from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append(sys.path[0] + "/..")

from setup.Setup import Setting

setting = Setting()
class SimulateAlert:
    def it_should_alert_user_and_fail_if_email_exists(self):
        setting.setUp()
        url = "https://signup.sendgrid.com/"

        setting.driver.get(url)

        wait = WebDriverWait(setting.driver, 10)

        email_input = setting.driver.find_element(By.ID, 'email')
        email = 'freshemail@gmail.com'

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
            var error_message_element = document.getElementById("email-info")
            var callback = arguments[arguments.length - 1];

            if (error_message_element) {
                alert("Email exists error")
            } else {
                alert("Fresh email, valid")
            }
            callback();
        """

        setting.driver.execute_script(script)

        alert = setting.driver.switch_to.alert

        print(alert.text)

        assert "valid" in alert.text, "an error has occurred"

        alert.accept()

        setting.driver.current_url

        print(setting.driver.title)

        setting.tearDown()