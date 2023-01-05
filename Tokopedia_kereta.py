from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options) 
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.tokopedia.com/kereta-api/?ispulsa=1")
    yield driver
    time.sleep(3)
    driver.quit()


def test_orderKereta(setup):
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[1]/div[1]/div[1]/input').click()
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[1]/div[1]/div[1]/input').send_keys("Malang")
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[3]/div/div[6]').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[1]/div[1]/div[3]/input').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[4]/div/div[9]/div').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[1]/div[2]/div[1]/div[2]/div[1]/label/span').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[1]/div[2]/div[2]/div[1]').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[5]/div[2]/table[1]/tbody/tr[5]/td[4]/div/div[1]').click()
    time.sleep(2)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[5]/div[2]/table[2]/tbody/tr[2]/td[3]/div/div[1]').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[1]/div[3]/div[2]/div').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[6]/div/div[1]/div[2]/button[2]').click()