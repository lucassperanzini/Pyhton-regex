import random

try:
    num = int(input(" me fale um numero inteiro"))
    
    num2 = random.randint(0,1)

    divisao = num / num2
    print("divisao feita")
except ZeroDivisionError:
    print("houve um erro, nao pode haver divisão por zero")
except Exception as exception:
    print(exception)
finally:
    print("Finalizado")

