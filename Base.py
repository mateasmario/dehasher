import GenerateSpecificLengthStrings
from multiprocessing import Process
import os
import time

def clean():
    file = os.path.join("temp", "result")
    if (os.path.exists(file)):
        os.remove(file)

def main():
    variant = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+{}[]:\";'|\\<>,.?/~ "

    word = input(">>> ")

    method = ""

    if len(word) == 128:
        method = "SHA512"
    elif len(word) == 96:
        method = "SHA384"
    elif len(word) == 64:
        method = "SHA256"
    elif len(word) == 56:
        method = "SHA224"
    elif len(word) == 40:
        method = "SHA1"
    elif len(word) == 32:
        method = "MD5"
    else:
        print("[ERROR] No hashing method identified.")
        exit(1)
    print("[INFO] Identified " + method + " hashing.")

    processes = []

    for length in range(1, 9, 2):
        proc = Process(target=GenerateSpecificLengthStrings.doTwice, args=(method, word, length, length+1, chars))
        processes.append(proc)
        proc.start()

    while True:
        if (os.path.exists(os.path.join("temp", "result"))):
            # kill all processes
            for proc in processes:
                proc.kill()
            break
        time.sleep(2)
