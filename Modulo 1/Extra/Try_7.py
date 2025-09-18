def divide(x,y)
Try:
sult=x/y 
except ZeroDivisionError:
    print("por favor, nao utilize zeros!")
except:
    print("\033[91m algo deu errado...")
else:
    print(f"seu resultado é:{result}")
finally:
print("\033[92m vamos de novo?")
divide(13,0)

