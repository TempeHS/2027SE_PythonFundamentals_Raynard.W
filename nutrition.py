Fruitcalories = 
"apple": 90
"banana": 100
"avocado": 250
"strawberry": 15

def main():
    item = input("Item:")
    if item in Fruitcalories:
        print(f"Calories: {Fruitcalories}")
main()

