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
    driver.get("https://www.tokopedia.com/flight/")
    yield driver
    time.sleep(5)
    driver.quit()

def test_orderFlight(setup):
    # input kota asal
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[1]/div[1]/div[1]/input').click()
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[1]/div[1]/div[1]/input').send_keys("Yogya")
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[3]/div/div[2]/div').click()
    # input kota tujuan
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[1]/div[1]/div[3]/input').click()
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[1]/div[1]/div[3]/input').send_keys("Jak")
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[4]/div/div[3]').click()

    # click check box untuk memunculkan tanggal pulang
    # setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[1]/div[2]/div[1]/div[2]/div[1]/label/span').click()
    # time.sleep(2)

    # input tanggal berangkat
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[1]/div[2]/div[2]/div').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[5]/div[2]/table[1]/tbody/tr[4]/td[7]/div/div[1]').click()
    time.sleep(1)

    # # input tanggal pulang
    # setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[5]/div[2]/table[1]/tbody/tr[5]/td[4]/div/div[1]').click
    
    # input jumlah penumpang dewasa (+)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[6]').click()
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[6]/div/div[1]/div[2]/button[2]').click()
    time.sleep(1)

    # input jumlah penumpang dewasa (-)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[6]/div/div[1]/div[2]/button[1]').click()
    time.sleep(1)

    # input jumlah penumpang anak (+)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[6]/div/div[2]/div[2]/button[2]').click()
    time.sleep(1)

    # input jumlah penumpang anak (-)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[6]/div/div[2]/div[2]/button[1]').click()
    time.sleep(1)

    # input jumlah penumpang bayi (+)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[6]/div/div[3]/div[2]/button[2]').click()
    time.sleep(1)

    # input jumlah penumpang bayi (-)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[6]/div/div[3]/div[2]/button[1]').click()
    time.sleep(1)

    # simpan jumlah penumpang
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[6]/div/div[4]/button').click()

    # pilih kelas penerbangan
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[1]/div[4]/div[2]/div').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[7]/div/div[2]').click()
    time.sleep(1)

    # click button cari tiket
    setup.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/section/div[2]/button').click()