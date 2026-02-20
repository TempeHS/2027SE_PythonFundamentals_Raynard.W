name = input("input variable name")
snake = ""
for ch in name:
    if ch.isupper():
        snake += "_" + ch.lower()
    else:
        snake += ch
print(snake)
