# Programa 8.1 - Pesquisa em uma lista
def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None
L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))

##--------------------------------------------

def soma(L):
    total= 0
    for e in L:
        total += e 
    return total
def média(L):
    return soma(L) / len(L)