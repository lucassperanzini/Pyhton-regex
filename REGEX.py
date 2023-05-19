import re

texto = "Bom dia flor do dia!"

padrão = r"o"

ocorrencias_f = re.findall(padrão,texto)

print(ocorrencias_f)

##############################################

texto = "bom dia flor do sol"

padrão = "fl"

match = re.search(padrão,texto)

if match == None:
    print("imbecil não tem nenhum padrão")
else:

    print(match)

######################################################

# dividir quando encontrar vírgula
texto = "Hello, World! How are you?"
padrao = r",\s" # \s faz isso
split = re.split(padrao, texto)
print(split)


##################################################


texto = "Hello, Lula!"
padrao = "Hello"
novo_texto = re.sub(padrao, "boa tarde", texto)
print(novo_texto)  # Saída: "Boa tarde, Lula!!" 

