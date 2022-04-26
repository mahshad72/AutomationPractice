from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("https://omayo.blogspot.com/")
driver.implicitly_wait(5)  # we can use time.sleep()

myElement = driver.find_element(By.ID, "alert2")
myElement.click()

driver.quit()
