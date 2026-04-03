import os
import re

files_to_check = ['index.html', 'about.html', 'services.html', 'credentials.html', 'contact.html', 'projects.html', 'home-v2.html']

def check_html_integrity(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        # Basic check for unclosed div tags logic or common syntax markers
        # For simplicity, we just check tag counts for common <div>
        div_opens = len(re.findall(r'<div', content))
        div_closes = len(re.findall(r'</div', content))
        section_opens = len(re.findall(r'<section', content))
        section_closes = len(re.findall(r'</section', content))
        
        if div_opens != div_closes:
            print(f"Error: {filename} has mismatched <div> tags ({div_opens} open, {div_closes} closed)")
        if section_opens != section_closes:
            print(f"Error: {filename} has mismatched <section> tags ({section_opens} open, {section_closes} closed)")
        
        # Test for unclosed script tags
        script_opens = len(re.findall(r'<script', content))
        script_closes = len(re.findall(r'</script', content))
        if script_opens != script_closes:
            print(f"Error: {filename} has mismatched <script> tags ({script_opens} open, {script_closes} closed)")

for f in files_to_check:
    if os.path.exists(f):
        check_html_integrity(f)
    else:
        print(f"File {f} not found.")

print("Check finished.")
