print("="*30)
print(" "*2,"Sequiencia de Fibbonahci")
print("="*30)

numero = int(input("Digite um numero: "))
termo1 = 0
termo2 = 1
termo3 = 0

print(termo1, termo2, end=" ")

while termo3 < numero:
    termo3 = termo1 + termo2
    print(f"{termo3}", end=" ")
    termo1 = termo2
    termo2 = termo3

print("...")

if numero == termo3:
    print(f"\033[32mO número {numero} faz parte da Sequencia de Fibbonahci\033[m")

if numero != termo3:
    print(f"\033[31mO numero {numero} não faz parte da Sequencia de Fibbonahci\033[m")
