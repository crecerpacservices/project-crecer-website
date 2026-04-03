import glob
import re

css_content = '''@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

:root {
  --clr-green: #1f8a4c;
  --clr-green-dark: #12542d;
  --clr-yellow: #fbbf24;
  --clr-yellow-hover: #f59e0b;
  --clr-dark: #11151c;
  --clr-dark-green: #0f1c16;
  --clr-text: #4b5563;
  --clr-heading: #111827;
  --clr-light: #f9fafb;
  --clr-white: #ffffff;
  --font-heading: 'Outfit', sans-serif;
  --font-body: 'Inter', sans-serif;
  --max-width: 1440px;
  --radius: 8px;
  --transition: 0.3s ease;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: var(--font-body); color: var(--clr-text); line-height: 1.6; background-color: var(--clr-white); -webkit-font-smoothing: antialiased; }
h1, h2, h3, h4, h5, h6 { font-family: var(--font-heading); color: var(--clr-heading); line-height: 1.2; }
a { text-decoration: none; color: inherit; transition: var(--transition); }
ul { list-style: none; }
img { max-width: 100%; display: block; }

.container { max-width: var(--max-width); margin: 0 auto; padding: 0 2rem; }
.flex-between { display: flex; justify-content: space-between; align-items: flex-end; }
.bg-light { background-color: var(--clr-light); }
.bg-green-dark { background-color: var(--clr-green-dark); }
.bg-dark { background-color: var(--clr-dark); }
.text-center { text-align: center; }

/* Buttons */
.btn { display: inline-block; padding: 0.8rem 1.75rem; border-radius: var(--radius); font-weight: 600; text-align: center; cursor: pointer; border: none; transition: var(--transition); font-family: var(--font-body); }
.btn-yellow { background-color: var(--clr-yellow); color: var(--clr-heading); }
.btn-yellow:hover { background-color: var(--clr-yellow-hover); }
.btn-green { background-color: var(--clr-green); color: var(--clr-white); }
.btn-green:hover { background-color: var(--clr-green-dark); }
.btn-outline { background-color: transparent; border: 2px solid var(--clr-white); color: var(--clr-white); }
.btn-outline:hover { background-color: var(--clr-white); color: var(--clr-heading); }
.link-green { font-weight: 600; color: var(--clr-green); display: inline-block; margin-top: 1rem; }

/* Header */
header { position: sticky; top: 0; background-color: var(--clr-white); z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
.nav-container { display: flex; align-items: center; justify-content: space-between; height: 90px; }
.logo img { height: 50px; }
.nav-links { display: flex; gap: 2.5rem; }
.nav-links a { font-weight: 600; font-size: 0.95rem; color: var(--clr-heading); }
.nav-links a:hover, .nav-links a.active { color: var(--clr-green); }

/* Footer */
footer { background-color: var(--clr-dark); color: rgba(255,255,255,0.7); padding: 5rem 0 2rem; position: relative; z-index: 1; border-top: 1px solid var(--clr-dark); }
.footer-grid { display: grid; grid-template-columns: 2.5fr 1fr 1fr 1.5fr; gap: 4rem; margin-bottom: 4rem; }
.footer-col h4 { color: var(--clr-white); margin-bottom: 2rem; font-size: 1.15rem; font-weight: 700; }
.footer-col ul { display: flex; flex-direction: column; gap: 1.25rem; }
.footer-col a:hover { color: var(--clr-green); }
.footer-bottom { border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 2rem; display: flex; justify-content: space-between; font-size: 0.875rem; }
.footer-socials { display: flex; gap: 1rem; margin-top: 2rem; }
.social-icon { width: 42px; height: 42px; background-color: rgba(255, 255, 255, 0.05); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: var(--clr-white); transition: var(--transition); }
.social-icon:hover { background-color: var(--clr-green); color: white; }
.social-icon svg { width: 22px; height: 22px; }
.social-icon i { width: 22px; height: 22px; }
.footer-col i { color: var(--clr-green); flex-shrink: 0; width: 20px; }

/* Base Layout */
.section-padding { padding: 6rem 0; }
.section-title { text-align: center; margin-bottom: 4rem; }
.section-title h2 { font-size: 2.5rem; margin-bottom: 1rem; }
.section-title p { color: var(--clr-text); max-width: 600px; margin: 0 auto; font-size: 1.1rem; }

/* Home Hero */
.hero { position: relative; padding: 12rem 0; background-image: url('hero-bg.png'); background-size: cover; background-position: center; border-bottom: 6px solid var(--clr-yellow); }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(rgba(17,21,28,0.7), rgba(17,21,28,0.8)); }
.hero-content { position: relative; z-index: 1; color: white; max-width: 900px; text-align: center; margin: 0 auto; }
.hero-badge { display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(31, 138, 76, 0.2); color: var(--clr-yellow); font-weight: 700; letter-spacing: 2px; font-size: 0.85rem; padding: 0.5rem 1rem; border-radius: 50px; margin-bottom: 1.5rem; }
.badge-dot { width: 8px; height: 8px; background-color: var(--clr-yellow); border-radius: 50%; }
.hero h1 { font-size: 5.5rem; margin-bottom: 1.5rem; color: white; line-height: 1.1; letter-spacing: -1px; }
.hero h1 span { color: var(--clr-yellow); }
.hero p { font-size: 1.25rem; margin-bottom: 3rem; color: rgba(255,255,255,0.9); max-width: 700px; margin-left: auto; margin-right: auto; line-height: 1.8; }
.hero-buttons { display: flex; justify-content: center; gap: 1rem; }

/* Other components (Services, Creds, Portfolio, Why Us, CTA) */
.cred-grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 1.5rem; }
.cred-card { background: var(--clr-white); padding: 1.5rem 1rem; border-radius: var(--radius); text-align: center; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); transition: var(--transition); border-top: 3px solid transparent; }
.cred-card:hover { transform: translateY(-5px); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); border-top-color: var(--clr-yellow); }
.cred-icon { width: 50px; height: 50px; background: rgba(31, 138, 76, 0.1); color: var(--clr-green); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; }
.cred-card p { font-weight: 600; font-size: 0.85rem; color: var(--clr-heading); }

.services-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; }
.service-card { background: var(--clr-white); padding: 2.5rem 1.5rem; border-radius: var(--radius); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); transition: var(--transition); }
.service-card:hover { box-shadow: 0 10px 20px -5px rgba(0,0,0,0.1); transform: translateY(-5px); }
.service-icon { width: 60px; height: 60px; background: rgba(31, 138, 76, 0.1); color: var(--clr-green); border-radius: var(--radius); display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; }
.service-card h3 { margin-bottom: 1rem; font-size: 1.25rem; }
.service-card p { font-size: 0.95rem; margin-bottom: 1.5rem; }

.portfolio-grid { display: grid; grid-template-columns: repeat(3, 1fr); grid-auto-rows: 300px; gap: 1.5rem; }
.port-item { border-radius: var(--radius); overflow: hidden; position: relative; }
.port-item img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }
.port-item:hover img { transform: scale(1.05); }
.port-item.tall { grid-row: span 2; }
.port-item.wide { grid-column: span 2; }

.why-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; text-align: center; }
.why-icon { width: 70px; height: 70px; background: var(--clr-yellow); color: var(--clr-heading); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; box-shadow: 0 10px 15px -3px rgba(251,191,36,0.3); }

.cta-floating { position: relative; top: 100px; z-index: 10; margin-bottom: 100px; }
.cta-box { background: var(--clr-white); padding: 4rem; border-radius: var(--radius); text-align: center; box-shadow: 0 20px 40px -10px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05); }
.cta-box h2 { font-size: 2.5rem; margin-bottom: 1rem; }

@media (max-width: 1024px) {
  .hero h1 { font-size: 4rem; }
  .services-grid, .why-grid { grid-template-columns: repeat(2, 1fr); }
  .cred-grid { grid-template-columns: repeat(3, 1fr); }
  .footer-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 768px) {
  .nav-links { display: none; }
  .hero h1 { font-size: 3rem; }
  .services-grid, .why-grid, .cred-grid { grid-template-columns: 1fr; }
  .portfolio-grid { grid-template-columns: 1fr; grid-auto-rows: auto; }
  .port-item.tall, .port-item.wide { grid-row: span 1; grid-column: span 1; }
  .port-item img { height: 250px; }
  .footer-grid { grid-template-columns: 1fr; gap: 2rem; }
  .footer-bottom { flex-direction: column; gap: 1rem; text-align: center; }
  .flex-between { flex-direction: column; align-items: flex-start; gap: 1rem; }
}
'''

