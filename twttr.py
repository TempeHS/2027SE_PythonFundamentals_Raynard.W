text_novowels = input("What's your phrase")
result = ""
vowels = "aeiouAEIOU"
for ch in text_novowels:
    if ch in vowels:
        result += ""
    else:
        result += ch
print(result)
