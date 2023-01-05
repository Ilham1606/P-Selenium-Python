from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import pyautogui

Kota = [('Yogyakarta')]

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options) 
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.tokopedia.com/hotel/")
    yield driver


@pytest.mark.parametrize('a',Kota)
def test_orderHotel(setup, a):
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]').click()
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/input').send_keys(Kota)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/div[1]').click()
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div').send_keys('Kam, 29/12/2022')

    
