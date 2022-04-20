import hashlib
import Increment
import os

def encrypt(method, possibility) -> str:
    if method == "MD5":
        return hashlib.md5(str.encode(possibility)).hexdigest()
    elif method == "SHA1":
        return hashlib.sha1(str.encode(possibility)).hexdigest()
    elif method == "SHA224":
        return hashlib.sha224(str.encode(possibility)).hexdigest()
    elif method == "SHA256":
        return hashlib.sha256(str.encode(possibility)).hexdigest()
    elif method == "SHA384":
        return hashlib.sha384(str.encode(possibility)).hexdigest()
    elif method == "SHA512":
        return hashlib.sha512(str.encode(possibility)).hexdigest()

def do(method, word, length, chars) -> bool:
    found = False

    possibility = ""
    finalPossibility = ""

    for i in range(0, length):
        finalPossibility += chars[-1]
        possibility += chars[0]

    if encrypt(method, possibility) == word:
        print("[SUCCESS] Found match: " + possibility)
        with open(os.path.join("temp", "result"), "w") as f:
            pass
        found = True
        return found

    while encrypt(method, possibility) != word:
        possibility = Increment.do(possibility, chars)
        if encrypt(method, possibility) == word:
            print("[SUCCESS] Found match: " + possibility)
            with open(os.path.join("temp", "result"), "w") as f:
                pass
            found = True
            return found
        elif possibility == finalPossibility:
            print("[INFO] Found no result for length " + str(length) + ".")
            return found


def doTwice(method, word, length1, length2, chars) -> bool:
    if do(method, word, length1, chars) == True or do(method, word, length2, chars) == True:
        return True
    return False
