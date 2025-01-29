# AAAI-Job-Analytics

# codes

### `pagination_scraper.py`
**Purpose**: Extract job-related data from paginated web pages, systematically navigating through each page to collect relevant information from the AAAI Careers website.

**Key Functionality**:
- Input: URL Pattern: https://careers.aaai.org/jobs/browse?page={page_number}. Output File Name: aaai_job_urls.txt.
- Supports ?page=x URL structures, dynamically generated pagination, or "Next" buttons.
- Iterates through multiple pages, following pagination logic.
- Extracts job posting URLs from each page.


# result

### `job_urls.txt`
**Purpose**: A file that stores a list of job posting URLs scraped from websites for analytics, reference, or further processing.

**Key Functionality**:
- Provides a simple and structured format for storing URLs.
- Acts as an input for other scripts that process or analyze the scraped job postings.
- Ensures data persistence and easy sharing of extracted information.
