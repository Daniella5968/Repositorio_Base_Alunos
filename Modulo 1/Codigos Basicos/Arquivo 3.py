import os
os.getcwd()
os.mkdir("d")
os.mkdir("e")
os.mkdir("f")

import os
arquivo_path="diretorio"
try:
    os.rmdir(arquivo_path)
    print(f"""\033[0;32m pasta'{arquivo_path}'removida com sucesso! ;D""")
except FileNotFoundError:
    print(f"""\033[0;33m pasta '{arquivo_path}']nao encontrada...@_@""")
except OSError:
    print(f"""\033[0;34m '{arquivo_path}']e um arquivo, nao uma pasta!!!+_+""")    
    
import os

try:
    for n in range(1,51):
        os.mkdir("Pasta_%d" % n)
        os.chdir("pasta_%d" % n)
        arquivo=open("arquivo.txt", "w")
        arquivo.write("oi")
        arquivo.close()
        os.chdir("..")
except FileNotFoundError:
    print('arquivo nao encontrado')

