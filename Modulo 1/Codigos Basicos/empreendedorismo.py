estoque={"Batom":[3, 5.70],
         "Paleta":[7,7.90],
         "Basse":[5,9.80],
         "corretivo":[2,7.80],
         "blush":[4,60.7],
         "serun":[1,50.9],
         "sombra de olho":[5,9.0],
         "contorno":[30,7.9],
         "sebra de pele":[50,0.0],
         "iluminador":[60,0.0],
         "rimel":[100,0.30],
         "po solto":[300,0.80],
         "po compacto":[800,0.90],
         "contorno de boca":[60,0.0],
         "gloss":[40,0.0],
         "idratante":[90,0.90],
         "primer":[50,60.0],
         "creme":[30,90.0],
         "fixador":[100,0.0],
         "brilho de olho":[200,0.5]}
sei_lá_oque = input("Digite o produto: ") # Empreendedorismo.py
venda = [ [ sei_lá_oque, int(input("Digite a quantidade: ")) ] ]

total = 0
print("Vendas:\n")
if sei_lá_oque in estoque:
  for operação in venda:
    produto, quantidade = operação 
    preço = estoque[produto][1] 
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f" %
		(produto, quantidade,preço,custo))
    estoque[produto][0] -= quantidade 
    total+=custo
else:
   print("Insuficiente!")
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])