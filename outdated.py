dates = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
while True:
    try:
        text = input("Date: ").strip()
if "/" in text:
    month_text, day_text, year_text = text.split("/")
    year = int(year_text)
    month = int(month_text)
    day = int(day_text)
else:
    raise ValueError

print(f"{year}-{month}-{day}")
break

except (ValueError, IndexError)
    continue