hero_html = '''  <!-- HERO SECTION -->
  <section class="hero">
    <div class="hero-overlay"></div>
    <div class="container hero-content">
      <div class="hero-badge">
        <span class="badge-dot"></span> ENGINEERING THE FUTURE
      </div>
      <h1>Engineering<br>Excellence.<br><span>Sustainable<br>Growth.</span></h1>
      <p>We provide world-class technical expertise and sustainable solutions for large-scale construction and infrastructure projects.</p>
      <div class="hero-buttons">
        <a href="contact.html" class="btn btn-yellow">Get Started</a>
        <a href="projects.html" class="btn btn-outline">View Our Projects</a>
      </div>
    </div>
  </section>'''

footer_html = '''  <!-- FOOTER -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col" style="padding-right: 2rem;">
          <a href="index.html" style="display:inline-block; margin-bottom: 1.5rem;">
            <img src="logo.png" alt="Crecer Logo" style="height: 48px;">
          </a>
          <p style="font-size: 0.95rem; line-height: 1.8; margin-bottom: 2rem;">Leading the way in sustainable engineering and modern construction practices. Dedicated to growth and environmental responsibility.</p>
          <div class="footer-socials">
            <a href="https://www.facebook.com/projectcrecer" target="_blank" rel="noopener noreferrer" class="social-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
            </a>
            <a href="#" class="social-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5 2.8 13.5 3 12c-.5 0-1-.2-1.4-.6C-.2 9.6 1.4 8 1.4 8s-1.8-4.5 1-6c1.8 1 4 1.5 6.2 1.5C9.6 2 11 1 12.8 1.4c1.5.3 2.7 1.5 3 3 1.2-.3 2.3-.9 3.2-1.4z"></path></svg>
            </a>
            <a href="#" class="social-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
            </a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Our Mission</a></li>
            <li><a href="services.html">Our Services</a></li>
            <li><a href="projects.html">Latest Projects</a></li>
            <li><a href="#">Sustainability Reports</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Expertise</h4>
          <ul>
            <li><a href="#">Civil Engineering</a></li>
            <li><a href="#">Fire Safety Systems</a></li>
            <li><a href="#">Sustainable Infrastructure</a></li>
            <li><a href="#">Electrical Engineering</a></li>
            <li><a href="#">Project Management</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contact Us</h4>
          <ul style="gap: 1.5rem;">
            <li style="display: flex; gap: 1rem; align-items: flex-start;"><i data-lucide="map-pin" style="margin-top: 3px;"></i> <div>123 Engineering Way, Innovation District, PH 12345</div></li>
            <li style="display: flex; gap: 1rem; align-items: center;"><i data-lucide="phone"></i> <div>+63 (2) 8888-0000</div></li>
            <li style="display: flex; gap: 1rem; align-items: center;"><i data-lucide="mail"></i> <div>crecerpacservices@gmail.com</div></li>
            <li style="display: flex; gap: 1rem; align-items: center;"><i data-lucide="clock"></i> <div>Mon - Fri: 8:00 AM - 6:00 PM</div></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Crecer. All Rights Reserved.</p>
        <div style="display: flex; gap: 2rem;">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
          <a href="#">Cookie Policy</a>
        </div>
      </div>
    </div>
  </footer>'''

