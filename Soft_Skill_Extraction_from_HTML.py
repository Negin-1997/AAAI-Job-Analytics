import json
import re
import os
import pandas as pd

# Path to the JSON file with HTML content
input_file_path = r"C:\Users\negin\Neginn\AI&Education\New Results\HTML_All_Titles.json"

# Path to the Excel file containing the dictionary of soft skills
dictionary_file_path = r"C:\Users\negin\Neginn\AI&Education\Excell\Dictionary of soft skills.xlsx"

# Load the dictionary of soft skills from Excel (read all rows from the first column)
soft_skills_df = pd.read_excel(dictionary_file_path, header=None)  # No header in the file
soft_skills = soft_skills_df[0].dropna().tolist()  # Read the first column (index 0)

# Compile regex patterns for each soft skill (case-insensitive search)
soft_skill_patterns = {skill: re.compile(rf"\b{skill}\b", re.IGNORECASE) for skill in soft_skills}

# Load the HTML JSON file
with open(input_file_path, 'r', encoding='utf-8') as file:
    html_data = json.load(file)

# Results to store soft skills per URL
extracted_skills = []

# Loop through each entry in the JSON file
for idx, entry in enumerate(html_data):
    url = entry.get("url")
    html_content = entry.get("html", "")
    found_skills = []

    # Search for each soft skill in the HTML content
    for skill, pattern in soft_skill_patterns.items():
        if pattern.search(html_content):  # If skill is found in HTML
            found_skills.append(skill)

    # Append the results for this URL
    extracted_skills.append({
        "url": url,
        "soft_skills": found_skills
    })

    # Log progress every 10 entries
    if idx % 10 == 0:
        print(f"Processed {idx + 1}/{len(html_data)} entries.")

# Save the extracted skills to a new JSON file
output_file_path = r"C:\Users\negin\Neginn\AI&Education\New Results\Extracted_Soft_Skills.json"
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(extracted_skills, file, ensure_ascii=False, indent=4)

print(f"Soft skills extracted and saved to {output_file_path}")
