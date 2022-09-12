file = open("persons.txt", mode="r")

for line in file:
    print(line)
file.close()    