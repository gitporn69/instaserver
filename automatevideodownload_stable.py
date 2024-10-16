from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Define the path to your ChromeDriver
chrome_driver_path = r'D:\FuckingDownloads\chrome-win64\chromedriver.exe'

# Set up the Service object with the path
service = Service(chrome_driver_path)

# Initialize the Chrome driver using the Service object
driver = webdriver.Chrome(service=service)

try:
    # Visit the FastDL website
    driver.get('https://fastdl.app/en')

    # Wait for the page to load (you can adjust the sleep time as needed)
    time.sleep(2)

    # Find the input field for the Instagram URL (update the selector if needed)
    input_field = driver.find_element('name', 'url')
    
    # Enter the Instagram video URL (replace with the actual URL you want to download)
    instagram_video_url = input("Enter url: ")  # Replace this with the actual Instagram video URL
    input_field.send_keys(instagram_video_url)

    # Trigger the download process by pressing Enter
    input_field.send_keys(Keys.RETURN)

    # Wait for the download button to appear (adjust the sleep time if necessary)
    time.sleep(5)

    # Find the download button and click it (update the selector if needed)
    download_button = driver.find_element('class name', 'download-btn')
    download_button.click()

    # Wait for a while to let the download start (adjust the time as necessary)
    time.sleep(10)

finally:
    # Close the browser after the process (optional)
    driver.quit()

print("Download process complete.")
