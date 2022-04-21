import pyfiglet
import os
import utils.Versioning
from termcolor import colored

def Title():
    word = pyfiglet.figlet_format("DEHASHER")
    print (colored(word, 'yellow'))

def Version():
    version = utils.Versioning.GetVersion()
    print("Current version: " + version)

def Description():
    print(colored("Main Description", "yellow"))
    with open(os.path.join("splash", "Description"), "r") as f:
        print(f.read() + "\n")

def Dependencies():
    print(colored("Dependencies", "yellow"))
    print("In order to be used, the following modules need to be installed: termcolor, pyfiglet, requests")
    print("These dependencies can be easily installed using a package manager like pip, directly from the already provided requirements file: 'pip install -r requirements'\n")

def Usage():
    print(colored("Usage", "yellow"))
    with open(os.path.join("splash", "Usage"), "r") as f:
        print(f.read() + "\n")

def ClearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
