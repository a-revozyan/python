from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

URL = "https://www.worldometers.info/world-population/"
X_TOTAL = "/html/body/div[3]/div[2]/div[2]/div/div[2]/div/span"
X_BIRTHS_TODAY = "/html/body/div[3]/div[2]/div[2]/div/div[4]/div[1]/div/div[2]/div[2]"
X_DEATHS_TODAY = "/html/body/div[3]/div[2]/div[2]/div/div[4]/div[1]/div/div[3]/div[2]"

class human_population:

    def __init__(self, path):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", False)
        self.options.add_argument("headless")
        self.chrome_driver_path = Service(path)
        self.driver = webdriver.Chrome(options=self.options, service=self.chrome_driver_path)
        self.driver.maximize_window()
        self.total = 0
        self.births_today = 0
        self.deaths_today = 0

    def get_population(self):
        self.driver.get(URL)
        sleep(2)
        self.total = self.driver.find_element(By.XPATH, X_TOTAL).text
        self.births_today = self.driver.find_element(By.XPATH, X_BIRTHS_TODAY).text
        self.deaths_today = self.driver.find_element(By.XPATH, X_DEATHS_TODAY).text