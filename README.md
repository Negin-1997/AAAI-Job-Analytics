# AAAI-Job-Analytics

# codes

### `pagination_scraper.py`
**Purpose**: Extract job-related data from paginated web pages, systematically navigating through each page to collect relevant information from the AAAI Careers website.

**Key Functionality**:
- Input: URL Pattern: https://careers.aaai.org/jobs/browse?page={page_number}. Output File Name: aaai_job_urls.txt.
- Supports ?page=x URL structures, dynamically generated pagination, or "Next" buttons.
- Iterates through multiple pages, following pagination logic.
- Extracts job posting URLs from each page.

### `fetch_html_content.py` 
**Purpose**: To fetch HTML content from a list of URLs provided in a text file and save the results (including errors, if any) into a structured JSON file for further processing or analysis.

**Key Functionality**:
- Input File Name:job_urls.txt. Output File Name: HTML_All_Titles.json
- Reads a list of URLs from a specified input file.
- Sends HTTP GET requests to each URL.
- Captures the HTML content of the pages.
- Handles errors gracefully (e.g., timeouts, HTTP errors).
- Stores the fetched content in a JSON file with structured fields (url, html, error).
  


# result

### `job_urls.txt`
**Purpose**: A file that stores a list of job posting URLs scraped from websites for analytics, reference, or further processing.

**Key Functionality**:
- Provides a simple and structured format for storing URLs.
- Acts as an input for other scripts that process or analyze the scraped job postings.
- Ensures data persistence and easy sharing of extracted information.

### `HTML_All_Titles.json` NOT AVAILBLE 
**Purpose**: To store the results of HTML content fetched from a list of URLs, including both successfully fetched pages and any errors encountered during the fetching process. This JSON file serves as a structured data format for further analysis or debugging.

**Key Functionality**:
- Input File Name:job_urls.txt. Output File Name: HTML_All_Titles.json. Script name:`fetch_html_content.py`
- Each entry contains the URL and its associated HTML content.
- Captures errors (e.g., timeouts, bad status codes) for any URL where HTML content couldn't be fetched, making it easier to debug problematic URLs.
- The file is in JSON format with the following fields for each URL: url: The URL of the web page. html: The HTML content of the page (or None if an error occurred). error: A string describing the error (if any).
