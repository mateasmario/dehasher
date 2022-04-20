import pyfiglet
import os
from termcolor import colored

def Title():
    word = pyfiglet.figlet_format("DEHASHER")
    print (colored(word, 'yellow'))

def Version():
    with open("CurrentVersion") as f:
        version = f.read()
    print("Current version: " + version)

def Description():
    print(colored("Main Description", "yellow"))
    with open(os.path.join("splash", "description"), "r") as f:
        print(f.read())

def Dependencies():
    print(colored("Dependencies", "yellow"))
    print("In order to be used, the following modules need to be installed:")
    with open("requirements", "r", encoding='utf-8-sig', errors="ignore") as f:
        content = f.read().splitlines()
        for ln in content:
            # 'pip freeze > requirements.txt' will add some nasty newlines between the dependencies, and we're just trying to NOT print them >:(
            if "=" in ln:
                print(ln)
    print("These dependencies can be easily installed using a package manager like pip, directly from the already provided requirements file: 'pip install -r requirements'")

def Usage():
    print(colored("Usage", "yellow"))
    print("Type in the MD5 hash of the text you want to decrypt, and wait for the magic to happen...")
    print("")

def ClearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
