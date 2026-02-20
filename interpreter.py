# user_input = input("Enter expression")
# parts = user_input.split(" ")
# x = int(parts[0])
# y = parts[1]
# z = int(parts[2])

# if y == "+":
# result = x + z
# elif y == "-":
# result = x - z
# elif y == "*":
# result = x * z
# elif y == "/":
# result = x / z
# print(f"{result:.1f}")


expression = input("equation")
result = eval(expression)
print(result)
