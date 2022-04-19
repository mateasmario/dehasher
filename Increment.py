import Reconstruct

def do(possibility, chars) -> str:
    i = 1

    # if possibility characters reached limit and can no longer be incremented, reset them
    while possibility[-i] == chars[len(chars)-1] and i < len(possibility):
        possibility = Reconstruct.do(possibility, len(possibility)-i, chars[0])
        i+=1

    # increment the available possibility character
    char = possibility[len(possibility)-i]
    index = chars.find(char)
    index = index+1
    possibility = Reconstruct.do(possibility, len(possibility)-i, chars[index])

    return possibility
