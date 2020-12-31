print("Welcome to the tip calculator!")

# Ask user for total bill
bill = float(input(f"What was the total bill?\n"))

#Ask user to imput tip percentage
tip = float(input(f"What percentage tip would you like to give?\n"))

# Ask user how many people will split the bill
people_count = int(input(f"How many people to split bill\n"))

# Calculate total for per each person
# Get tip as a percent
tip_percentage = tip/100

# Get tip amoount
tip_amount = bill * tip_percentage

# Get total bill
total_bill = bill + tip_amount

# Get per person total rounding by two decimal places
person_total = round(total_bill/ people_count, 2)

# Print total for each person
print(f"Each person should pay:  ${person_total}")
