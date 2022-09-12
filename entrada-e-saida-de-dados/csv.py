import csv

with open("graduacao_unb.csv",  encoding = "utf-8") as file:
    graduacao_reader = csv.DictReader(file)
    for gradu in graduacao_reader:
       print(gradu)
    