Python Failed Login Detection Script

Project Overview

This project is a beginner-level cybersecurity tool developed using Python to analyze authentication logs and identify potentially suspicious login activity.

The script reviews authentication records, identifies failed login attempts, counts failures by IP address, and generates an alert when an IP address reaches the configured failure threshold.

Project Objectives

* Analyze authentication log files.
* Identify failed login attempts.
* Extract IP addresses associated with failed authentication attempts.
* Count failed login attempts by IP address.
* Flag suspicious IP addresses that meet or exceed the alert threshold.

Tools & Technologies

* Python
* Visual Studio Code (VS Code)
* Windows
* Authentication log files

Skills Demonstrated

* Python scripting
* File handling and log parsing
* Dictionaries and conditional logic
* IP address identification
* Basic security monitoring
* Detection of suspicious authentication activity

Sample Results

During testing, the script analyzed simulated authentication records and identified the following activity:

IP Address	Failed Login Attempts	Result
192.0.2.10	8	Alert Triggered
192.0.2.22	2	Below Threshold
192.0.2.31	1	Below Threshold

The script successfully flagged the IP address with eight failed login attempts.

How It Works

1. Opens and reads the authentication log file.
2. Searches for failed login records.
3. Extracts the associated IP addresses.
4. Counts failed attempts for each IP address.
5. Compares the counts against the configured alert threshold.
6. Displays a warning when suspicious activity is detected.

How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Ensure Python is installed.
4. Open the terminal.
5. Run:

python login_detector.py

Project Purpose

This project was created as part of my cybersecurity learning journey to develop practical Python skills and better understand how security analysts identify suspicious authentication activity.

Disclaimer

This project uses simulated authentication log data for educational and portfolio purposes. It demonstrates basic detection logic and is not a replacement for enterprise security monitoring tools or a SIEM platform.
