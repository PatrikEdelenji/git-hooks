#!/bin/python

# Remove last commit by using: git reset --soft HEAD^


import os
import sys
from datetime import date

header = """/*
         ===========================================================
         HEADER

         Author: {author}

         Date: {date}

         Description: {description}

         ===========================================================
*/
         """

console_output = """
===========================================================
PRE COMMIT MESSAGE
===========================================================
"""

today = date.today()
d1 = today.strftime("%d/%m/%Y")


print(console_output)

# prints all files that are in sql format


def checkFiles():

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    txt = "This is the file {something}: "
    print(txt.format(something=files))
    for f in files:
        if f.endswith('.sql'):
            print(f)
            readFile(f)


def readFile(fileName):
    with open(fileName, 'r') as f:
        sqlquery = f.read()
        print(sqlquery)
        f.close()
        userInput(fileName, sqlquery)


# inputs are thrown into the string using formatter


def userInput(fileName, sqlquery):

    # Need to find out how to do inputs in pre-commit
    # author = input("Enter your name: ")
    # date = input("Enter date of creation: ")
    # description = input("Short summary of current query: ")

    # sys.stdin = open("COM1:")
    author = "Pero"
    date = "10102000"
    description = "This is sql file"
    print(header.format(author=author, date=date, description=description))
    editFile(fileName, sqlquery)


def editFile(fileName, sqlquery):
    with open(fileName, 'w') as f:
        formated = header + "\n" + sqlquery
        print("FORMATED:\n\n " + formated + "\n\n")
        f.write(formated)
        f.close()


checkFiles()
