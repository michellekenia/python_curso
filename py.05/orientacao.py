from operacoes import OperacoesMatematicas

instancia_operacoes = OperacoesMatematicas()

primeiro_numero = int(input ("Digite o primeiro número:"))

segundo_numero = int(input ("Digite o primeiro número:"))

resultado_da_soma = instancia_operacoes.soma(primeiro_numero, segundo_numero)
print(f"O resultado da soma é: {resultado_da_soma}")

resultado_da_subtracao = instancia_operacoes.subtracao(primeiro_numero, segundo_numero)
print(f"O resultado da subtração é: {resultado_da_subtracao}")

resultado_da_divisao = instancia_operacoes.divisao(primeiro_numero, segundo_numero)
print(f"O resultado da divisão é: {resultado_da_divisao}")

resultado_da_multiplicacao = instancia_operacoes.multiplicacao(primeiro_numero, segundo_numero)
print(f"O resultado da multiplicação é: {resultado_da_multiplicacao}")
