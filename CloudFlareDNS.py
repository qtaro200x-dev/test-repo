import requests

API_TOKEN = "v1br5a7vdcfUwxNhQH3WfYHZs_BmMk7OO6ue0WDb"
ZONE_ID = "936830c18137e5457a1a3758bac24502"

def test():
    print("Testing CloudFlare DNS script...")

def test2():
    print("Testing CloudFlare DNS script...")

def format_ttl(ttl):
    if ttl == 1:
        return "auto"
    elif ttl < 60:
        return f"{ttl} sec"
    elif ttl < 3600:
        return f"{ttl // 60} min"
    else:
        return f"{ttl // 3600} hour"

def list_dns_records():
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return

    data = response.json()

    with open("dns_output.txt", "w", encoding="utf-8") as f:
        f.write("=== DNS Records ===\n")

        for record in data.get("result", []):
            ttl_human = format_ttl(record["ttl"])
            line = f"{record['type']} {record['name']} -> {record['content']} (TTL: {ttl_human})"
            print(line)
            f.write(line + "\n")

if __name__ == "__main__":
    list_dns_records()
