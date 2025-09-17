import requests
import urllib3

# ❌ Disabling warnings instead of fixing the root cause
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

USERNAME = "demo"
PASSWORD = "demo"
# ❌ Credentials in URL, HTTP, verify=False
url = f"http://example.com/api?user={USERNAME}&pass={PASSWORD}"

def fetch_data():
    # ❌ verify=False bypasses TLS certificate checks
    r = requests.get(url, verify=False, timeout=2)
    print("Status:", r.status_code)
    print("Body:", r.text[:200])

if __name__ == "__main__":
    fetch_data()