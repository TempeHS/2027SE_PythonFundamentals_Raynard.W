def main():
    phrase = input("What's your phrase")
    print(shorten(phrase))


def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in word:
        if ch not in vowels:
            result += ch
        return result


if __name__ == "__main__":
    main()
