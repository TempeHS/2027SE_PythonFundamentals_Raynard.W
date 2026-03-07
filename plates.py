def main():
    plate = input("Plate: ").strip()
    print("Valid" if is_valid(plate) else "Invalid")


def is_valid(plate: str):
    if not (2 <= len(plate) <= 6):
        return False


return True
if name == "main":
    main()
