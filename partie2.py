# exo1: Un échiquier

line = "# # # # # # # #"
blanc = " "

print("```")
print("  \"")
for i in range(0, 8):
    if i%2 == 0:
        print("   {}{}".format(line, blanc))
    else: 
        print ("   {}{}".format(blanc, line)) 
print("  \"")
print("```")      

#exo2: Matrix dans le terminal

L = [0,0,0,0]
var1=0; var2=0; var3=0; var4=0; var5= "-------"
print("```")
for i in range(0, 4):
    L[i] = 1
    var1 = L[0]
    var2 = L[1]
    var3 = L[2]
    var4 = L[3]
    print("{}\n{}\n{}\n{}\n{}".format(var1,var2,var3,var4,var5))
    L[i] = 0
print("```")

#exo3: Nombre paire ?

def evenYesNo(number):
    number = int(number)
    print(not(number%2))

user = input("Entrez votre montant ? ") 
if "." in user:
    user=float(user)
else:
    user=int(user)
evenYesNo(user) 

#exo4: Vous avez dit factorielle ?

def Factoriel(N):
    if N > 1: return N * Factoriel(N - 1)
    else: return 1
    
print ("Liste des 5 premiers factoriels entiers:")
for i in range(0, 5):
     print (i," est ",Factoriel(i))

#exo5: Les tirets ça compte !

def replaceMinusWithUnderscore (DaString):
    import re
    retour=re.sub(r"-",r"_",DaString)
    return(retour)

MyString = input("Entrez votre ligne : ")
print(replaceMinusWithUnderscore(MyString))

#exo6: Entraînez-vous avec les tableaux

Liste_course = ["Pommes", "Banane", "Poire", "Fraises"]
print ("Vous devez encore achetez des", Liste_course[0], "ansi que des", Liste_course[-1])

#exo7: Le tableau d'un homme
liste = [["bruno", "harlein", "40", "1979"], ["thomas", "gossart", "28", "1954"]]

def tableau(liste):
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            print(liste[i][j])

tableau(liste)

#exo8: 

Age = [25, 10.9, 3, 765.2]
Age2 = ["bbb","bbbbb","bb"]
Age3 = [12, "Abdel", "Booba", 34]

def AgeMax(MyAge):
    try:
        print("le max est ", max(MyAge))
    except:
        print(False)

AgeMax(Age)
AgeMax(Age2)
AgeMax(Age3)

#exo9: 

Agenda = list()
def save(Tâches):
    Agenda.append(Tâches)
    return Agenda 
mot=""
while mot != "stop":
    save(mot)
    mot=input("Quel tache voulez-vous rajouter à votre agenda ? ")
print(Agenda)








