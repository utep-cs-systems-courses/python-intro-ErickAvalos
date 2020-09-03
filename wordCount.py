# opening the file
text = open("declaration.txt", "r")

# new dictionary
d = dict()

# reading every line of the file
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    # counting the occurences in 'words'
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

# sorting the dictionary into a list
lists = sorted(d.keys())

# create a new file
text = open("declarationKey.txt", "w")

# writing the word and the key value into the file
for word in lists:
    text.write(word + " " + str(d[word]) + "\n")
text.close()