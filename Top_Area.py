# Top Area

o = input()  
soma = 0.0
contador = 0
for k in range(144): 
    valor = float(input()) 
    i = k // 12
    j = k % 12
    if j > i and i + j < 11: 
        soma += valor
        contador += 1
if o == 'S':
    print("%.1f" % soma)
elif o == 'M':
    if contador > 0: 
        media = soma / contador
        print("%.1f" %media)
    else:
        print("0.0")