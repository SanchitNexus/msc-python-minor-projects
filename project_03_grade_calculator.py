# Student Grade Calculator

# Take marks for 3 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Calculate total and percentage
total = sub1 + sub2 + sub3
percentage = total / 3

print(f"\nTotal Marks: {total}/300")
print(f"Percentage: {percentage:.2f}%")

# Determine grade based on percentage
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: F (Fail)")
