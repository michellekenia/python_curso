entrada_do_usuario = int(input("numero"))

def fizzbuzz(parametro_da_funcao): 
    for num in range(1, parametro_da_funcao + 1): 
        if num % 15 == 0:
            print ("FIZZZBUZZ")
        elif num % 5 == 0:
            print ("BUZZ")
        if num % 3 == 0:
            print("FIZZ")
        else: 
            print(num)    

fizzbuzz(entrada_do_usuario)        

