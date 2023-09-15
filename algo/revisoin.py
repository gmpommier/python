from math import*

"""
for i in range(3,16):
    print(i)


i=2
while i<16:
    i+=1
    print(i)


for i in range(30,9,-1):
    print(i)

i=31
while i>10:
    i-=1
    print(i)
"""
"""
for i in range(0,6):
    print(0*i)
    for n in range(0,5):
"""


#exercice 3
"""
n=int(input())
m=1.07310
print(n,'euro(s)=',n*m,'dollar(s)')
"""
#exercice 4
"""
heure=int(input('heure  '))
minute=int(input('minute  '))
seconde=int(input('seconde  '))
heure=heure*60*60
minute=minute*60
total=heure+minute+seconde
print(total)
"""
# Exercice 5
"""
menu="0"
nb1=int(input("Nombre 1"))
nb2=int(input("Nombre 2"))
while menu!='q':
    print("------------------------------------------------------------")
    print("1 : Addition ")
    print("2 : Soustraction ")
    print("3 : Multiplication ")
    print("4 : Division ")
    print("q : quitter ")
    print("------------------------------------------------------------")
    menu=input("votre choix ?  ")
    if menu== "1":
        print(nb1 + nb2)
    if menu== "2":
        print(nb1 - nb2)
    if menu== "3":
        print(nb1 * nb2)
    if menu== "4":
        print(nb1 / nb2)

"""
#exercice 6
"""
a=float(input('Donnez une valeur '))
b=float(input('Donnez une valeur '))
c=float(input('Donnez une valeur '))

delta=b**2-4*a*c
if delta<0:
    print("x n'a pas de solution dans R ")
elif delta==0:
    x=-b/(2*a)
    print("il a une valeur pour x=0 qui sont",x,)

elif delta >0:
    x1=-b-sqrt(delta)/(2*a)
    x2=-b+sqrt(delta)/(2*a)
    print("il a deux valeurs pour x=0 qui sont",x1,"et",x2)
"""
#exercice 7
"""
a1=float(input("coef directeur 1 "))
b1=float(input("ordonnée à l'origine 1 "))
a2=float(input("coef directeur 2 "))
b2=float(input("ordonnée à l'origine 2 "))

x=(b2-b1)/(a1-a2)
y=a1*x+b1
print("les coordonées sont(",x,y,")")
"""










































