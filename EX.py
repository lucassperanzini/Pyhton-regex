import math

try:
    a = int(input("Digite valor de A: "))
    b = int(input("Digite valor de B "))
    c = int(input("Digite valor de C"))
    
    delta = (b**2) - 4 * a * c
    try:
        if delta < 0:
            raise ValueError("Delta não pode ser negativo. A equação não possui raízes reais.")
        else:

            x1 = (-b + math.sqrt(delta)) / 2 * a

            x2 = (-b - math.sqrt(delta)) / 2 * a

            print(x1,x2)
            
    except ValueError as err:
        print(" Erro", err)
    
    


except ValueError:
     print(" os números devem ser inteiros")   
except Exception as error:
    print(f" ocorreu o erro :  {error}")  
finally:
    print("Finalizado")