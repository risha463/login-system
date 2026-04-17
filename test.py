import hashlib
import time

def make_hash(paswo):
    return hashlib.sha256(paswo.encode()).hexdigest()

df = {}              # username -> hashed password
attempts = {}        # username -> number of failed attempts
lock_time = {}       # username -> lock expiry timestamp

# --- SIGNUP PHASE ---
u = input("Create username: ")

if u == "":
    print("Username can't be empty")
elif len(u) < 5:
    print("Username is too short")
elif u in df:
    print("Username already exists")
elif "--" in u or "'" in u:
    print("Suspicious username")
elif not (any(c.isupper() for c in u) and
          any(c.islower() for c in u) and
          any(c.isdigit() for c in u)):
    print("Username not valid ❌")
    print("Must contain uppercase, lowercase, and digit")
else:
    print("Username valid ✅")
    p = input("Create password: ")

    # Password validation
    if (len(p) >= 8 and
        any(c.isupper() for c in p) and
        any(c.islower() for c in p) and
        any(c.isdigit() for c in p) and
        any(not c.isalnum() for c in p)):

        print("Strong password ✅")
        df[u] = make_hash(p)
        print("Signup successful")

        # --- LOGIN LOOP ---
        while True:
            lu = input("\nEnter username: ")

            # 🔴 USER EXIST CHECK
            if lu not in df:
                print("User does not exist ❌")

                if lu not in attempts:
                    attempts[lu] = 0
                attempts[lu] += 1
                print(f"Invalid attempt ❌ ({attempts[lu]}/3)")

                if attempts[lu] >= 3:
                    print("⛔ Too many attempts! Account locked for 5 minutes")
                    lock_time[lu] = time.time() + 300
                continue

            # 🔴 LOCK CHECK
            if lu in lock_time:
                if time.time() < lock_time[lu]:
                    print("⛔ Account locked! Try later")
                    continue
                else:
                    del lock_time[lu]
                    attempts[lu] = 0

            # 🔑 Take password
            lp = input("Enter password: ")

            if lu not in attempts:
                attempts[lu] = 0

            # 🔴 LOGIN CHECK
            if lu in df and df[lu] == make_hash(lp):
                print("Login successful ✅")
                attempts[lu] = 0
                break
            else:
                attempts[lu] += 1
                print(f"Invalid login ❌ (Attempt {attempts[lu]}/3)")

                if attempts[lu] >= 3:
                    print("⛔ Too many attempts! Account locked for 5 minutes")
                    lock_time[lu] = time.time() + 300

    else:
        print("Weak password ❌")
        print("Password must contain:")
        print("- At least 8 characters")
        print("- Uppercase, lowercase, number")
        print("- Special character (#$%)")