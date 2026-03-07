while True:
    fraction = input("Fraction: ").strip()
    left, right = fraction.split("/")
    x = int(left)
    y = int(right)
    if y == 0 or x > y: raise ValueError
    percent = round((x/y) * 100)
    else print(f"{percent}%")
