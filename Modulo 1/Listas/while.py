def tabuada():#Exercicio 5.7
    n=int(input("Digite um numero:"))    
    fim=int(input("Digite o final:"))

    x=1
    while x <=10:
        print("n","x",x,"=",x*"n")
        x=x+1
#tabuada()

def whilebreak():
    s=0
    while True:
        v=int(input("Digite um numero a somar ou 0 para sair:"))
        if v==0:
            break
        s=s+v
    print(s)
whilebreak()


