import sys
sys.path.append(sys.path[0] + "/..")
from selenium.webdriver.common.by import By
from setup.Setup import Setting

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

settings = Setting()

driver = settings.driver



class Selectors:
    item = "//img[@title='Apple Cinema 30{}']".format('"')
    view_element_class_name = "quick-view-31"
    alt_text_product = "Nikon D300"
    spinner = "loader-spinner"
    video_element = "mfp-iframe"
    youtube_video = "html5-main-video"
    url = "https://ecommerce-playground.lambdatest.io/"


class TestWatchVideo(Selectors):
    def test_watch_video(self):
        settings.setUp()
        driver.get(self.url)

        wait = WebDriverWait(driver, 10)

        image_visibility_confirmed = f'''
            var img = document.querySelector('img[alt="{self.alt_text_product}"]');
            return img && img.complete;
            '''

        wait.until(lambda driver: driver.execute_script(image_visibility_confirmed))
        
        element_to_hover = driver.execute_script(
            f'return document.querySelector(\'img[alt="{self.alt_text_product}"]\')'
            )
        
        driver.execute_script("arguments[0].scrollIntoView();", element_to_hover)
        
        driver.execute_script(
            "arguments[0].dispatchEvent(new Event('mouseover', { bubbles: true }));", element_to_hover
            )
        
        expanded_view = driver.execute_script(
            f'return document.getElementsByClassName("{self.view_element_class_name}")'
            )
    
        assert element_to_hover and expanded_view, "elements not visible"

        driver.execute_script("arguments[0].click();", expanded_view[0])

        spin = driver.find_element(By.CLASS_NAME, self.spinner)

        spinner = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.spinner)))

        wait.until(EC.invisibility_of_element(spinner))

        assert not spin.is_displayed(), "spinner is still running"

        video_player = driver.find_element(By.CLASS_NAME, self.video_element)

        assert video_player.is_enabled(), "Element not displayed"

        driver.execute_script("arguments[0].click();", video_player)
        
        settings.tearDown()