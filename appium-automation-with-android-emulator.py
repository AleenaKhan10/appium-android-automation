# Import necessary modules
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

def configure_chrome_with_proxy() -> Dict[str, Any]:
    # chrome_options = ChromeOptions()
    # proxy = "https://{username}:{password}@{host}:{port}"
    # chrome_options.add_argument(f'--proxy-server={proxy}')
    
    chrome_driver_path = ChromeDriverManager(driver_version="83.0.4103.14").install()
    cap = {
        "platformName": "Android",
        "appium:automationName": "uiautomator2",
        "appium:platformVersion": "11",
        "appium:deviceName": "myEmulator",
        "browserName": "Chrome",
        "appium:newCommandTimeout": 900,
        "appium:chromedriverExecutable": chrome_driver_path
        # "appium:chromeOptions": {
        #     "args": chrome_options.arguments
        # },
    }
    return cap


# Function to perform actions with a specific proxy
def perform_actions_with_proxy():
    cap = configure_chrome_with_proxy()
    
    # Appium server URL
    url = "http://localhost:4723"
    
    # Initialize the Appium driver with the specified capabilities
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    driver.get("https://bot.incolumitas.com/")
    
    # Perform search on Google
    search_box = driver.find_element(by=AppiumBy.XPATH, value='//textarea[@name="q"]')
    for char in "automation":
        search_box.send_keys(char)
    driver.press_keycode(66)
    
    time.sleep(10)  # Wait for the results page to load
    
    
    # Quit the Appium driver
    driver.quit()

perform_actions_with_proxy()
