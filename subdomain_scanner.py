#!/usr/bin/env python3
import requests, json, time, argparse

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

def check_200_ok(url):
    try:
        r = requests.get(url, timeout=5)
        print(f"✅ {url} is UP (200 OK)" if r.status_code==200 else f"❌ {url} returned {r.status_code}")
    except Exception as e:
        print(f"⚠️ {url} error: {e}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("domain", help="Target domain (e.g. example.com)")
    p.add_argument("-k","--apikey", required=True, help="VirusTotal API key")
    args = p.parse_args()

    print("🔍 Fetching subdomains…")
    subs = set()
    subs |= get_subdomains_from_wayback(args.domain)
    subs |= get_subdomains_from_crt_sh(args.domain)
    subs |= get_subdomains_from_virustotal(args.domain, args.apikey)

    if not subs:
        print("⚠️ No subdomains found."); return

    print("\nSubdomains found:")
    for s in subs: print(" -", s)

    print("\n🔍 Checking each for 200 OK (1 s delay)…")
    for s in subs:
        check_200_ok(s)
        time.sleep(1)

if __name__=="__main__":
    main()
