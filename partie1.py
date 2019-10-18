import math

# exo1: Le nombre le plus grand
num_1 = 3; num_2 = 8; num_3 = 23; num_4 = 64
b = [num_1, num_2, num_3, num_4]
print(max(b))
    
# exo2: Conditon d'âge
try:
    Age = int(input("Quel est votre âge ? "))
    if Age <= 0:
            print("Entrer votre âge réel ")
    if Age >= 21:
            print("Bonne nouvelle, l'accés vous est autorisé")
    if Age%2 == 0:
            print("Encore une bonne nouvelle, votre âge est pair")
    if math.sqrt(Age).is_integer():
            print("Bingo ! votre âge est carré")
    else:
            print("rentrer votre vrai âge !")
except ValueError:
    print("petit malin tu m'aura pas ;)")

# exo3:Le nombre caché
Nombre_caché = 18
User = int(input("Quel est le nombre caché ? "))

while Nombre_caché != User:
    if User > Nombre_caché:
        print("Le nombre est trop grand")
        User = int(input("Recommence "))
    if User < Nombre_caché:
        print("Le Nombre est trop petit")
        User = int(input("Recommence "))
    if User == Nombre_caché:
        print("Bien jouer tu as trouver le bon nombre !")
if User == Nombre_caché:
    print("bravooooo!!!")  

#exo4: Des nombres en boucles
input("appuyer sur enter")
for x in range(101):
    print(x)

#exo5: Des nombres en boucle bis
for x in range(101):
    if x%2 == 0:
        print(int(x), "Ce nombre est pair")
        
#exo6: Remplir la piscine
def pool_filing(long, larg, prof, debit):
    filing_time = (long*larg*prof)/debit
    print("time of filing is {} minutes".format(filing_time))

pool_filing(12, 6, 3, 10)

#exo7: Calcul de cercle
def Périmètre(rayon):
    périmètre = round((2*math.pi*rayon), 2)
    print("votre cercle a un périmètre de {} cm".format(périmètre))

def Aire(rayon):
    aire = round((math.sqrt(rayon)*math.pi), 2)
    print("Votre cercle a une aire de {} cm carré".format(aire))

rayon = int(input("Quel est le rayon de votre cercle"))
Périmètre(rayon)
Aire(rayon)

#exo8: Une pyramide
Var_0 = "```"
Var_1 = "\n"
Var_2 = ""

for i in range(1, 6):
    if i == 1:
        Var_1 = Var_0 + Var_1
    else:
        Var_2 += "*"
        Var_1 += Var_2 + "\n"
print(Var_1 + Var_0)

#exo9: 
fizbuz = ""
for i in range(1, 101):
    if i%3 == 0:
        fizbuz = "FIZZ"
        if i%5 == 0: 
            fizbuz = "FIZZBUZZ"
    elif i%5 == 0:
        fizbuz = "BUZZ"    
    print("{} - {}".format(i, fizbuz))
    fizbuz = ""

