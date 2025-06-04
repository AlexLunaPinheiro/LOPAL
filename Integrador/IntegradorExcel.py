import pandas as pd

caminho_csv = 'LOPAL-ProjetoIntegrador-Esp8266_Receiver (1).csv'
df = pd.read_csv(caminho_csv)
caminho_excel = 'DadosSensor.xlsx'
df.to_excel(caminho_excel, index=False)


