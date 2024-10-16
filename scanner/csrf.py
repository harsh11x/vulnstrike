# scanner/csrf.py

import requests

def detect_csrf(url, proxy=None):
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        response = requests.get(url, proxies=proxies)
        
        if "csrf" not in response.text.lower():
            return "Possible CSRF vulnerability detected: No anti-CSRF token found."
        else:
            return "No CSRF vulnerabilities detected."
    except requests.RequestException as e:
        return f"Error checking CSRF: {e}"
