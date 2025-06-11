import pandas as pd

df = pd.read_excel('historico_pedidos.xlsx', sheet_name='Sheet1', header=0)
df.to_csv('historico_pedidos.csv', index=False)


