import random
import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        chosefont = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1]
    chosenfont = sys.argv[2]
    if chosefont not in fonts:
        sys.exit("Invalid usage")
    text = input("Input: ")
    print("Output:")
main()