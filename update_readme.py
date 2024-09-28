import datetime
import re

# Calculate years of experience
current_year = datetime.datetime.now().year
years_experience = current_year - 2018

# Read the README.md file
with open('README.md', 'r', encoding='utf-8') as file:
    content = file.read()

# Replace the placeholder with the calculated years
new_content = re.sub(r'<span id="years-experience"></span>', f'{years_experience}', content)

# Write the updated content back to README.md
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(new_content)
