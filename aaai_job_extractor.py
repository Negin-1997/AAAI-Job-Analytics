from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Correct path to chromedriver.exe
driver_path = r"C:\Users\negin\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: Run in headless mode
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(service=service, options=options)

# Initialize a set to store unique URLs
all_urls = set()

try:
    # Loop through all 85 pages
    for page in range(1, 86):  # Adjust range if needed
        page_url = f"https://careers.aaai.org/jobs/browse?page={page}"
        driver.get(page_url)
        
        # Wait for the page to load
        time.sleep(3)

        # Extract all job posting links on the current page
        job_links = driver.find_elements(By.XPATH, '//a[contains(@href, "/jobs/")]')
        for link in job_links:
            url = link.get_attribute('href')
            if url and url.startswith("https://careers.aaai.org/jobs/"):  # Ensure the URL is valid
                all_urls.add(url)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Save the URLs to a file
    with open("job_urls.txt", "w") as file:
        for url in sorted(all_urls):  # Sort URLs for easier debugging
            file.write(url + "\n")

    # Close the WebDriver
    driver.quit()

# Print completion message
print(f"Scraping completed. {len(all_urls)} job URLs saved to job_urls.txt.")
