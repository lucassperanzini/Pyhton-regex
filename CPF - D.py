import re

def verifica_CPF(CPF):
    if not re.match(r"\d{11}", CPF):
        raise ValueError("CPF tem que ter 11 números!!!")

def calcula_digitos(CPF):
     # Só checará os primeiors 9 digitos
    CPF_sera_checado = CPF[0:9]

    pesos = []
    #atribuir pesos aos digitos do CPF
    valor = 10 
    for i in range(len(CPF_sera_checado)):
        pesos.append(valor)
        valor -= 1
        if valor == 1:
            break
    
   

    # multiplicar os valores dos pesos
    CPF_int = [int(d) for d in CPF_sera_checado if d.isdigit()]
    for i in range(len(CPF_int)):
        resultado = CPF_int[i] * pesos[i]
        pesos[i] = resultado
   

    # Soma dos pesos
    soma = sum(pesos)
    

    # resto
    resto = soma % 11
    

    if resto < 2:
        #primeiro digito = 0
        CPF_int.append(0)
        
    else:
        # se não primerio digito 
         CPF_int.append( 11- resto) 
         
    # Novos pesos por conta do novo dígito
    pesos_novos = []
    valor = 11 
    for i in range(len(CPF_int)):
        pesos_novos.append(valor)
        valor -= 1
   

    # multiplicar novos pesos com o cpf com o digito adicionado
    for i in range(len(CPF_int)):
        resultado_mult = CPF_int[i] * pesos_novos[i]
        pesos_novos[i] = resultado_mult
    
    # Soma dos pesos - segundo_digito
    soma = sum(pesos_novos)
   
    #resto
    resto = soma % 11

    if resto < 2:
        #primeiro digito = 0
        CPF_int.append(0)
    else:
        #primerio digito 
         CPF_int.append( 11- resto) 

    return CPF_int


try:
    CPF = input("Digite seu CPF: ")

    #verifica se tem 11 digitp 
    verifica_CPF(CPF)

    CPF_final = calcula_digitos(CPF)

    CPF_final_str = ''.join(str(d) for d in CPF_final)

    # se os dois digitos forem diferenrtes gera um erro
    if CPF[9:] != CPF_final_str[9:]:
        raise ValueError("CPF inválido")
    else:
        CPF_final_str = re.sub("(\d{3})(\d{3})(\d{3})(\d{2})",r"\1.\2.\3-\4",CPF_final_str)
        print(f"O seus CPF é válido  : {CPF_final_str}")


    



except ValueError as err:
    print(str(err))



    

    
    


