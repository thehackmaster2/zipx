import pyzipper
import itertools
import string
import time

def try_letters_only(zip_path, min_length, max_length):
    charset = string.ascii_lowercase  # Nyuguti nto gusa: abcdefghijklmnopqrstuvwxyz

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
                zip_file.extractall(pwd=password.encode('utf-8'))
                print(f"\n✅ PASSWORD FOUND: {password}")
                return password
            except:
                continue

    print("\n[🔒] Password not found.")
    return None

# === CONFIGURATION ===
zip_file_path = input("Enter ZIP file path (e.g., cracker.zip): ").strip()
min_len_input = input("Enter MIN password length (e.g., 1): ").strip()
max_len_input = input("Enter MAX password length (e.g., 6): ").strip()

# Validate and convert
if not min_len_input.isdigit() or not max_len_input.isdigit():
    print("❌ Lengths must be numbers.")
    exit(1)

min_len = int(min_len_input)
max_len = int(max_len_input)

start = time.time()
try_letters_only(zip_file_path, min_len, max_len)
end = time.time()

print(f"\n⏱️ Time taken: {end - start:.2f} seconds\n")
