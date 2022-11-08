#Faça um programa que preencha um vetor com seis elementos númericos inteiros. Calcule e mostre
#.todos os números pares;
#.a quantidade de números pares
#.todos os números impares
#.a quantidade de números impares
 
num = []
qp = 0
qi = 0

for n in range (0,6):
    num.append(int(input(f"Digite o {n + 1}º número: ")))

for n in range (0,6):
    if num[n] % 2 == 0:
        print(f"Os números pares são :{num[n]}")
        qp += 1
    else:
        print(f"Os números ímpares são: {num[n]}")
        qi += 1
print(f"A quantidade de números pares são: {qp}")
print(f"A quantidade de números ímpares são: {qi}")






