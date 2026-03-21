import emoji


def main():
    text = input("Input: ")
    output = emoji.emojize(text, language="alias")
    print(f"{output}")


main()
