def do(possibility, position, character) -> str:
    result = ""
    for i in range(0, len(possibility)):
        if i != position:
            result += possibility[i]
        else:
            result += character
    return result
