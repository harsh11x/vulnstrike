import os
import argparse
from scanner import sql_injection, xss, csrf, directory_traversal, rce, subdomain_enum
from scanner.utils import sanitize_url
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def generate_report(scan_results, output_file):
    from fpdf import FPDF  # Ensure fpdf is imported here for report generation
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Vulnerability Scan Report", ln=True, align='C')

    for scan_type, results in scan_results.items():
        pdf.cell(200, 10, txt=scan_type, ln=True)
        if results:
            for result in results:
                pdf.cell(200, 10, txt=f" - {result}", ln=True)
        else:
            pdf.cell(200, 10, txt=" - No vulnerabilities found.", ln=True)

    pdf.output(output_file)
    print(f"Report saved as {output_file}")

def main():
    print(Fore.LIGHTBLUE_EX + "Developed by Harsh Dev")
    print(Fore.LIGHTBLUE_EX + "GitHub: harsh11x")
    
    url = input(Fore.WHITE + "Enter the website URL to scan: ")
    
    print(Fore.GREEN + "Select the scan mode:")
    modes = {
        "1": "full",
        "2": "sql_injection",
        "3": "xss",
        "4": "csrf",
        "5": "rce"
    }
    
    for key, mode in modes.items():
        print(Fore.GREEN + f"{key}. {mode.replace('_', ' ').capitalize()}")

    mode_choice = input(Fore.WHITE + "Type the number of your choice: ")
    selected_mode = modes.get(mode_choice)

    # Validate the mode selection
    if selected_mode is None:
        print(Fore.RED + "Invalid selection. Exiting.")
        return

    # Set up proxy input
    proxy = input(Fore.WHITE + "Enter proxy URL (or leave blank if none): ") or None

    scan_results = {}

    if selected_mode == 'full':
        scan_results['SQL Injection'] = sql_injection.detect_sql_injection(url, proxy)
        scan_results['XSS'] = xss.detect_xss(url, proxy)
        scan_results['CSRF'] = csrf.detect_csrf(url, proxy)
        scan_results['Directory Traversal'] = directory_traversal.detect_directory_traversal(url, proxy)
        scan_results['RCE'] = rce.detect_rce(url, proxy)
        scan_results['Subdomain Enumeration'] = subdomain_enum.detect_subdomains(url)

    else:
        scan_mapping = {
            'sql_injection': sql_injection.detect_sql_injection,
            'xss': xss.detect_xss,
            'csrf': csrf.detect_csrf,
            'rce': rce.detect_rce
        }
        scan_results[selected_mode.capitalize()] = scan_mapping[selected_mode](url, proxy)

    # Check and print scan results for debugging
    print("Scan Results:", scan_results)  # Debugging line to check the contents of scan_results

    # Construct the path to the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "report.pdf")

    # Generate report
    generate_report(scan_results, desktop_path)
    print(Fore.WHITE + f"Scan completed! Report generated at {desktop_path}")

if __name__ == "__main__":
    main()