header_html = '''  <!-- HEADER -->
  <header>
    <div class="container nav-container">
      <a href="index.html" class="logo">
        <img src="logo.png" alt="Crecer Logo" style="height: 48px;">
      </a>
      <nav class="nav-links">
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="services.html">Services</a>
        <a href="projects.html">Projects</a>
        <a href="credentials.html">Credentials</a>
        <a href="contact.html">Contact</a>
      </nav>
      <a href="contact.html" class="btn btn-yellow">Request a Quote</a>
    </div>
  </header>'''

# 1. Update style.css
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Update HTML files
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace header block correctly no matter what's in it currently
    content = re.sub(r'<!-- HEADER -->.*?</header>', header_html, content, flags=re.DOTALL)
    
    # Replace footer block correctly
    content = re.sub(r'<!-- FOOTER -->.*?</footer>', footer_html, content, flags=re.DOTALL)
    
    # If it is index.html, replace the hero section
    if file == 'index.html':
        content = re.sub(r'<!-- HERO SECTION -->.*?</section>', hero_html, content, flags=re.DOTALL)

    # Clean up any bad cache busters on style.css
    content = re.sub(r'<link rel="stylesheet".*?href="style\.css.*?>', '<link rel="stylesheet" href="style.css">', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied perfect Figma recovery!")
