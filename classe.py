class Pedido:
    def __init__(self):
        self.itens = list()
        self.preco_total = 0.0
        self.precos = list()
    
    def _Adicionar_Item(self, nome_produto, preco_produto):
        self.itens.append(nome_produto)
        self.precos.append(preco_produto)
        self.preco_total += preco_produto

    def _Remover_Item(self, nome_produto_remove):
        if nome_produto_remove in self.itens:
            indice = self.itens.index(nome_produto_remove)
            self.preco_total -= self.precos[indice]
            self.itens.pop(indice)
            self.precos.pop(indice)
            print(f"Produto '{nome_produto_remove}' removido com sucesso!")
        else:
            print("Produto não encontrado!")

    def _Print_Pedido(self):
        if not self.itens:
            print("Voce nao adicionou nenhum produto!")
        else:
            print("Produtos no pedido:")
            for item, preco in zip(self.itens, self.precos):
                print(f"{item} - R${preco}")
            print(f"Total: R${self.preco_total}")