import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    validate_paths(input_file, output_file)
    apply_shirt_overlay(input_file, output_file)

    try:
        with Image.open(input_path) as input_img:
            shirt = Image.open("shirt.png")
            size = shirt.size
    
except FileNotFoundError:
    sys.exit("Does not exist")

if __name__ == "__main__":
    main()