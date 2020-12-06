# supondo que o valor do carro seja R$50 reais por dia 
# e cada quilometro rodado custe R$0.20

dias = int(input('quantos dias alugados'))
km = float(input('quantos km rodados'))
pago = (dias * 50) + (km * 20)
print('o total a pagar é de R${:.2f}'.format(pago))