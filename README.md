# Subdomain Scanner 200OK

🔍 A Python-based terminal tool to fetch subdomains from public sources (Wayback Machine, crt.sh, VirusTotal) and check if they return **200 OK**.

## Features

- Collects subdomains from:
  - Wayback Machine
  - crt.sh
  - VirusTotal (API Key required)
- Checks each subdomain for HTTP 200 OK status
- CLI-based and simple to use

## Usage

python3 subdomain_scanner.py example.com -k <VirusTotal-API-Key>


# subdomain-scanner200OK
-subdomain scanner which checks from crt.sh waybackMashine and virustotal(need API key) and checks if 200OK

This is a Subdomain Scanner which get subs from wayback, crt and virustotal(need API key).

It will check if 200OK so you dont need to. have fun.

1.Download.

2.python --version is needed 

3.cd /path/to/files.

4.run in terminal: python3 subdomain_scanner.py <example.com> -k <your-api-key>
