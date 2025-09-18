arquivo=open("numeros.txt", "w")
for linha in range(101):
        arquivo.write("%dDaniella\n" % linha)
        arquivo.close()
except FileNotFoundError:
print('Arquivo nao encontrado!')
