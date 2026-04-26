import sys
import csv


def main():
    if len(sys.argv) < 2:
        sys.exit
    if len(sys.argv) > 2:
        sys.exit


filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Not a csv file")


def read_csv(filename):
    try:
        with open(filename) as file:
            return
    except ValueError:
        sys.exit("file was not found")


def print_table(rows):
    print(rows)
    pass


if __name__ == "__main__":
    main()
