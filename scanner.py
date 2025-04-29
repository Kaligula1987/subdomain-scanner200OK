#!/usr/bin/env python3

import requests
import json
import time
import argparse

# Function to get subdomains (this will be used by the scan function)
def get_subdomains_from_wayback(domain):
    subdomains = set()
    url = f"http://web.archive.org/cdx/search/cdx?url=*.{domain}&output=json"
    try:
        data = requests.get(url, timeout=10).json()
        for record in data[1:2]:
            original = record[2]
            host = original.split("://",1)[1].split("/",1)[0]
            if host.endswith(domain):
                subdomains.add("http://" + host)
    except Exception as e:
        print(f"⚠️ Wayback error: {e}")
    return subdomains

def get_subdomains_from_crt_sh(domain):
    subdomains = set()
    url = f"https://crt.sh/?q={domain}&output=json"
    try:
        data = requests.get(url, timeout=10).json()
        for entry in data[:1]:
            host = entry["name_value"]
            if host.endswith(domain):
                subdomains.add("http://" + host)
    except Exception as e:
        print(f"⚠️ crt.sh error: {e}")
    return subdomains

def get_subdomains_from_virustotal(domain, api_key):
    subdomains = set()
    url = f"https://www.virustotal.com/api/v3/domains/{domain}/subdomains"
    headers = {"x-apikey": api_key}
    try:
        data = requests.get(url, headers=headers, timeout=10).json()
        for item in data.get("data", []):
            host = item["id"]
            subdomains.add("http://" + host)
    except Exception as e:
        print(f"⚠️ VirusTotal error: {e}")
    return subdomains

# Function to check if subdomain returns 200 OK
def check_200_ok(url):
    try:
        r = requests.get(url, timeout=5)
        return r.status_code == 200
    except Exception as e:
        return False

# Function to scan for working subdomains (returns a list of working subdomains)
def scan_for_200_ok(domain, api_key):
    subs = set()
    subs |= get_subdomains_from_wayback(domain)
    subs |= get_subdomains_from_crt_sh(domain)
    subs |= get_subdomains_from_virustotal(domain, api_key)

    working_subdomains = []
    for subdomain in subs:
        if check_200_ok(subdomain):
            working_subdomains.append(subdomain)

    return working_subdomains

# Function to save results to 'output.txt'
def save_results(working_subdomains):
    with open("output.txt", "w") as f:
        for subdomain in working_subdomains:
            f.write(subdomain + "\n")

# Function to handle the scan when the command is run
def start_scan(domain, api_key):
    print("🔍 Fetching subdomains…")
    try:
        working_subdomains = scan_for_200_ok(domain, api_key)
        if working_subdomains:
            save_results(working_subdomains)  # Save to output.txt
            print("✅ Scan completed! Check 'output.txt' for results.")
        else:
            print("❌ No working subdomains found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {str(e)}")

# Main function to parse arguments and trigger the scan
def main():
    parser = argparse.ArgumentParser(description="Subdomain Scanner")
    parser.add_argument("domain", help="Target domain (e.g. example.com)")
    parser.add_argument("-k", "--apikey", required=True, help="VirusTotal API key")
    args = parser.parse_args()

    # Start the scan
    start_scan(args.domain, args.apikey)

if __name__ == "__main__":
    main()
