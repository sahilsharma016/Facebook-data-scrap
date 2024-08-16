
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


login_url = "https://www.facebook.com/"


driver = webdriver.Chrome()
time.sleep(5)


driver.get(login_url)
time.sleep(5)


username_field = driver.find_element(By.ID,"email") 

time.sleep(5)


username_field.send_keys("don018401@gmail.com")

driver.implicitly_wait(3)

time.sleep(5)

password_field = driver.find_element(By.NAME,"pass") 


password_field.send_keys("Asdf@1234")
time.sleep(3)

 
press_login = driver.find_element(By.NAME,'login')
press_login.send_keys(Keys.RETURN)


""" or uncomment this

input("Press Enter to close the browser...")
driver.quit()

"""


