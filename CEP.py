import re

erro = ""
try:
    nome = input("Digite seu nome: ")

    if re.search(r"\d", nome):
        erro = "Nomes não podem conter números"
        raise ValueError
    
    CEP = input("Digite seu CEP: ")

    if not re.search(r"\d{8}", CEP) or len(CEP) > 8:
        erro = "CEP deve conter 8 dígitos"
        raise ValueError  
    
    CEP_alterado = CEP[0:5] + "-" + CEP[5:]
    
    print(f""" Nome : {nome} 
    
    CEP : {CEP_alterado}

     """)
    
except ValueError:
    if erro:
        print(erro)
finally:
    print("Bom sono, bonequinha")