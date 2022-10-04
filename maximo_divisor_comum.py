# Algoritmo com finalidade de calcular o "MDC", algoritmo de euclides - (Maximo dividor comum)

# Defiindo função para o calculo

def mdc_inter(numero_x, numero_y):
    resto_divisao = numero_x % numero_y
    while resto_divisao != 0:
        numero_x = numero_y
        numero_y = resto_divisao
        resto_divisao = numero_x % numero_y
    return numero_y

# Parte principal

numero_x = int(input('Insira o valor do primeiro número: '))
numero_y = int(input('Difite o valor do segundo número: '))

print("O MDC de:({:d},{:d}) = {:d}".format(numero_x,numero_y,mdc_inter(numero_x,numero_y)))
