# Student Attendance Calculator

total_classes = int(input("Enter total number of classes held: "))
attended_classes = int(input("Enter number of classes attended: "))

if total_classes <= 0 or attended_classes > total_classes:
    print("Invalid attendance numbers entered.")
else:
    percentage = (attended_classes / total_classes) * 100
    print(f"\nAttendance Percentage: {percentage:.2f}%")
    
    if percentage >= 75:
        print("Status: Eligible for examinations.")
    else:
        print("Status: Shortage of attendance! Minimum 75% required.")
