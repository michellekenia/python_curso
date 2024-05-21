
#Somar todos os números de 0 a 5 - vindos do usuário

numero_0 = int(input("Me diga o primeiro número de 0 a 5:"))
numero_1 = int(input("Me diga o segundo número de 0 a 5:"))
numero_2 = int(input("Me diga o terceiro número de 0 a 5:"))
numero_3 = int(input("Me diga o quarto número de 0 a 5:"))
numero_4 = int(input("Me diga o quinto número de 0 a 5:"))
numero_5 = int(input("Me diga o sexto número de 0 a 5:"))

def somatorio(primeiro_numero, segundo_numero, terceiro_numero, quarto_numero, quinto_numero, sexto_numero): 

    return primeiro_numero+segundo_numero+terceiro_numero+quarto_numero+quinto_numero+sexto_numero

resultado_da_soma = (numero_1+numero_2+numero_3+numero_4+numero_5)
print(f"O resultado da soma é: {resultado_da_soma}")