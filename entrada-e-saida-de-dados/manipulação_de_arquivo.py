file = open("persons.txt", mode="w")

file.write("yang wom\n")
file.write("cecilia\n")
file.write("valternei\n")
file.write("theus\n")
file.write("petzinguer\n")
file.write("gabi\n")

print("ruy chegando", file=file)
# excrevendo mutiplas linhas 
LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
file.writelines(LINES)
file.close()




