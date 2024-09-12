import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

valores = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

print(f'O menor valor de faturamento é: {menor_valor:.2f}')
print(f'O maior valor de faturamento é: {maior_valor:.2f}')
print(f'O número de dias com faturamento acima da média é: {dias_acima_media}')
