import sys
sys.path.append(sys.path[0] + "/..")
from selenium.webdriver.common.by import By
from setup.Setup import Setting
import os
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC

settings = Setting()
driver = settings.driver

load_dotenv('.env')


class Selectors:
    username_field = "login_field"
    password_field = "password"
    login_button= "btn"
    input_box = "react-aria-2"
    github_username = os.getenv("GITHUB_USERNAME")
    github_password = os.getenv("GITHUB_PASSWORD")
    url = "https://github.com/new"


class TestCredentials(Selectors):
    def test_credentials(self):
        settings.setUp()
        driver.get(self.url)

        page_title = driver.title


        assert "Sign in to GitHub" in page_title


        driver.execute_script(f'''
        document.getElementById("{self.username_field}").value = "{self.github_username}";
    ''')
        
        driver.execute_script(f'''
        document.getElementById("{self.password_field}").value = "{self.github_password}";
    ''')
        
        login = driver.execute_script(
            f'return document.getElementsByClassName("{self.login_button}")'
            )
        
        driver.execute_async_script(f'''
                var callback = arguments[arguments.length - 1];
                var email = document.getElementById("{self.username_field}").value;
                var password = document.getElementById("{self.password_field}").value;

                    setTimeout(function() {{
                    if (email === "{self.github_username}" && password === "{self.github_password}") {{
                        alert("Login successful!");
                        callback("Authentication successful");   
                    }} else {{
                        alert("password or username incorrect");
                        callback("Authentication failed");      
                    }}
                }}, 2000);
            ''')
        
        alert = driver.switch_to.alert

        assert "Login successful" in alert.text

        alert.accept()
        
        driver.execute_script("arguments[0].click();", login[0])

        driver.current_url

        current_page_title = driver.title

        assert "Where software" in current_page_title
        
        settings.tearDown()