import hashlib
import os
import itertools
import time
from termcolor import colored

def Identify(word) -> str:
    if len(word) == 128:
        return "SHA512"
    elif len(word) == 96:
        return "SHA384"
    elif len(word) == 64:
        return "SHA256"
    elif len(word) == 56:
        return "SHA224"
    elif len(word) == 40:
        return "SHA1"
    elif len(word) == 32:
        return "MD5"
    else:
        return None

def Hash(method, possibility) -> str:
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

def Generate(method, word, length, chars) -> bool:
    start_time = time.time()
    found = False
    possibility = ""
    finalPossibility = ""

    for i in range(0, length):
        finalPossibility += chars[len(chars)-1]

    ranges = []

    for i in range(0, length):
        ranges.append(range(0, len(chars)))

    for xs in itertools.product(*ranges):
        if found == True:
            break
        possibility = ""
        for i in range(0, length):
            possibility += chars[xs[i]]
        if Hash(method, possibility) == word:
            finish_time = time.time()
            print(colored("[INFO] Found match: " + possibility + "\n[INFO] Finish time: " + str(finish_time - start_time) + " seconds", "green"))
            with open(os.path.join("temp", "result"), "w") as f:
                pass
            found = True
            return found
        if (possibility == finalPossibility):
            print("[INFO] Didn't find any match with length " + str(length) + ".")
            return False

def GenerateTwoLengths(method, word, length1, length2, chars) -> bool:
    if Generate(method, word, length1, chars) == True or Generate(method, word, length2, chars) == True:
        return True
    return False
