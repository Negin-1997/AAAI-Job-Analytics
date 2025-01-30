from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
import time
import os

# File paths
input_file_path = r"C:\Users\negin\AAAI-Job-Analytics\job_urls.txt"
output_file_path = r"C:\Users\negin\AAAI-Job-Analytics\Extracted_Job_Details.json"

# Chrome WebDriver setup (replace with your ChromeDriver path)
driver_path = r"C:\Users\negin\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (no browser window)
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=service, options=options)

# Function to extract job details using Selenium
def extract_job_details_selenium(url):
    try:
        driver.get(url)
        time.sleep(3)  # Wait for the page to load

        # Extract details using Selenium
        job_title = driver.find_element(By.CLASS_NAME, "pb-0.mb-0.text-primary").text
        job_description = driver.find_element(By.CLASS_NAME, "job-description").text

        posted_date = driver.find_element(By.XPATH, "//div[text()='Posted:']/following-sibling::div").text
        location = driver.find_element(By.XPATH, "//div[text()='Location:']/following-sibling::div").text
        job_type = driver.find_element(By.XPATH, "//div[text()='Type:']/following-sibling::div").text
        categories = driver.find_element(By.XPATH, "//div[text()='Categories:']/following-sibling::div").text
        years_of_experience = driver.find_element(By.XPATH, "//div[text()='Years of Experience:']/following-sibling::div").text
        required_education = driver.find_element(By.XPATH, "//div[text()='Required Education:']/following-sibling::div").text

        # Return all extracted details
        return {
            "url": url,
            "job_title": job_title,
            "job_description": job_description,
            "posted_date": posted_date,
            "location": location,
            "job_type": job_type,
            "categories": categories,
            "years_of_experience": years_of_experience,
            "required_education": required_education
        }

    except Exception as e:
        print(f"Failed to fetch details from {url}: {e}")
        return {
            "url": url,
            "error": str(e)
        }

# Load URLs from the file
with open(input_file_path, 'r') as file:
    job_urls = [line.strip() for line in file if line.strip()]

# List to store extracted job details
job_details = []

# Loop through each URL and extract details
for idx, url in enumerate(job_urls):
    print(f"Processing {idx + 1}/{len(job_urls)}: {url}")
    details = extract_job_details_selenium(url)
    job_details.append(details)

# Save extracted details to a JSON file
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(job_details, file, ensure_ascii=False, indent=4)

print(f"Job details extracted and saved to {output_file_path}")

# Close the WebDriver
driver.quit()
