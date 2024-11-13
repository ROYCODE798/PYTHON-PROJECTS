import os
import subprocess
import sys
import socket
import re

# Function to check if nmap is installed
def check_nmap_installed():
    try:
        subprocess.run(["nmap", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("Error: Nmap is not installed. Please install Nmap to continue.")
        sys.exit(1)

# Function to validate the target (IP or domain)
def is_valid_target(target):
    # Check if the target is a valid IP address or domain
    ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    domain_pattern = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"

    if re.match(ip_pattern, target):  # If it's a valid IP address
        return True
    elif re.match(domain_pattern, target):  # If it's a valid domain name
        return True
    else:
        return False

# Function to run the Nmap scan
def nmap_scan(target, scan_type):
    print(f"\nStarting {scan_type} scan on {target}...\n")

    # Define the Nmap command based on the scan type
    if scan_type == "1":
        command = f"nmap -sS {target}"  # SYN Scan (requires root)
    elif scan_type == "2":
        command = f"nmap -sT {target}"  # TCP Connect Scan
    elif scan_type == "3":
        command = f"nmap -sU {target}"  # UDP Scan
    elif scan_type == "4":
        command = f"nmap -sV {target}"  # Version Detection
    elif scan_type == "5":
        command = f"nmap -O {target}"   # OS Detection
    elif scan_type == "6":
        command = f"nmap -A {target}"   # Aggressive Scan (OS detection + version detection + script scan + traceroute)
    elif scan_type == "7":
        command = f"nmap -Pn {target}"  # No Ping Scan
    else:
        print("Invalid scan type selected.")
        return

    try:
        # Run the chosen Nmap command using subprocess
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())  # Output the scan result
    except subprocess.CalledProcessError as e:
        print(f"Error during scan: {e.stderr.decode()}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function
def main():
    check_nmap_installed()  # Ensure Nmap is installed

    target = input("Enter the target IP or domain for the Nmap scan: ").strip()

    # Validate the target IP/domain
    if not is_valid_target(target):
        print("Error: Invalid IP address or domain.")
        return

    # Display scan type options to the user
    print("\nSelect the type of Nmap scan to perform:")
    print("1. SYN Scan (Stealth Scan)")
    print("2. TCP Connect Scan")
    print("3. UDP Scan")
    print("4. Version Detection")
    print("5. OS Detection")
    print("6. Aggressive Scan")
    print("7. No Ping Scan")

    scan_type = input("Enter the scan type number (1-7): ").strip()

    # Validate scan type input
    if scan_type not in {"1", "2", "3", "4", "5", "6", "7"}:
        print("Error: Invalid scan type selected.")
        return

    # Run the scan
    nmap_scan(target, scan_type)

if __name__ == "__main__":
    main()
