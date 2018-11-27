import random
import time
total_penalties = 0
pl_score = 0
ki_score = 0
sh_directions = ["left","middle","right"]
text1 = input("Geben Sie ihren Namen ein : ")
text2 = "Penalty-Shootout"
zeichen = "*"
anzahl = len(text2)+8

def sternenreihe(z, a):
    return z * a

def Titel(t):
    return (zeichen + t.center(anzahl-2)+ zeichen)

print(sternenreihe(zeichen, anzahl))
print(Titel(text2))
print(Titel(text1))
print(sternenreihe(zeichen, anzahl))
time.sleep(1)