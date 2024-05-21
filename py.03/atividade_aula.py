
# # se numero for múltiplo de 3 print FIZZ
# # se numero for múltipo de 5 print BUZZ  
# # se numero for múltipo de 3 e de 5 print FIZZBUZZ 
# # se numero não for múltipo nem for múltipo de 5 print o próprio número 
    

num = int(input("Diga um número: ")) # o python espera ua entrada do usuário

if num  % 5 == 0 and num % 3 ==0 : 
    print("FIZZBUZZ")
elif num % 3 == 0:   
     print("FIZZ")
elif num % 5 == 0:   
     print("BUZZ")
else:
    print(num) 