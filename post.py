import csv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_txt import read_text
# import duration
from facebook_login import driver
from selenium.common.exceptions import NoSuchElementException

# Read the links from the file
links = read_text().split('\n')

# Create a CSV file to store the extracted data
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['name', 'text_content'])

    # Iterate over the links
    for link in links[:]: 

        # Open a new tab
        driver.execute_script("window.open();")

        if len(driver.window_handles) > 3:
            driver.switch_to.window(driver.window_handles[-1])  # Switch to the new tab
            driver.close()
            driver.switch_to.window(driver.window_handles[1])

        # Switch to the newly opened tab
        driver.switch_to.window(driver.window_handles[-1])

        # Navigate to the link
        driver.get(link)

        # get name
        name_element = driver.find_element(By.XPATH, '//*[@id=":Rlataql9l9aqqd9emhpapd5aq:"]/span/a/strong/span')
        name_text = name_element.text
        print("___________________________________________________________________", name_text)

        print("Scroll time is starting")
        # start_time = duration.time.time()

        while True:
            post_elements = driver.find_elements(By.XPATH, '//div[@data-ad-comet-preview="message"]')

            if post_elements:
                for post_element in post_elements:
                    try:
                        # Check for the "See more" button and click if present
                        see_more_button = post_element.find_element(By.XPATH, './/div[@role="button" and contains(text(), "See more")]')
                        ActionChains(driver).move_to_element(see_more_button).click().perform()

                    except NoSuchElementException:
                        print("No 'See more' button found. Continuing...")

                    try:
                        # Extract text content from each element
                        text_content = post_element.text
                        print(f"Text Content: {text_content}")
                        # Save the extracted data to the CSV file
                        csv_writer.writerow([name_text, text_content])

                    except Exception as e:
                        print(f"Error extracting text content: {e}")

            # Scroll down
            driver.execute_script("window.scrollBy(0,600);")

            # Wait for a specific duration before scrolling again
            # duration.time.sleep(duration.pause_duration)

            # Check if we have reached the end of the page
            if driver.execute_script("return (window.innerHeight + window.scrollY) >= document.body.scrollHeight"):
                print("Reached end of the page. Moving to the next link.")
                break  # Break out of the while loop and move to the next link

        # Close the current tab
        driver.close()

# Keep the script running for observation
input("Press Enter to close the browser...")
driver.quit()
