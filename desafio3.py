import json

with open("dados.json") as d:
    dados = json.load(d)

contador = 0
maior_faturamento = 0
menor_faturamento = 999999999
dia_do_maior = 0
dia_do_menor = 0
media = 14605.759116666664
dias_maior_media = 0

for dado in dados:
    print(dado["dia"],  dado["valor"])
    contador += 1

    if contador == 0:
        maior_faturamento = dado["valor"]
        menor_faturamento = dado["valor"]

    if dado["valor"] > 14605.759116666664:
        dias_maior_media += 1

    else:
        if dado["valor"] > maior_faturamento:
            maior_faturamento = dado["valor"]
            dia_do_maior = dado["dia"]

        if dado["valor"] == 0:
            dado["valor"] = 99999999

        if dado["valor"] < menor_faturamento:
            menor_faturamento = dado["valor"]
            dia_do_menor = dado["dia"]
    

print(f"\n\033[32mO Maior Faturamento do Mês\033[m\nDia: {dia_do_maior}\nFaturamento: R${maior_faturamento:,.2f}")
print("-"*30)  
print(f"\033[32mO Menor Faturamento do Mês\033[m\nDia: {dia_do_menor}\nFaturamento: R${menor_faturamento:,.2f}")   
print("-"*30)  
print(f"No Total {dias_maior_media} Dias Superaram a Média Mensal de R${media:,.2f} ")
