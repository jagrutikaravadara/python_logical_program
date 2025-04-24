from datetime import datetime

# Get input from user
date1 = input("Enter your birthdate (dd-mm-yyyy): ")
date2 = input("Enter today's date (dd-mm-yyyy): ")

# Convert input strings to datetime objects
d1 = datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.strptime(date2, "%d-%m-%Y")

# Calculate difference in days
difference = (d2 - d1).days

# Output the result
print("You have lived for", difference, "days.")
