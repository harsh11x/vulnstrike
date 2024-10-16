import requests
import dns.resolver

def detect_subdomains(url, proxy=None):
    # List of common subdomains to check
    subdomains = ["www", "mail", "ftp", "dev", "test", "api", "blog", "secure"]
    base_domain = url.split("//")[-1].split("/")[0]  # Extract base domain from URL
    found_subdomains = []

    for sub in subdomains:
        full_domain = f"{sub}.{base_domain}"
        try:
            # Resolve the subdomain
            answers = dns.resolver.resolve(full_domain, 'A')
            if answers:
                found_subdomains.append(full_domain)
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            continue
        except Exception as e:
            return [f"Error resolving {full_domain}: {str(e)}"]

    return found_subdomains if found_subdomains else ["No subdomains found."]
