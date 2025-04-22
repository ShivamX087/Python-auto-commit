import datetime

now = datetime.datetime.now()
print(now)

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond

print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Second: {second}")
print(f"Microsecond: {microsecond}")

# To get the day of the week
day_name = now.strftime("%A") # Full weekday name
print(f"Day of the week: {day_name}")
