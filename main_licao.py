from classe import Pedido

pedido = Pedido()

while True:
    resposta = input("Digite\n1 para adicionar produto\n2 para retirar produto\n3 para exibir os produtos\n")
    
    if resposta not in ["1", "2", "3"]:
        print("Digite um número válido!\n")
        continue

    if resposta == "1":
        try:
            nome_produto = input("Digite o nome do produto:\n")
            preco_produto = float(input("Digite o preço do produto:\n"))
            pedido._Adicionar_Item(nome_produto, preco_produto)
            print("Produto adicionado com sucesso!")
        except ValueError:
            print("Digite um preço válido! Produto não foi adicionado.\n")

    elif resposta == "2":
        nome_produto_remove = input("Digite o nome do produto para remover:\n")
        pedido._Remover_Item(nome_produto_remove)
    
    elif resposta == "3":
        pedido._Print_Pedido()
