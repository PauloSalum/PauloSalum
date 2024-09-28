import datetime
import re

current_year = datetime.datetime.now().year
years_experience = current_year - 2018

with open('Readme.md', 'r', encoding='utf-8') as file:
    content = file.read()

pattern = r'(<span id="years-experience">)[^<]*(</span>)'
replacement = r'\1 {} \2'.format(years_experience)

new_content = re.sub(pattern, replacement, content)

with open('Readme.md', 'w', encoding='utf-8') as file:
    file.write(new_content)
