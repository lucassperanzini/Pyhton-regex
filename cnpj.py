import re

COR_VERMELHO = '\033[91m'
COR_VERDE = '\033[92m'
COR_AZUL = '\033[94m'
COR_RESET = '\033[0m'


erro = ""



try:

    CNPJ = input(f"Qual é o seu CNPJ: ")


        
    if re.search(r"[a-zA-Z]", CNPJ):
        erro = "Não pode haver letras no CNPJ"
        raise ValueError

    if not re.match(r"\d{14}", CNPJ):
        erro = "O CNPJ deve conter 14 números!"
        raise ValueError
    
    CNPJ_formatado = CNPJ[0:2] + "." + CNPJ[2:5] +"." + CNPJ[5:8] + "/" + CNPJ[8:12] + "-" + CNPJ[12:] 

    if CNPJ[8:12] != "0001":
        print("formato NÃO adequado")

        print(CNPJ_formatado )

    else:   
        print(CNPJ_formatado)
        print("Deu certo !!!")


except ValueError:
    print(erro)
