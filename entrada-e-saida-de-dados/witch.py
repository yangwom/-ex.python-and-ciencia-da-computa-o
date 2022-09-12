from fileinput import close
from ntpath import join

recuStudents = []
with open("persons.txt", mode="r") as file:
   for line in file:
    reprovados = line.split(" ")
    
    if int(reprovados[1]) < 6:
       recuStudents.append(reprovados[0] + "\n")

with open("reprovados.txt", mode="w") as recuperação:
    recuperação.writelines(recuStudents)

file.close()