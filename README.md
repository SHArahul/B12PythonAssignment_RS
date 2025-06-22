# B12PythonAssignment_RS (part of Python Graded Assignment)
# DevOps Python Scripts

This repository contains Python scripts for common DevOps tasks: password strength validation, CPU usage monitoring, and file backup.

| Script | What it Solves |
| ------ | -------------- |
| `Python_passgen.py` | Checks whether a user-supplied password is **strong** (8 chars+, upper & lower case, ≥1 digit, ≥1 special char). |
| `Cpu_monitor.py`    | Continuously monitors system CPU load and **alerts** when it breaches a configurable threshold (default 80 %). |
| `backup.py`         | Backs up every file from a source folder to a destination folder, **timestamping** duplicates so nothing is overwritten. |

---

## 1. Quick-start


# 1. Clone the repository
git clone https://github.com/SHArahul/B12PythonAssignment_RS.git
cd B12PythonAssignment_RS

# 2. (Optional but recommended) create venv
python -m venv .venv && source .venv/bin/activate      # Linux / macOS
# .venv\Scripts\Activate.ps1                            # Windows PowerShell

# 3. Install the only third-party dependency
pip install psutil
psutil is needed only by Cpu_monitor.py.
All other imports are from Python’s standard library.

2. How to run each program
##2.1 Password-Strength Checker Python_passgen.py
python Python_passgen.py
You will be prompted to paste a password; the script prints which criteria are (or are not) met and labels it strong or weak.

Sample Output:
Please enter your password to check its strength and criteria
> MyPass@2025
Your password has uppercase letters.
Your password has lowercase letters.
Your password has 4 digit(s).
Your password has 1 special character(s).
You have a strong password which has atleast eight characters both in upper and lowercase along with atleast one digit and special character.


##2.2 CPU Usage Monitor Cpu_monitor.py
# Optional flag --threshold lets you raise/lower the limit
python Cpu_monitor.py
What happens:

Every second the script prints the current CPU percentage.
If usage ≥ 80 % it prints an Alert! line.
Stop any time with CTRL+C.
Tip: To monitor remotely you can run it inside tmux or redirect output to a log file.

##2.3 Folder-Backup Utility backup.py
python backup.py /path/to/source /path/to/destination
All regular files in source are copied to destination (sub-directories are ignored).

When a filename already exists in the destination, the new copy is renamed:
example.txt ➜ example_20250622_142305.txt (timestamp = YYYYMMDD_HHMMSS).
The script prints one line per file copied.

##3. Repo Structure

B12PythonAssignment_RS/
├─ Python_passgen.py   # Q1 – Password checker
├─ Cpu_monitor.py      # Q2 – CPU monitor
├─ backup.py           # Q4 – File backup tool
├─ .gitignore
└─ README.md           # (you are here)
---
Screenshot of output:
Cpu_monitor.py:
![cpu-monitoring](https://github.com/user-attachments/assets/ed8b68a5-baad-4c03-95ef-3a383109814b)

Python backup Script:
![backup script python](https://github.com/user-attachments/assets/b617a6c9-8d80-4f7f-847c-bf57559b2034)
![image](https://github.com/user-attachments/assets/35c23b61-2ada-46ad-8eec-0286b95875c9)


Password strength check:
![passwordcheck](https://github.com/user-attachments/assets/eb97dd34-7716-4ed8-8a0b-0868532f8333)


---
##4. Tested Environment
Component	Version
Python	3.10 – 3.12
psutil	≥ 5.9.0
OS	Windows 10/11, Ubuntu 22.04 LTS

Scripts are cross-platform; only psutil hides the OS-specific CPU details.

##5. Contributing
Feel free to fork the repo and open pull requests.
Author: Rahul Sharma

