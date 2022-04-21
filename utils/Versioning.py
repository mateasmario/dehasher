import requests
from termcolor import colored

def GetVersion() -> str:
    with open("CurrentVersion") as f:
        return f.read()

def CheckVersion():
    response = requests.get('https://raw.githubusercontent.com/mateasmario/dehasher/main/CurrentVersion')
    content = response.content
    content = str(content)
    content = content.replace('b', '')
    content = content.replace('\'', '')
    content = content.replace('\\n', '')
    content = content.strip()

    if content != GetVersion().strip():
        print(colored("New version " + content + " is now available!", "green"))
        print("Update by git pulling/cloning from https://github.com/mateasmario/dehasher")
        print("")
