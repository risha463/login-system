import hashlib
def make_hash(paswo):
    return hashlib.sha256(paswo.encode()).hexdigest()
df={}
u=input("Create username")
if  u=="":
    print("user name can't be empty")
elif  len(u)<5:
    print("username is to short")
elif u in df:
    print("user name  is already exist")
elif "--" in u or "'" in u:
    print("suspicious username") 
elif not (any(c.isupper() for c in u) and
          any(c.islower() for c in u) and
          any(c.isdigit() for c in u)):
 print("Username not valid ❌")
 print("Must contain uppercase, lowercase and digit")
else:
     print("username valid ")
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
        attempts=0
        while attempts<3:  
             lu = input("Enter username: ")
             lp = input("Enter password: ")

             if lu in df and df[lu] == make_hash(lp):
              print("Login successful ✅")
              break
             else:
              attempts+=1
              print("Invalid login ❌")
             if attempts==3:
               print('Block user')
         
     else:
        print("Weak password ❌")
        print("Password must contain:")
        print("- At least 8 characters")
        print("- Uppercase, lowercase, number")
        print("- Special character (#$%)")