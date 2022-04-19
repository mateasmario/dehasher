import hashlib
import Increment

def do(word, length, chars) -> bool:
    found = False

    possibility = ""
    finalPossibility = ""

    for i in range(0, length):
        finalPossibility += chars[-1]
        possibility += chars[0]

    if hashlib.md5(str.encode(possibility)).hexdigest() == word:
        print(possibility)
        found = True
        return found

    while hashlib.md5(str.encode(possibility)).hexdigest() != word:
        possibility = Increment.do(possibility, chars)
        if hashlib.md5(str.encode(possibility)).hexdigest() == word:
            print(possibility)
            found = True
            return found
        elif possibility == finalPossibility:
            return found
