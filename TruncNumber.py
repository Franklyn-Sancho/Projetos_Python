#Quebrar um número decimal, apenas apresentando o seu inteiro. 

from math import trunc
num = float(input('Digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
