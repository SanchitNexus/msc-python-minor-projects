# Password Strength Checker

password = input("Enter password: ")

has_digit = False
has_upper = False

# Check each character
for char in password:
    if char.isdigit():
        has_digit = True
    elif char.isupper():
        has_upper = True

print("\n--- Password Evaluation ---")
if len(password) >= 8 and has_digit and has_upper:
    print("Password Strength: Strong")
elif len(password) >= 6:
    print("Password Strength: Medium (Consider adding numbers and uppercase letters)")
else:
    print("Password Strength: Weak (Too short)")
