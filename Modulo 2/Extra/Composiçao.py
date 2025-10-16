class itemDopedido:
    def __init__(self,produto:str,quantidade:int,preço_unitario:float):
        self.produto=produto
        self.quantidade=quantidade
        self.preço_unitario=preço_unitario

    def calcular_subtotal(self) -> float:
        return self.quantidade * self.preço_unitario
    
class pedido:
    def __init__(self,id_cliente:int):
        self.id_cliente=id_cliente
        self.itens=[]
        print(f"\npedido criado para o cliente {self.id_cliente}.")

    def adicionar_item(self,produto:str,quantidade:int,preço_unitario: float):
        novo_item=itemDopedido(produto,quantidade,preço_unitario)
        self._itens.append(novo_item)
        print(f" - item '{produto}' adcionado ao pedido.")
    
    def calcular_total(self):
        total=sum(item.calcular_subtotal() for item in self._itens)
        print(f"total do Pedido: R${total:.2f}")

pedido_123=pedido(957)

pedido_123.adicionar_item("Notebook Gamer", 1, 5000.00)
pedido_123.adicionar_item("Mause sem fio",2,150)
pedido_123.calcular_total()




