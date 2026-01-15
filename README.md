ZIP Password Brute-Force (Lowercase Letters Only)
📌 Description

This Python script attempts to recover the password of a ZIP file by performing a brute-force attack using lowercase letters only (a–z).
It systematically tries every possible combination within a user-defined password length range until the correct password is found or all possibilities are exhausted.

⚠️ Important:
This tool is intended strictly for educational purposes and authorized security testing only, such as:

Recovering your own ZIP files

Learning how brute-force attacks work

Practicing cybersecurity concepts in a legal lab environment

Do NOT use this script on files you do not own or have explicit permission to test.

🧠 How It Works

Uses pyzipper to handle encrypted ZIP files (including AES-encrypted ZIPs)

Generates password combinations using:

itertools.product

Lowercase English letters only (a–z)

Tries passwords from a minimum length to a maximum length

Stops immediately when the correct password is found

Displays:

Current attempt count

Total possible combinations

Time taken

🛠️ Requirements
Python Version

Python 3.7+

Required Libraries

Install dependencies using pip:

pip install pyzipper


(Standard libraries like itertools, string, and time are included with Python.)

▶️ Usage

Save the script as, for example:

zip_bruteforce_letters.py


Run the script:

python zip_bruteforce_letters.py


When prompted, enter:

ZIP file path

Minimum password length

Maximum password length

Example Input
Enter ZIP file path (e.g., cracker.zip): secret.zip
Enter MIN password length (e.g., 1): 1
Enter MAX password length (e.g., 6): 4

📤 Output Example
[🔍] Trying lowercase letters | Length: 3
[+] Possibilities: 17576
[1240/17576] Trying: cat

✅ PASSWORD FOUND: cat

⏱️ Time taken: 3.42 seconds


If no password is found:

[🔒] Password not found.

⚙️ Configuration Details

Character set:

abcdefghijklmnopqrstuvwxyz


Attack type:
Brute force (exhaustive search)

ZIP type supported:
Standard ZIP and AES-encrypted ZIP files

🚀 Performance Notes

Time increases exponentially with password length

Example number of combinations:

Length 4 → 26⁴ = 456,976

Length 6 → 26⁶ = 308,915,776

For larger lengths, expect very long runtimes.

🔐 Ethical & Legal Notice

This script is for:

Learning cybersecurity concepts

Password recovery on your own files

Authorized penetration testing labs (CTFs, practice environments)

❌ Illegal use is strictly prohibited.
You are fully responsible for how you use this code.

📚 Learning Goals

By studying this script, you can learn:

How brute-force attacks work

Why strong passwords matter

How ZIP encryption validation behaves

Python iteration and exception handling

Real-world security limitations

🧩 Possible Improvements

Add uppercase letters and numbers

Support custom wordlists

Multithreading for speed

Resume attack from last position

Progress bar instead of terminal overwrite

👤 Author

Created for educational cybersecurity practice and learning.
