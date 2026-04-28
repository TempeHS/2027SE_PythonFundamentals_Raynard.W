from datetime import date
import inflect

p = inflect.engine()


def main():
    dob = get_Date()
    minuteS = minutes(dob)
    mWord = min_Word(minuteS)
    print(f"{mWord} minutes")


def get_Date():
    dob_text = input("Date of birth").strip()
    try:
        dob = date.fromisoformat(dob_text)
        return dob
    except ValueError:
        raise SystemExit("Invalid date")


def minutes(dob):
    today = date.today()
    difference = today - dob
    minutes = difference.days * 24 * 60
    return minutes


def min_Word(minutes):
    return p.number_to_words(minutes, andword="").capitalize()


if __name__ == "__main__":
    main()
