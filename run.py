import GenerateSpecificLengthStrings

def main():
    variant = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+{}[]:\";'|\\<>,.?/~ "

    word = input("Word: ")

    found = False

    if found == False:
        for length in range(1, 8):
            res = GenerateSpecificLengthStrings.do(word, length, chars)
            if res == True:
                break

main()
