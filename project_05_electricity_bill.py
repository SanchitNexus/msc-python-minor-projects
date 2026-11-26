# Electricity Bill Calculator

units = float(input("Enter electricity units consumed: "))
bill = 0.0

# Calculate tiered slab rates
if units <= 100:
    bill = units * 1.50
elif units <= 200:
    bill = (100 * 1.50) + (units - 100) * 2.50
elif units <= 300:
    bill = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00
else:
    bill = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + (units - 300) * 6.00

# Fixed meter service charge
total_bill = bill + 50.0

print(f"\nElectricity Bill: Rs. {bill:.2f}")
print(f"Fixed Meter Charge: Rs. 50.00")
print(f"Total Amount Payable: Rs. {total_bill:.2f}")
