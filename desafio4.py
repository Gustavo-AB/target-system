sp = 6783643
rj = 3667866
mg = 2922988
es = 2716548
outros = 1984953
total = sp+rj+mg+es+outros


sp_percentual = (sp/total)*100
rj_percentual = (rj/total)*100
mg_percentual = (mg/total)*100
es_percentual = (es/total)*100
outros_percentual = (outros/total)*100

print("=-"*20)
print(" "*10, "FATURAMENTO MENSAL")
print("=-"*20)
print("SP – R$67.836,43\nRJ – R$36.678,66\nMG – R$29.229,88\nES – R$27.165,48\nOutros – R$19.849,53")

print("-"*30)
print(f"Percentual de Representação de SP: {sp_percentual:.2f}%")
print(f"Percentual de Representação de RJ: {rj_percentual:.2f}%")
print(f"Percentual de Representação de MG: {mg_percentual:.2f}%")
print(f"Percentual de Representação de ES: {es_percentual:.2f}%")
print(f"Percentual Representação de Outros: {outros_percentual:.2f}%")
