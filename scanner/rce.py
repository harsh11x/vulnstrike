import requests

def detect_rce(url, payloads=None, proxy=None, timeout=5):
    if payloads is None:
        payloads = ["; echo test", "; id", "; ls"]

    headers = {'User-Agent': 'Mozilla/5.0'}
    results = []

    for payload in payloads:
        try:
            rce_url = f"{url}?cmd={payload}"
            proxies = {"http": proxy, "https": proxy} if proxy else None
            response = requests.get(rce_url, headers=headers, proxies=proxies, timeout=timeout)

            if "test" in response.text or "uid" in response.text or "ls" in response.text:
                results.append(f"Possible RCE vulnerability detected with payload: {payload}")
        except requests.RequestException as e:
            results.append(f"Error during RCE test with payload '{payload}': {str(e)}")

    return results if results else ["No RCE vulnerabilities detected."]
