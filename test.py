from datetime import datetime

data = input("Enter time with ':'")
hours, minutes = map(int, data.split(':'))
print("minutes: ", minutes)
print("hours: ", hours)