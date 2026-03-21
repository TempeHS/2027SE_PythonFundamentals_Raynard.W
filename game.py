import random

def main():
    level = getlevel()
    secret = random.radint(1, level)

    while True:
        try:
            guess = int(input("Guess:"))
            if guess <== 0:
                continue
        except ValueError:
            continue
if guess < secret: print("Too small!")
elif guess > secret: print("Too big!")
else: print("Just Right!")
break

def getlevel():
    while True
    try:
        level = int(input("Level:"))
        if level > 0:
            return level
    except ValueError:
        pass

if name == "main"
main()