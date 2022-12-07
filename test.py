# Remove last commit by using: git reset --soft HEAD^

import github
from github import Github
import os
import sys
from datetime import date
g = github.Github(os.getenv ("GITHUB_TOKEN"))
repo = g.get_repo("PatrikEdelenji/git-hooks")
branch = repo.get_branch ("main")

header = """/*
         ===========================================================
         HEADER

         Author: {author}

         Date: {date}

         Description: {description}

         ===========================================================
*/
         """


today = date.today()
d1 = today.strftime("%d/%m/%Y")

# prints all files that are in sql format


def checkFiles():

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    txt = "This is the file {something}: "
    # print(txt.format(something=files))
    for f in files:
        if f.endswith('.sql'):
            print(f)
            readFile(f)


def readFile(fileName):
    with open(fileName, 'r') as f:
        sqlquery = f.read()
        # print(sqlquery)
        f.close()
        fillHeader(fileName, sqlquery)


# inputs are thrown into the string using formatter


def fillHeader(fileName, sqlquery):

    # author = input("Enter your name: ")
    # date = input("Enter date of creation: ")
    # description = input("Short summary of current query: ")

    # sys.stdin = open("COM1:")
    author = branch.commit.author.login
    date = d1
    description = "This is sql file"
    # print(header.format(author=author, date=date, description=description))
    changedHeader = header.format(author = author, date = date, description = description)
    editFile(fileName, sqlquery, changedHeader)


def editFile(fileName, sqlquery, changedHeader):
    with open(fileName, 'w') as f:
        
        formated = changedHeader + "\n" + sqlquery

        print("FORMATED:\n\n " + formated + "\n\n")
        f.write(formated)
        f.close()


checkFiles()
