# exo1: Le nombre le plus grand
num_1 = 3; num_2 = 8; num_3 = 23; num_4 = 64
b = [num_1, num_2, num_3, num_4]
print(max(b))
    
# exo2: Conditon d'âge
import math
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
         
