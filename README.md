🔍 Subdomain Scanner 200OK
A fast, Python-based subdomain enumeration tool that fetches subdomains from public data sources and checks which ones respond with HTTP 200 OK. Perfect for bug bounty, penetration testing, and OSINT.

⚙️ Features
✅ Collects subdomains from:

Wayback Machine

crt.sh

VirusTotal (API key required)

🔄 Checks for live subdomains by verifying HTTP 200 OK response

🧰 Simple and lightweight CLI tool

🐍 Written in Python 3 — no heavy dependencies

📦 Installation
Clone the repository:

bash
Kopieren
Bearbeiten
git clone https://github.com/Kaligula1987/subdomain-scanner200OK.git
cd subdomain-scanner200OK
Check your Python version:

bash
Kopieren
Bearbeiten
python3 --version
🚀 Usage
Run the scanner using:

bash
Kopieren
Bearbeiten
python3 subdomain_scanner.py example.com -k
Replace example.com with your target domain.

Use -k to enable VirusTotal API integration.

💡 Note: VirusTotal requires a free API key. Get it here.

📖 Example
css
Kopieren
Bearbeiten
[+] Fetching subdomains from Wayback, crt.sh, and VirusTotal...
[+] Found 42 subdomains
[+] Checking HTTP status for each...
[200] mail.example.com
[200] shop.example.com
🔐 API Key Setup
To use VirusTotal:

Create an account at virustotal.com

Get your API key from your dashboard

Provide it via command line or script configuration

🧠 Why Use Subdomain Scanner 200OK?
Saves time by automating subdomain discovery and liveness checks

Combines multiple data sources into a single scan

Ideal for recon workflows, red teaming, and security assessments

📚 License
MIT License – use freely and responsibly.
