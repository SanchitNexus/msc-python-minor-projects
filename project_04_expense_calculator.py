# Simple Expense Calculator

expenses = []
categories = ["Food", "Transport", "Entertainment", "Utilities", "Other"]

print("--- Simple Expense Calculator ---")
for category in categories:
    amount = float(input(f"Enter amount spent on {category}: Rs. "))
    expenses.append(amount)

total_spent = sum(expenses)
highest = max(expenses)

print("\n--- Summary ---")
print(f"Total Expenditure: Rs. {total_spent:.2f}")
print(f"Highest Single Expense: Rs. {highest:.2f}")
