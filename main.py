print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill?"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
share = (bill*(1+(tip_percent/100)))/people
share = "{:.2f}".format(share)
print(f"Each person should pay: ${share}")
