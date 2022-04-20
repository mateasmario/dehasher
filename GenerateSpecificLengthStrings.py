import hashlib
import Increment
import os

def do(word, length, chars) -> bool:
    found = False

    possibility = ""
    finalPossibility = ""

    for i in range(0, length):
        finalPossibility += chars[-1]
        possibility += chars[0]

    if hashlib.md5(str.encode(possibility)).hexdigest() == word:
        print(possibility)
        with open(os.path.join("temp", "result"), "w") as f:
            pass
        found = True
        return found

    while hashlib.md5(str.encode(possibility)).hexdigest() != word:
        possibility = Increment.do(possibility, chars)
        if hashlib.md5(str.encode(possibility)).hexdigest() == word:
            print(possibility)
            with open(os.path.join("temp", "result"), "w") as f:
                pass
            found = True
            return found
        elif possibility == finalPossibility:
            return found

def doTwice(word, length1, length2, chars) -> bool:
    if do(word, length1, chars) == True or do(word, length2, chars) == True:
        return True
    return False
