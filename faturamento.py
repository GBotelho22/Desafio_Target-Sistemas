#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

def menor_valor(dados):
    return min(dados)

def maior_valor(dados):
    return max(dados)

def valores_acima_m(dados):
    
    valores_validos = [valor for valor in dados if valor > 0]
    media = sum(valores_validos)/len(valores_validos)
    return sum(1 for valor in dados if valor > media)

def extrair_valores(dados):
    return [item["valor"]for item in dados]    

arquivo = open("dados.json","r")
dados = json.load(arquivo)
valores = extrair_valores(dados)

print(menor_valor(valores))
print(maior_valor(valores))
print(valores_acima_m(valores))
