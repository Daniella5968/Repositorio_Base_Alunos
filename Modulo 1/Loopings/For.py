L=[9,8,7,6,5,4,3,2,1,0]
for Daniella in L:
    print(Daniella)

L=["maça","peras","kiwis"]
for s in L:
    for letras in s:
        print(letras)

L=[1,7,2,4,6,0,3,5,50]     
maximo=L[0]   
for e in L:
    if e > maximo:
        maximo=e
print(maximo)

for v in range(5,8):
    print(v)
    
for t in range(3,33,3):
    print(t,end="")

nome="Daniella"
idade=15
grana=51.34
print("%20s tem %010d anos e R$%5.2f no bolso."%(nome, idade, grana))
 
def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("por favor, nao ultilize zeros ")
    except:
        print("\033[91m algo de errado...]")
    else:
        print(f"seu resultado e :{result}")
    finally:
        print("\033[91m vamos de novo?]")
divide(13,0)
divide("a","q")

value=2
match value:
    case 0:
        print("zero")
    case 1:
        print("um!")
case_:
print("Dois!")













