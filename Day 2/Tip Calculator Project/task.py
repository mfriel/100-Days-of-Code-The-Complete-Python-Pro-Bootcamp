print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? €"))
tip = int(input("What percentage tip would you like to give, 10, 12 or 15? "))
tip = (tip/100)+1
people = int(input("How many people to split the bill? "))
final_bill = round(((bill/people)*tip), 2)

# print(round(((bill/people)*tip), 2))

print(f"Each person should pay €{final_bill}")
