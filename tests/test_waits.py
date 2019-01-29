import time
from selenium.webdriver.support import expected_conditions as ec

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# const
PATH = './chromedriver'
URL = 'http://common-remarks.com/'
TIME = 10


def test_thread_wait():
    driver = webdriver.Chrome(PATH)
    driver.get(URL)
    time.sleep(TIME)
    driver.find_element_by_id('author-slider')
    driver.quit()


def test_implicit_wait():
    driver = webdriver.Chrome(PATH)
    driver.get(URL)
    driver.implicitly_wait(TIME)
    driver.find_element_by_id('author-slider')
    driver.quit()


def test_explicit_wait():
    driver = webdriver.Chrome(PATH)
    driver.get(URL)
    wait = WebDriverWait(driver, TIME)
    wait.until(ec.visibility_of_element_located((By.ID, 'author-slider')))
    driver.quit()
