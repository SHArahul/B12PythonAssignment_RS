# B12PythonAssignment_RS (part of Python Graded Assignment)
# DevOps Python Scripts

This repository contains Python scripts for common DevOps tasks: password strength validation, CPU usage monitoring, and file backup.

## Q1: Password Strength Checker
Validates password based on:
Minimum 8 characters  
Contains uppercase and lowercase letters  
Includes at least one digit  
Includes at least one special character (e.g., `!@#$%`)

**Run:**
python password_checker.py

**Q2: CPU Usage Monitor**
Continuously monitors CPU usage and alerts if it exceeds a threshold (default: 80%).
Uses the psutil library
Handles runtime errors
Runs until manually stopped

Run:
python cpu_monitor.py

**Q4: File Backup Utility**
Backs up files from a source directory to a destination directory.
Appends a timestamp if a file with the same name exists
Handles missing or invalid paths

Run:
python backup.py /path/to/source /path/to/destination

**Requirements**
**Install dependencies:**
pip install psutil

