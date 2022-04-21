# Dehasher
### Main description
This is a (probably inefficient - but still working on it) "dehasher" tool that looks through all the word combinations possible, hashes them and outputs the raw word that has the same hash as the given input.  
Dehashing works on the following hashing methods: **MD5**, **SHA1**, **SHA224**, **SHA256**, **SHA384** and **SHA512**.

The dehasher uses Python's hashlib module. More info can be found at https://docs.python.org/3/library/hashlib.html.  
For any questions or suggestions, feel free to send an e-mail at mateasmario@aol.com.
### Requirements
1. [Python](https://www.python.org/) - Last version is recommended
2. [pip](https://pypi.org/project/pip/) - Usually comes together with Python

Make sure they are properly installed by typing in your terminal:
```
python --version
pip --version
```

### Installation
1. Dehasher is a Python script. So make sure you install Python (and all the other dependencies) from the above section.
2. Take the source code from GitHub (either download it or `git clone`)
3. It is recommended to create a virtual environment in Python, because you'll need to install some pip modules.
4. The code also comes with a file called `requirements`, that contains all the pip modules needed, together with their versions. Run `pip install -r requirements` in the same folder as the source code, in order to install them.
5. You're set up! Try running the script using `py run.py`, in order to check if something's still missing.

### Usage
#### Dehashing your input
Firstly, open a terminal and navigate to the root folder of the source code. Then, run the script using `py run.py`.
Type in a hashed text you want to decrypt, and wait for the magic to happen. The script automatically identifies the hashing method, based on the input's length.
#### Multiprocessing
In order to improve the overall speed of the script, Dehasher uses **multiprocessing**, meaning that it is going to handle two possible text length values on each process, creating a total of 4 processes. First process will try and find a possible hash for lengths (1, 2), the second one for (3, 4), and so on.  
Dehasher is going to automatically kill all its child processes, after finding a match.  
#### Waiting too much for a dehashing?
If you feel like waiting too much for a dehashing, **terminate** the main process by pressing `CTRL` + `C`.
