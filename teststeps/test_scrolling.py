import sys
sys.path.append(sys.path[0] + "/..")
from setup.Setup import Setting
from selenium.webdriver.common.by import By

setting = Setting()

class TestScrolling:
    def test_should_scroll_to_image(self):
        setting.setUp()
        url = "https://ecommerce-playground.lambdatest.io/"
        setting.driver.get(url)

        script = """
                const image_alt = "HTC Touch HD";
                const selector = `img[alt="${image_alt}"]`;
                const img = document.querySelector(selector);
                const pos = img.getBoundingClientRect();
                window.scrollTo(0, pos.top + window.scrollY);
                img.scrollIntoView()
                img.dispatchEvent(new Event('mouseover', { 'bubbles': 'true' }));           
        """
        setting.driver.execute_script(script)

        element = setting.driver.find_element(By.XPATH, '//img[@alt="HTC Touch HD"]')

        relative_height = element.location['y']

        print(f"Current height: {relative_height} px")

        setting.tearDown()

    def test_should_scroll_to_image_easy(self):
        setting.setUp()
        url = "https://ecommerce-playground.lambdatest.io/"
        setting.driver.get(url)

        script = """
                img.scrollIntoView()
                img.dispatchEvent(new Event('mouseover', { 'bubbles': 'true' }));          
        """
        setting.driver.execute_script(script)

        setting.tearDown()




