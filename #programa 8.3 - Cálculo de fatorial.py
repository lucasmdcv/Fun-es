#programa 8.3 - Cálculo de fatorial
def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n 
        n -= 1
    return fat