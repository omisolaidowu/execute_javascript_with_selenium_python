import sys
sys.path.append(sys.path[0] + "/..")
from setup.Setup import Setting
setting = Setting()

class TestStyleChange:
    def test_should_change_style(self):
        setting.setUp()
        print("Driver instance has started...")
        url = "https://signup.sendgrid.com/" 
        setting.driver.get(url)
        button_class = "btn"


        script = f'''
        var buttons = document.getElementsByClassName('{button_class}');
        var button = buttons[0];
        button.disabled = false;
        button.style.backgroundColor = 'green';
        button.style.color = 'white';
'''
        
        setting.driver.execute_script(script)

        print("Style changed successfully")

        setting.tearDown()