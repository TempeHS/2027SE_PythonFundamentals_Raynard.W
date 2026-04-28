import sys


def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except ValueError, ZeroDivisionError:
            continue

def convert(fracrtion):
    try:
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)
    except ValueError:
        raise ValueError ("x and y must be integers")

    if y == 0:
        raise ZeroDivisionError("Y cannot be 0")
    if x > y:
        raise ValueError("x cannot be greater than y")

    return round(x/y * 100)

def gauge(percentage):
    if percentage <= 1:
        return"E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()





