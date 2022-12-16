#Programa 8.4 - Outra forma de calcular o fatorial
def fatorial(n):
    fat = 1
    x = 1 
    while x <= n:
        fat *= x
        x += 1
    return fat