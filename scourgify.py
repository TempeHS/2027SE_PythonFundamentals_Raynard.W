import sys
import csv

import sys
import csv


def main():
    if len(sys.argv) < 2:
        sys.exit
    if len(sys.argv) > 2:
        sys.exit


filename = sys.argv[1]

try:
    with open(input_file) as file:
        last, first = row["name"].split(",")
        students.append(
            "first": first,
            "last": last,
            "house": row["house"]
        )
    except ValueError:
        sys.exit("file does not exist")

if __name__ == "__main__":
    main()
