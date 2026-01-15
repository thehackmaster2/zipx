import pyzipper
import itertools
import string
import time
import webbrowser
import sys
import os

# ===============================
# SUBSCRIPTION GATE
# ===============================

CHANNEL_URL = "https://www.youtube.com/@neox_neoxa"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def subscription_gate():
    clear_screen()
    print("=" * 50)
    print("🔐 ZIP PASSWORD TOOL - ACCESS REQUIRED")
    print("=" * 50)
    print("\n📢 To use this tool, please SUBSCRIBE to:")
    print("👉 https://www.youtube.com/@neox_neoxa\n")
    print("🌐 Opening YouTube channel now...\n")

    time.sleep(2)
    webbrowser.open(CHANNEL_URL)

    print("\nAfter subscribing, type YES to continue.")
    confirm = input("Have you subscribed? (YES/NO): ").strip().lower()

    if confirm != "yes":
        print("\n❌ Access denied.")
        print("⚠️ Please subscribe to use this tool.")
        sys.exit(0)

    print("\n✅ Access granted. Welcome!")
    time.sleep(1)
    clear_screen()

# ===============================
# ZIP BRUTE FORCE FUNCTION
# ===============================

def try_letters_only(zip_path, min_length, max_length):
    charset = string.ascii_lowercase  # a-z only

    try:
        zip_file = pyzipper.AESZipFile(zip_path)
    except FileNotFoundError:
        print(f"[🚫] ZIP file '{zip_path}' not found.")
        return None

    for password_length in range(min_length, max_length + 1):
        total = len(charset) ** password_length
        print(f"\n[🔍] Trying lowercase letters | Length: {password_length}")
        print(f"[+] Possibilities: {total}")

        count = 0
        for pwd_tuple in itertools.product(charset, repeat=password_length):
            password = ''.join(pwd_tuple)
            count += 1

            print(f"[{count}/{total}] Trying: {password}", end='\r')

            try:
                zip_file.extractall(pwd=password.encode("utf-8"))
                print(f"\n\n✅ PASSWORD FOUND: {password}")
                return password
            except:
                pass

    print("\n[🔒] Password not found.")
    return None

# ===============================
# MAIN PROGRAM
# ===============================

if __name__ == "__main__":
    subscription_gate()

    zip_file_path = input("Enter ZIP file path (e.g., secret.zip): ").strip()
    min_len_input = input("Enter MIN password length (e.g., 1): ").strip()
    max_len_input = input("Enter MAX password length (e.g., 6): ").strip()

    if not min_len_input.isdigit() or not max_len_input.isdigit():
        print("❌ Password lengths must be numbers only.")
        sys.exit(1)

    min_len = int(min_len_input)
    max_len = int(max_len_input)

    start = time.time()
    try_letters_only(zip_file_path, min_len, max_len)
    end = time.time()

    print(f"\n⏱️ Time taken: {end - start:.2f} seconds\n")
