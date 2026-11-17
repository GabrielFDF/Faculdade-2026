n1 = float(input('Qual a nota:'))
n2 = float(input('Qual a nota:'))
n3 = float(input('Qual a nota:'))
n4 = float(input('Qual a nota:'))
m = (n1 + n2 + n3 + n4)/4
print ('Sua media é: {:.1f}'.format(m))
if m >=6:
    print('aprovado')
else:
    print('reprovado')