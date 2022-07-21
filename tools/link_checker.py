# import OS
import os

exceptions = [
    "data.py",
    "helpers.py",
]

with open("README.md") as rdm:
    md = rdm.read()
    for filename in os.listdir(os.getcwd() + "/leetcode"):
        if filename.endswith(".py"):
            if filename not in exceptions and filename not in md:
                print(f"\033[91m» Missing from README.md \033[93m{filename}")
