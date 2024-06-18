age = int(input("Enter you age: "))

total_years_left = 90*365 - age*365
total_weeks_left = 90*52 - age*52
total_months_left = 90*12 - age*12

print(f"Total years left: {total_years_left}, weeks left: {total_weeks_left}, months left: {total_months_left}")