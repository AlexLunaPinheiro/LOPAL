import pandas as pd


df = pd.read_csv('historico_pedidos.csv', encoding='utf-8')
df.to_json('historico_pedidos.json', orient='records', force_ascii=False, indent=4)
