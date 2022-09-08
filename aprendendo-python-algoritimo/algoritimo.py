# import antigravity
# import this
# print('hello word')

# fisilofia em python

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
from array import array
from cgi import print_environ_usage
from ntpath import join
from ssl import RAND_bytes


chave = ""
meu_dict = {
 123: "um dois tres",
 chave: "valor",
}
""" Exercício 1: No terminal, inicialize duas variáveis a e b, sendo a = 10 e b = 5. Mostre o resultado das 7 operações básicas (soma, subtração, multiplicação, divisão, divisão inteira, potenciação e módulo) envolvendo essas variáveis. """
a = 10
b = 5
print(a + b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)
print(a - b)
print(a // b)

""" Exercício 2: Declare e inicialize uma variável: hours = 6. Quantos minutos têm em 6 horas? E quantos segundos? Declare e inicialize variáveis minutes e seconds que recebem os respectivos resultados das contas. Depois, imprima cada uma delas. """

hour = 6

minutes = hour * 60

seconds = minutes * 60

print(minutes)
print(seconds)

books = 60
book_price = 24.29 * 0.4
logistic = 3 + books * 0.75
cost = books * book_price + logistic
cost
print(cost)
fruits = ["laranja", "maçã", "uva", "abacaxi"]  # elementos são definidos separados por vírgula, envolvidos por colchetes

fruits[0]  # o acesso é feito por índices iniciados em 0

fruits[-1]  # o acesso também pode ser negativo
print(fruits[-1])
fruits.append("banana")  # adicionando uma nova fruta

fruits.remove("abacaxi")  # removendo uma fruta

fruits.extend(["pera", "melão", "kiwi"])  # acrescenta uma lista de frutas a lista original

fruits.index("maçã")  # retorna o índice onde a fruta está localizada, neste caso, 1

fruits.sort()  # ordena a lista de frutas

trybe_course = ["Introdução", "Front-end", "Back-end"]

trybe_course.append("ciencia da computação")

trybe_course[0] = "Fundamentos"

print(trybe_course)
"""tuplas"""
user = ("Will", "Marcondes", 42)  # elementos são definidos separados por vírgula, envolvidos por parênteses

user[0]  # acesso também por índices

"""Um conjunto é uma coleção de elementos únicos e não ordenados. Conjuntos implementam operações de união, intersecção e outras."""

permissions = {"member", "group"}  # elementos separados por vírgula, envolvidos por chaves

permissions.add("root")  # adiciona um novo elemento ao conjunto

permissions.add("member")  # como o elemento já existe, nenhum novo item é adicionado ao conjunto

print(permissions.union({"user", "eita"}))  # retorna um conjunto resultado da união



print(permissions.intersection({"user", "member"}))  # retorna um conjunto resultante da intersecção dos conjuntos

print(permissions.difference({"user"}))  # retorna a diferença entre os dois conjuntos

name = set()
name.add("yang wom")
print(name)

people_by_id = {1: "Maria", 2: "Fernanda", 3: "Felipe"}  # elementos no formato "chave: valor" separados por vírgula, envolvidos por chaves

people_by_name = {"Maria": 1, "Fernanda": 2, "Felipe": 3}  # outro exemplo, dessa vez usando strings como chaves. As aspas são necessárias para que o Python não ache que `Maria`, `Fernanda` e `Felipe` sejam variáveis.

# elementos são acessados por suas chaves
people_by_id[1]  # saída: Maria

# elementos podem ser removidos com a palavra chave del
del people_by_id[1]
people_by_id.items()  # dict_items([(1, "Maria"), (2, "Fernanda"), (3, "Felipe")])
# um conjunto é retornado com tuplas contendo chaves e valoresinfo = {
  
info = {
  "personagem": "Margarida",
  "origem": "Pato Donald",
  "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}

info["recorrente"] = "sim"

del info["origem"]
print(info)

eita = range(5)
print(list(eita))

# vamos converter o range em uma lista para ajudar na visualização

# definimos somente o valor de parada
list(range(5))  # saída: [0, 1, 2, 3, 4]

# definimos o valor inicial e o de parada
list(range(1, 6))  # saída: [1, 2, 3, 4, 5]

# definimos valor inicial, de parada e modificamos o passo para 2
list(range(1, 11, 2))  # saída: [1, 3, 5, 7, 9]

# podemos utilizar valores negativos para as entradas também
print(list(range(10, 2, -2)))  # saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

data_base = {
    "name": "tiago",
    "lastname": "meireles",
    "idade": 29
}

restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

filtered_restaurants = []
min_rating = 3.0
for restaurant in restaurants:
    if restaurant["nota"] >  min_rating:
        filtered_restaurants.append(restaurant)

        print(f' new {filtered_restaurants}')

        for index in range(5):
            print(index)

            nomes = ['Duda', 'Rafa', 'Cris', 'Yuri']
nomes2 = [s for s in nomes if 'a' in s]
print(nomes2)
n = 10
last, next = 0, 1
while last < n:
    print(last)
    last, next = next, last + next
# Saída
['Duda', 'Rafa']

languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# converte um objeto enumerate em uma lista
print(list(enumerate_prime))

languages = ['Python', 'Java', 'JavaScript']

for index, language in enumerate(languages):
    print(f'{index} - {language}')
number = 5
result = 1
# Usamos number + 1 pro range ir até o number
for factor in range(number, 0, -1):
    result *= factor
print(result)
# Saída: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

def concat(*strings):
    # Equivalente a um ", ".join(strings), que concatena os elementos de um iterável em uma string utilizando um separador
    # Nesse caso a string resultante estaria separada por vírgula
   ", ".join(strings)
   return strings
# pode ser chamado com 2 parâmetros
 # saída: "Carlos, Cristina"
print(concat("Carlos", "Cristina"))
# pode ser chamado com um número n de parâmetros
concat("Carlos", "Cristina", "Maria")  # saída: "Carlos, Cristina, Maria"
print(len([1, 2, 3, 4]))  # função len não aceita argumentos nomeados
# dict é uma função que já vem embutida no python
dict(nome="Felipe", sobrenome="Silva", idade=25)  # cria um dicionário utilizando as chaves passadas

dict(nome="Ana", sobrenome="Souza", idade=21, turma=1)  # o número de parâmetros passados para a função pode variar