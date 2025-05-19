import os, sys, time, json, urllib.request
from datetime import datetime
from rich.progress import track
from time import sleep

# File & URL Settings
approval_url = "https://github.com/Drindaw/updated
key_file = ".MR_WALEED_saved_key"

# Line Divider
def linex():
    print("\033[1;97m" + "--" * 50)

# Slow Type Input
def slow_input(text):
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.03)
    return input()

# Load Approval Keys
def load_approvals():
    try:
        with urllib.request.urlopen(approval_url) as res:
            return json.loads(res.read().decode()).get("keys", {})
    except:
        print("[x] Approval loading failed.")
        return {}

# Validate Key
def verify_key(key, approvals):
    if key in approvals:
        exp = approvals[key]['expiry']
        join = approvals[key]['joined']
        today = datetime.today().date()
        exp_date = datetime.strptime(exp, "%Y-%m-%d").date()
        if today <= exp_date:
            return True, join, exp
    return False, None, None

# Save Key
def save_key(key):
    with open(key_file, 'w') as f:
        f.write(key)

# Read Saved Key
def read_key():
    if os.path.exists(key_file):
        return open(key_file).read().strip()
    return None

# Loading Text
def loading(text):
    print(text)

# Menu
def menu(joined, expiry):
    banner()
    print(f"\033[1;97m[✓] Key Verified Successfully!")
    print(f"[✓] Joined On : \033[1;92m{joined}")
    print(f"\033[1;97m[✓] Expiry    : \033[1;91m{expiry}")
    linex()
    print("\033[1;97m[1] Start Cracking")
    print("[2] Update Tool")
    print("[3] Remove Key")
    print("[0] Exit")
    linex()
    
    choice = input("\033[1;97m[?] Select Option: ")
    if choice == "1":
        print("[✓] Starting cracking module...")
    elif choice == "2":
        print("[✓] Update logic coming soon!")
    elif choice == "3":
        os.remove(key_file)
        print("[✓] Key removed. Restarting...")
        time.sleep(1)
        main()
    elif choice == "0":
        print("[✓] Bye!")
        exit()
    else:
        print("[x] Invalid option.")
        time.sleep(1)
        menu(joined, expiry)

# Main Logic
def main():
    banner()
    approvals = load_approvals()
    saved = read_key()
    if saved:
        valid, joined, expiry = verify_key(saved, approvals)
        if valid:
            return menu(joined, expiry)

    key = slow_input("[?] Enter your key: ").strip()
    loading("[✓] Verifying → ")
    valid, joined, expiry = verify_key(key, approvals)
    if valid:
        save_key(key)
        print("[✓] Key Approved and Saved!")
        time.sleep(1)
        return menu(joined, expiry)
    else:
        print("[x] Invalid or Expired Key.")
        exit()

# Banner (Add your custom ASCII banner here if you like)
def banner():
    linex()
    print("        MR WALEED TOOL | KEY VERIFICATION SYSTEM")
    linex()

if __name__ == "__main__":
    main()