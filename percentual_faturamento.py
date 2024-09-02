# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 
faturamentos = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

valor_total = sum(faturamentos.values())

for esatdo,faturamento in faturamentos.items():
    percentual = (faturamento/valor_total)* 100
    print(f'{esatdo}:{percentual:.2f}%')
