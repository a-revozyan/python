from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

DRIVER_PATH = "C:\Selenium\chromedriver.exe"
URL = "https://www.speedtest.net/"
XPATH_BUTTON = "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a"
XPATH_UP = "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span"
XPATH_DOWN = "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span"
XPATH_SCREEN = "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]"

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# chrome_driver_path = Service(DRIVER_PATH)
# driver = webdriver.Chrome(options=options, service=chrome_driver_path)
# driver.maximize_window()
class InternetSpeedBot:

    def __init__(self, path):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.chrome_driver_path = Service(path)
        self.driver = webdriver.Chrome(options=self.options, service=self.chrome_driver_path)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0
        self.screen = 0

    def get_internet_speed(self, urls, x_button, x_up, x_down, x_screen):
        self.driver.get(urls)
        sleep(3)
        go_button = self.driver.find_element(By.XPATH, x_button)
        go_button.click()
        sleep(100)
        self.up = self.driver.find_element(By.XPATH, x_up).text
        self.down = self.driver.find_element(By.XPATH, x_down).text
        self.screen = self.driver.find_element(By.XPATH, x_screen).screenshot("result.png")