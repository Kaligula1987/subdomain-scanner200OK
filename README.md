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

git clone https://github.com/Kaligula1987/subdomain-scanner200OK.git

cd subdomain-scanner200OK
Check your Python version
python3 --version



🚀 Usage
1. Ensure You Have Python 3 Installed
Run:


python3 --version
If not installed, install it:


sudo apt update && sudo apt install python3 python3-pip -y
2. Create and Activate a Virtual Environment (optional but recommended)



python3 -m venv venv
source venv/bin/activate
3. Install Required Packages
You only need requests, so install it:


pip install requests
You can also create a requirements.txt with:



4. Run the Script
Make sure you're in the same folder as subdomain_scanner.py.

Then run:

python3 subdomain_scanner.py example.com -k YOUR_API_KEY

--------Replace example.com with your target domain----------


💡 Note: VirusTotal requires a free API key. Get it here.




📖 Example

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


Have fun its free!!!
https://buymeacoffee.com/lukassimun



📚 License
MIT License – use freely and responsibly.

https://github.com/Kaligula1987/subdomain-scanner200OK

#subdomain #subdomain-scanner #scanner #sub #domains #subdomainscanner #kaligula
