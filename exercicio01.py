from biblioteca import estoque
nomeProduto = input("Digite o produto: ")
quantidade = int(input("Digite a quantidade que você tem do produto em estoque: "))
valorUnit = float(input("Digite o valor unitário do produto: "))

retorno = estoque(nomeProduto, quantidade, valorUnit)

print(retorno)

