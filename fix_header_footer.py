import glob
import re

svg_logo = """<div style="display: flex; align-items: center;">
  <svg width="45" height="45" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Crescent Moon -->
    <path d="M 50 5 A 45 45 0 1 0 85 85 A 50 50 0 1 1 50 5 Z" fill="url(#moonGrad)"/>
    <!-- Leaf Stalk -->
    <path d="M 45 90 Q 42 65 45 40" stroke="#4ade80" stroke-width="2.5" fill="none"/>
    <!-- Left Leaf -->
    <path d="M 43 70 Q 20 65 25 45 Q 35 45 43 70" fill="#4ade80"/>
    <!-- Top Leaf -->
    <path d="M 45 45 Q 35 20 50 15 Q 60 25 45 45" fill="#4ade80"/>
    <!-- Right Leaf -->
    <path d="M 44 60 Q 65 55 70 40 Q 55 40 44 60" fill="#4ade80"/>
    <defs>
      <linearGradient id="moonGrad" x1="0" y1="0" x2="100" y2="100" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#fde047"/>
        <stop offset="100%" stop-color="#eab308"/>
      </linearGradient>
    </defs>
  </svg>
  <span style="font-family: 'Outfit', sans-serif; font-weight: 800; color: #fbbf24; font-size: 1.8rem; margin-left: 0.5rem; letter-spacing: 0.5px;">Crecer</span>
</div>"""

footer_socials = """<div class="footer-socials">
            <a href="https://www.facebook.com/projectcrecer" target="_blank" rel="noopener noreferrer" class="social-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
            </a>
            <a href="#" class="social-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5 2.8 13.5 3 12c-.5 0-1-.2-1.4-.6C-.2 9.6 1.4 8 1.4 8s-1.8-4.5 1-6c1.8 1 4 1.5 6.2 1.5C9.6 2 11 1 12.8 1.4c1.5.3 2.7 1.5 3 3 1.2-.3 2.3-.9 3.2-1.4z"></path></svg>
            </a>
            <a href="#" class="social-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
            </a>
          </div>"""

# Ensure Request Quote button has soft shadow matching Figma image
new_css = """
.btn-yellow { 
  background: linear-gradient(180deg, #fcd34d 0%, #f59e0b 100%); 
  color: #111827; 
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.3);
}
.social-icon { 
  width: 40px; height: 40px; 
  background-color: #1a2332; 
  border-radius: 50%; 
  display: flex; align-items: center; justify-content: center; 
  color: #cad1da; 
  transition: 0.3s ease; 
}
.social-icon:hover { 
  background-color: #1f8a4c; 
  color: #ffffff; 
}
.nav-links a.active { color: #27ae60; }
"""

# Open style.css and append the new button styles if not present
with open('style.css', 'r', encoding='utf-8') as f:
    css_text = f.read()
if ".nav-links a.active" not in css_text:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(new_css)

# Process HTML files
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace the old image logo with pure robust SVG Logo!
    html = re.sub(r'<img src="logo\.png".*?>', svg_logo, html)
    
    # Force the home nav link to be literally "Home" with active class explicitly set correctly
    if file == 'index.html':
       html = re.sub(r'<a href="index.html">Home</a>', '<a href="index.html" class="active">Home</a>', html)
       
    # Replace social icons
    html = re.sub(r'<div class="footer-socials">.*?</div>', footer_socials, html, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Headers and Footers matched locally, logos corrected.")
