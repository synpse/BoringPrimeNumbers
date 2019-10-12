# Função que vê se o número n é primo
def checkPrime(n):
    # Se o número n for maior que 1
    if n > 1:
        # Para cada número no intervalo 2 a n
        for i in range(2, n):
            # Se n for divisivel por i
            if (n % i) == 0:
                # Retornar falso
                return False;
                # Forçar saida da iteração
                break
        # Se o anterior não se verificar
        else:
            # Retornar verdadeiro
            return True;
    # Se o número n não for maior que 1
    else:
        # Retornar falso
        return False;

# Dar um parágrafo
print()
# Pedir um input ao utilizador e recebê-lo com um int(inteiro)
num = int(input("Número: "))
# Dar um parágrafo
print()
# Meter o input como parêmetro da função que verifica se o número é primo
if checkPrime(num):
    # Se a função retornar verdadeiro
    print(num, "é primo.")
else:
    # Se a função retornar falso
    print(num, "não é primo.")
