'''
Escreva uma função chamada intercala_numeros que recebe como entrada duas tuplas de três
elementos e retorna uma tupla de seis elementos, com os números intercalados.
Exemplo:
Suponha que as tuplas de entrada da função sejam:
(1, 2, 3)
(4, 5, 6)
Para estas tuplas, a função deve retornar a tupla:
(1, 4, 2, 5, 3, 6)
'''
from random import randint

def intercala_numeros(tupla1, tupla2):
    tupla3 = ()
    
    for i in range(len(tupla1)):
        tupla3 = tupla3 + (tupla1[i],) + (tupla2[i],)
    
    return tupla3

tupla1 = ()
tupla2 = ()

for i in range(3):
    n = randint(1, 9)
    tupla1 = tupla1 + (n,)

    n = randint(1, 9)
    tupla2 = tupla2 + (n,)

print('Primeira Tupla:', tupla1)
print('Segunda Tupla:', tupla2)

tupla3 = intercala_numeros(tupla1, tupla2)
print('Tupla Resultante', tupla3)
