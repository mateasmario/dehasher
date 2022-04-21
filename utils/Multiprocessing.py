import utils.Hashing
from multiprocessing import Process
import os
import time

def Clean():
    file = os.path.join("temp", "result")
    if (os.path.exists(file)):
        os.remove(file)

def CreateProcesses():
    variant = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+{}[]:\";'|\\<>,.?/~ "

    word = input(">>> ")

    method = utils.Hashing.Identify(word)

    if method is None:
        print("[ERROR] No hashing method identified.")
        exit(1)
    print("[INFO] Identified " + method + " hashing.")

    print("[INFO] Starting to look for the matching word. This can take up to a few hours, depending on the length of the word.")

    processes = []

    for length in range(1, 9, 2):
        proc = Process(target=utils.Hashing.GenerateTwoLengths, args=(method, word, length, length+1, chars))
        processes.append(proc)
        proc.start()

    while True:
        if (os.path.exists(os.path.join("temp", "result"))):
            # kill all processes
            for proc in processes:
                proc.kill()
            exit(1)
        time.sleep(2)

    for proc in processes:
        proc.join()
    exit(2)
