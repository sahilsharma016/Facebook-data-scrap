import time
import csv
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_txt import read_text
from facebook_login import driver
from selenium.common.exceptions import NoSuchElementException

links = read_text().split('\n')

with open('final.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['name', 'text_content'])


    start_time = time.time()
    for link in links[:]:
        
        driver.execute_script("window.open();")

        if len(driver.window_handles) > 3:
            driver.switch_to.window(driver.window_handles[-1])  # Switch to the new tab
            driver.close()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(4)

        # Switch to the newly opened tab
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)

       
        driver.get(link)
        time.sleep(4)

        # Wait for the footer to be visible
        footer = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//footer')))

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        
        time.sleep(6)

     
        driver.execute_script("window.scrollTo(0, 0);")

        
        time.sleep(3)

        # Keep scrolling until the bottom of the page is reached
        while True:
            # Scroll down by 1000 pixels
            driver.execute_script("window.scrollBy(0, 1500);")

            time.sleep(2)

            # Check if the bottom of the page is reached
            if driver.execute_script("return window.scrollY + window.innerHeight >= document.body.scrollHeight;"):
                break

           
            post_elementz = driver.find_elements(By.XPATH, '//div[@data-ad-comet-preview="message"]')

            for e in post_elementz:
                
                print(e.text)
                csv_writer.writerow([link, e.text])

            try:
                name_element = driver.find_element(By.XPATH, '//div[@data-ad-comet-preview="message"]//div[@class="_12p _1wj"]//a[@class="_12p _1wj"]//strong//span')
             
                print("___________________________________________________________________")

            except NoSuchElementException:
                print("name not found")



    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")

