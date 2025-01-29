import requests
import json
import os

# Path to the file containing URLs
input_file_path = r"C:\Users\negin\RA_Workspace\AAA\job_urls.txt"

# Read the URLs from the file
with open(input_file_path, 'r') as file:
    urls = [line.strip() for line in file.readlines() if line.strip()]

# Dictionary to store results
results = []

# Loop through each URL, fetch HTML, and save to results
for url in urls:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        html_content = response.text
        results.append({"url": url, "html": html_content})
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        results.append({"url": url, "html": None, "error": str(e)})

# Specify output directory and filename
output_directory = r"C:\Users\negin\Neginn\AI&Education\New Results"
output_filename = "HTML_All_Titles.json"
output_path = os.path.join(output_directory, output_filename)

# Ensure the directory exists
os.makedirs(output_directory, exist_ok=True)

# Write results to the file
with open(output_path, 'w', encoding='utf-8') as file:
    json.dump(results, file, ensure_ascii=False, indent=4)

print(f"HTML content saved to {output_path}")
