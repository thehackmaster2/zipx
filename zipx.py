import pyzipper
import itertools
import string
import time
import sys
import os
import webbrowser
import subprocess

CHANNEL_URL = "https://www.youtube.com/@neox_neoxa"

# ===============================
# OPEN URL (PHONE + PC FIX)
# ===============================

def open_youtube(url):
    try:
        # Try Python webbrowser first
        if webbrowser.open(url):
            return
    except:
        pass

    # Android / Termux
    try:
        subprocess.run(["termux-open-url", url], check=True)
        return
    except:
        pass

    # Android intent fallback
    try:
        subprocess.run([
            "am", "start",
            "-a", "android.intent.action.VIEW",
            "-d", url
        ], check=True)
        return
    except:
        pass

    # Linux desktop fallback
    try:
        subprocess.run(["xdg-open", url], check=True)
        return
    except:
        pass

    print("⚠️ Could not auto-open YouTube. Please open manually:")
    print(url)


# ===============================
# SUBSCRIPTION GATE
# ===============================

def subscription_gate():
    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 55)
    print("🔐 ZIP PASSWORD TOOL - SUBSCRIPTION REQUIRED")
    print("=" * 55)
    print("\n📢 Subscribe to unlock this tool:")
    print("👉 https://www.youtube.com/@neox_neoxa\n")

    time.sleep(1)
    print("🌐 Opening YouTube channel...\n")
    open_youtube(CHANNEL_URL)

    print("\nAfter subscribing, type YES to continue.")
    confirm = input("Have you subscribed? (YES/NO): ").strip().lower()

    if confirm != "yes":
        print("\n❌ Access denied.")
        print("⚠️ Subscription required.")
        sys.exit(0)

    print("\n✅ Access granted. Welcome!")
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")


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

            print(f"[{count}/{total}] Trying: {password}", end="\r")

            try:
                zip_file.extractall(pwd=password.encode("utf-8"))
                print(f"\n\n✅ PASSWORD FOUND: {password}")
                return password
            except:
                pass

    print("\n[🔒] Password not found.")
    return None


# ===============================
# MAIN
# ===============================

if __name__ == "__main__":
    subscription_gate()

    zip_file_path = input("Enter ZIP file path (e.g., secret.zip): ").strip()
    min_len_input = input("Enter MIN password length (e.g., 1): ").strip()
    max_len_input = input("Enter MAX password length (e.g., 6): ").strip()

    if not min_len_input.isdigit() or not max_len_input.isdigit():
        print("❌ Password lengths must be numbers.")
        sys.exit(1)

    min_len = int(min_len_input)
    max_len = int(max_len_input)

    start = time.time()
    try_letters_only(zip_file_path, min_len, max_len)
    end = time.time()

    print(f"\n⏱️ Time taken: {end - start:.2f} seconds\n")
