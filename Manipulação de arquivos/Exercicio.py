import csv

dados = [
    ['Nome','Preço'],
    ['Livro',20]

]

with open('produtos.csv','w',newline='')as arquivo:
    escritor_csv = csv.writer(arquivo)
    for linha in dados:
        escritor_csv.writerow(linha)
i = 0
with open('produtos.csv', 'r')as arquivo:
    leitor_csv =csv.reader(arquivo)
    for linha in leitor_csv:
        print(f"{linha[0]},{linha[1]}")
