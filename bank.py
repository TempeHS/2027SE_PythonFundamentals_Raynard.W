greeting = input("greeting")
if greeting.startswith("Hello") or greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h") or greeting.startswith("H"):
    print("$20")
else:
    print("$100")
