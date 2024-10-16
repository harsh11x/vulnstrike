
# Vulnerability Scanner

## Overview
The Vulnerability Scanner is a powerful tool designed to help security professionals and developers identify potential vulnerabilities in web applications. It supports various scanning modes, including SQL Injection, Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), Remote Code Execution (RCE), and Directory Traversal. The tool generates comprehensive reports to help users understand vulnerabilities and take necessary actions to secure their applications.

## Features
- **Multiple Scan Modes**: Choose between full scans or specific vulnerability checks.
- **PDF Report Generation**: Automatically generates a detailed PDF report of the scan results.
- **Proxy Support**: Option to set up a proxy for the scanning process.

## Requirements
- Python 3.x
- Required packages:
  - `fpdf`
  - `colorama`

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/harsh11x/vulnstrike.git
   ```
   ```bash
   cd vulnerability-scanner
   ```
2. **Install Required Packages**:
   Ensure you have `pip` installed, then run:
   ```bash
   pip3 install -r requirements.txt\
   ```

## Usage
1. **Run the Scanner**:
   ```bash
   python main.py
   ```
2. **Input the Website URL**: Enter the URL of the website you want to scan when prompted.
3. **Select Scan Mode**:
   - Type `1` for a full scan (all vulnerabilities).
   - Type `2` for SQL Injection.
   - Type `3` for XSS.
   - Type `4` for CSRF.
   - Type `5` for RCE.
4. **Set Proxy (optional)**: Enter a proxy URL if needed, or leave it blank for no proxy.
5. **View Results**: The scan will complete, and a report will be generated as `report.pdf` on your desktop.

## Report Format
The generated report will include:
- **Vulnerability Type**: The type of vulnerability detected.
- **Details**: Specific details or examples of vulnerabilities found.
- **Recommendations**: Suggested actions to mitigate the vulnerabilities.

## Author
- **Name**: Harsh Dev
- **GitHub**: [harsh11x](https://github.com/harsh11x)


