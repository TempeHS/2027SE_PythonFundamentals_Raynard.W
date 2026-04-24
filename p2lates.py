def main():
    plate = input("Plate: ").strip()
    print("Valid" if is_valid(plate) else "Invalid")


def is_valid(plate: str):
    if not (2 <= len(plate) <= 6):
        return False
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False


if __name__ == "__main__":
    main()
