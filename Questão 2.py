#Faça um programa que preencha um vetor com sete números inteiros, clacule e mostre:
#.os números múltiplos de 2
#.os números multiplos de 3
#.os números múltiplos de 2 e 3

num = []

for n in range(0,8):
    num.append(int(input(f"Digite o {n + 1}º número: ")))

for n in range(0,8):
    if num[n] % 2 == 0:
        print(f"O número {num[n]} é multiplo de 2")
    
    if num[n] % 2 == 0 and num[n] % 3 == 0:
        print(f"O número {num[n]} é multiplo de 2 e 3")
    
    if num[n] % 3 == 0:
        print(f"O número {num[n]} é multiplo de 3")

    
