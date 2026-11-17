
import re

print("================================")
print("     PASSWORD STRENGTH CHECKER")
print("================================")

password = input("Enter your password: ")
if len(password) < 8:
    print("Password is Weak")
elif not re.search(r"[A-Z]", password):
    print("Add at least one uppercase letter")
elif not re.search(r"[a-z]", password):
    print("Add at least one lowercase letter")
elif not re.search(r"[0-9]", password):
    print("Add at least one number")
elif not re.search(r"[!@#$%^&*]", password):
    print("Add at least one special character")
else:
    print("Password is Strong!")
