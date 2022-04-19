import hashlib

def reconstruct(possibility, position, character) -> str:
    result = ""
    for i in range(0, len(possibility)):
        if i != position:
            result += possibility[i]
        else:
            result += character
    return result

def increment(possibility, chars) -> str:
    i = 1

    # if possibility characters reached limit and can no longer be incremented, reset them
    while possibility[-i] == chars[len(chars)-1] and i < len(possibility):
        possibility = reconstruct(possibility, len(possibility)-i, chars[0])
        i+=1

    # increment the available possibility character
    char = possibility[len(possibility)-i]
    index = chars.find(char)
    index = index+1
    possibility = reconstruct(possibility, len(possibility)-i, chars[index])

    return possibility


def main():
    variant = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+{}[]:\";'|\\<>,.?/~ "

    word = input("Word: ")

    possibility = ""
    finalPossibility = ""

    found = False

    if found == False:
        for length in range(1, 8):
            possibility = ""
            finalPossibility = ""
            if found == True:
                break

            for i in range(0, length):
                finalPossibility += chars[-1]

            for i in range(0, length):
                possibility += chars[0]

            if hashlib.md5(str.encode(possibility)).hexdigest() == word:
                print(possibility)
                found = True
                break

            while hashlib.md5(str.encode(possibility)).hexdigest() != word:
                possibility = increment(possibility, chars)
                if hashlib.md5(str.encode(possibility)).hexdigest() == word:
                    print(possibility)
                    found = True
                    break
                elif possibility == finalPossibility:
                    break

main()
