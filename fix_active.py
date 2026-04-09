import os
import re

files_and_targets = {
    'about.html': 'about.html',
    'services.html': 'services.html',
    'projects.html': 'projects.html',
    'credentials.html': 'credentials.html',
    'home-v2.html': 'home-v2.html'
}

for filename, target in files_and_targets.items():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We only want to replace inside <nav class="nav-links"> ... </nav> ideally, but replacing all instances in the header is fine since it's the only nav.
        
        # We look for <a href="about.html">
        # and replace with <a href="about.html" class="active">
        
        # But we must only replace the one in the nav, in case there are other links.
        # Let's find the nav block first.
        nav_match = re.search(r'<nav class="nav-links">.*?</nav>', content, flags=re.DOTALL)
        if nav_match:
            nav_html = nav_match.group(0)
            # Remove any existing active classes from the nav just in case? No, the user says they are NOT green.
            # Add active class to the correct tab
            new_nav_html = re.sub(f'(<a href="{target}")>', r'\1 class="active">', nav_html)
            
            # if target == 'home-v2.html', maybe it links to index.html?
            # actually if it's home-v2, it might link to home-v2 or index.html. We will just look at target
            
            if nav_html != new_nav_html:
                new_content = content.replace(nav_html, new_nav_html)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated nav active class in {filename}")
            else:
                print(f"No changes made to nav in {filename}. Already active or not found.")
        else:
            print(f"Nav not found in {filename}")
