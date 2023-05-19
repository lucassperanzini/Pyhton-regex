import re

erro = ""
try:
    nome = input("nome :")
    if re.search(r"\d" , nome):
        erro = "não pode haver números em nomes"
        raise ValueError
    
    celular = input(" digite seu número de celular")
    
    if  not re.match('^\d{10,11}', celular):
        erro = "o número de celular tem que ter de 10 a 11 digitos"
        raise ValueError
    
    if len(celular) == 10:
        phone = f"({celular[0:2]})" + celular[2:6] + "-" + celular[6:]
    else:
        phone = f"({celular[0:2]})" + celular[2:7] + "-" + celular[7:]

    print(f"Telefone : {phone}")
        
except ValueError:
    print(erro)


##############################

