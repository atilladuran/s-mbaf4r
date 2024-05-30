# simbaf4r
This project is a tool developed to perform brute force attacks on a given IP address for different services (SSH, FTP, RDP and SMB). Using lists of usernames and passwords, valid credentials on the target system are attempted to be found.

Content of the Project
Connection attempts are made to various services using modules such as paramiko, ftplib, smbprotocol, socket.
Parallel processing is performed using ThreadPoolExecutor.
After receiving the necessary information from the user, username and password combinations are tried for the specified service.
When valid credentials are found, the results are shown as a table on the screen.

# SIMBAF4R - Brute Force Attack Tool

SIMBAF4R is a tool that performs brute force attacks on a given IP address for different services (SSH, FTP, RDP and SMB). Using lists of usernames and passwords, it tries to find valid credentials on the target system.

## Features

- Performs brute force attempts for SSH, FTP, RDP and SMB services.
- Attempts to find valid credentials using username and password lists.
- Speeds up experimentation by using multiple threads.
- Shows valid credentials as a table.

## Requirements

- Python 3.x
- Required Python modules:
  - paramiko
  - ftplib
  - smbprotocol
  - socket
  - concurrent.futures
  - tabulate
  - colorama
  - uuid
  - pyfiglet

## Installation

You can use the following command to install the necessary Python modules:

```bash
pip install paramiko ftplib smbprotocol tabulate colorama pyfiglet
```
## Requirements
Run the tool:
```bash

python simbarf4r.py
```
Enter the IP address, username file and password file.
Select the service you want to try (SSH, FTP, RDP or SMB).
When valid credentials are found, the results will be shown as a table on the screen.


Example Usage
```bash

Enter IP address: 192.168.1.100
Select port to try:
1. SSH (22)
2. FTP (21)
3. RDP (3389)
4. SMB (445)
Enter your choice: 1
Enter username file path: usernames.txt
Enter password file path: passwords.txt
```
