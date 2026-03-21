import sys
import requests


def main():
    if len(sys.argv) != 2:
    
    try:
        amount = float(sys.argv[1])
    except ValueError:
        
    price = data["bpi"]["USD"]["rate_float"]
    total = amount * price
    print(f"${total:,.4f}")

if name == "main":
    main()
