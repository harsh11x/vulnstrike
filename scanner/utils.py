# scanner/utils.py

import re

def sanitize_url(url):
    # A basic URL sanitizer function
    return re.sub(r'[^\w\s-]', '', url)  # Removes special characters from URL
