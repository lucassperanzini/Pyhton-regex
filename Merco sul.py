import re

erro = ""

try:
   nome = input(" Qual é o seu nome?")

   if re.search(r"\d",nome):
       erro = "Não pode haver números no nome"
       raise ValueError
   

   placa = input("Digite a placa do carro")

   if not re.search(r"[A-Z]{3}\d{1}[A-Z]{1}\d{2}", placa) or len(placa) > 7:
       erro = "Não está no formato adequado. Se vira Chat gpt te informa"       
       raise ValueError
   else:
       
       MERCO_SUL = placa[0:3] + " " + placa[3:]

       print(F"""

       Seu nome : {nome}

       Sua placa : {MERCO_SUL}
       
       
       
       """)




except ValueError:
    print(erro)

finally:
    print("Finalizado")