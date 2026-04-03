import re

svg_logo = """<div class="logo-wrapper" style="display: flex; align-items: center;">
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

header_html = f"""<!-- HEADER -->
  <header>
    <div class="container nav-container">
      <a href="index.html" class="logo" style="text-decoration:none;">
        {svg_logo}
      </a>
      <nav class="nav-links">
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="services.html">Services</a>
        <a href="projects.html">Projects</a>
        <a href="credentials.html">Credentials</a>
        <a href="contact.html" class="active">Contact</a>
      </nav>
      <a href="contact.html" class="btn btn-yellow">Request a Quote</a>
    </div>
  </header>"""

# Fix contact.html Specifically
try:
    with open('contact.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the entire header robustly
    content = re.sub(r'<header>.*?</header>', header_html, content, flags=re.DOTALL)

    # Replace specific contact card details as requested
    content = content.replace('+1 (555) 824-9000', '09260586209')
    content = content.replace('DIRECT LINE', 'Viber / Phone')
    content = content.replace('450 Engineering Plaza, NY', 'Tondo, Manila')
    content = content.replace('Design District, Suite 1200', 'Main Branch')

    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("contact.html successfully updated!")
except Exception as e:
    print(f"Error: {e}")
