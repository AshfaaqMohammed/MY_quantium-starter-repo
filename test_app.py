from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service('C:\webrowsers\chromedriver.exe')

# driver = webdriver.Chrome(service=s)
# driver.get("http://127.0.0.1:8050")
#
# ele = driver.find_element(By.ID, value="header")
# print(ele)
#
# loc = driver.service.path
# print(loc)
#
# driver.quit()


def test_header_present():
    driver = webdriver.Chrome(service=s)
    driver.get("http://127.0.0.1:8050/")

    # Check if the header is present
    assert driver.find_element(By.ID, value="header")

    driver.quit()


def test_visualization_present():
    driver = webdriver.Chrome(service=s)
    driver.get("http://127.0.0.1:8050/")

    # Check if the visualization is present
    assert driver.find_element(By.ID, value="line-chart")

    driver.quit()


def test_region_picker_present():
    driver = webdriver.Chrome(service=s)
    driver.get("http://127.0.0.1:8050/")

    # Check if the region picker is present
    assert driver.find_element(By.ID, value="region-radio")

    driver.quit()
