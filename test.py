import pyperclip

minha_variavel = "Texto que vai para o clipboard"
pyperclip.copy(minha_variavel)

#import csv

#pokedex = {}

#with open("gen01.csv", encoding="utf-8") as arquivo:
#leitor = csv.DictReader(arquivo)

#print(leitor.fieldnames)

#for item in leitor:
    #pokedex[item["name"]] = item

    #print(pokedex)

    #team = ['', "a", '', '', '', '', ]

    #print(team)

    #a = True
    #a = a*0

    #if a:
    #print(f"True em a: {a}")
    #else:
    #print(f"False em a: {a}")
a = ["1"]
b = a

print(b)
a.append("2")
print(b)

var1 = ("A", "B")

for i in range(2):
    print (f"{var1[0]} bateu em {var1[1]}")
    var1 = (var1[1], var1[0])

a = [1, 2, 3, 4]

def somar1(lista):
    for i in lista:
        i +=1

somar1(a)

print(a)

# Lendo a entrada do exercício
A = int(input("digite o número de alunos: "))
M = int(input("digite o número de monitores:"))

# Seu código vai aqui

def validate(num):
    if 0 < num <= 50:
        return True
    else:
        return False

if validate(A) and validate(M) and 0 < A + M <= 50:
    print("S")
else:
    print("N")

test_dict = {
    "ameixa" : 10,
    "abacate" : 12,
}

print(test_dict.items())