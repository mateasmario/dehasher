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

    word = input("Input: ")

    found = False

    processes = []

    if found == False:
        for length in range(1, 9, 2):
            proc = Process(target=GenerateSpecificLengthStrings.doTwice, args=(word, length, length+1, chars))
            processes.append(proc)
            proc.start()

    while True:
        if (os.path.exists(os.path.join("temp", "result"))):
            # kill all processes
            for proc in processes:
                proc.kill()
            break
        time.sleep(2)
