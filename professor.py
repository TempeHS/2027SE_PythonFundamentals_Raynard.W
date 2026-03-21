import random
def main():
    level = get_level()
    score = 0

        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
    
set tries = 0
while tries < 3:
    try:
        guess = int(input(f"{x} + {y} = "))
        if correct, add to score
    break
        if wrong, print("EEE")
print(f"Score : {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError

def generate_integer():
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randit(10, 99)
    else:
        returnn random.randint(100, 999)

if name == "main":
    main()