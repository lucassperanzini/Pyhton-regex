import re
erro = ""
try:
    data = input(" Qual a sua data de nascimento? DD/MM/AAAA  :  ")

    if  re.search(r"^[a-zA-Z]",data):
        erro = "Não pode haver Letras na Data de nascimento"
        raise ValueError
    
    

    data_formatada = re.sub(r"(\d{2})(\d{2})(\d{4})", r"\1/\2/\3", data)

    if data_formatada == data:
        erro = """Por favor, insira corretamente sua data de nascimento, 
        exemplo: 5 de maio de 1998 colocar '05051998'"""
        raise ValueError


    print("Data de nascimento formatada:", data_formatada)

except ValueError:
    print(erro)
finally:
    print("ola")