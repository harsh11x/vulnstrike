import requests

def detect_xss(url, proxy=None, timeout=5):
    payloads = [
        "<script>alert(1)</script>",
        "<img src='x' onerror='alert(1)'>",
        "<body onload=alert(1)>"
    ]
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    results = []

    for payload in payloads:
        try:
            # Constructing URL with XSS payload
            xss_url = f"{url}?q={payload}"
            proxies = {"http": proxy, "https": proxy} if proxy else None
            response = requests.get(xss_url, headers=headers, proxies=proxies, timeout=timeout)
            
            # Detecting if the payload triggers XSS (usually by checking if the payload is reflected)
            if payload in response.text:
                results.append(f"Possible XSS vulnerability detected with payload: {payload}")
        except requests.RequestException as e:
            results.append(f"Error during XSS test with payload '{payload}': {str(e)}")

    return results if results else ["No XSS vulnerabilities detected."]
