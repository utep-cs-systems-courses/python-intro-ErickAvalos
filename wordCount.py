#!/usr/bin/python


def readFile():
    file = open("declaration.txt", "r")
    text = file.read()
    file.close()
    print(text)
    return text


def countWords(text):
    words = text.split()
    print(len(words))


text = readFile()
countWords(text)