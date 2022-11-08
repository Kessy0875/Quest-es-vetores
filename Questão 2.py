import os
#Faça um programa que preencha um vetor com sete números inteiros, clacule e mostre:
#.os números múltiplos de 2
#.os números multiplos de 3
#.os números múltiplos de 2 e 3

num = []
numMult2 = []
numMult3 = []
numMult2e3 = []
os.system("clear")
for n in range(0,7):
    num.append(int(input(f"Digite o {n + 1}º número: ")))

for n in range(0,7):
    if num[n] % 2 == 0:
       numMult2.append(num[n])
    
    if num[n] % 2 == 0 and num[n] % 3 == 0:
        numMult2e3.append (num[n])
    
    if num[n] % 3 == 0:
        numMult3.append (num[n])
os.system("clear")
print(f"Os números: {numMult2} são multiplos de 2")
print(f"Os números: {numMult3} são multiplos de 3")
print(f"Os números: {numMult2e3} são multiplos de 2 e 3")    
