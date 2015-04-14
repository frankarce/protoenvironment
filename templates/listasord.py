lista=[110,91,31,41,51,61,71,81,210,101]
contador=0
tempmenor=0
mayor=0
for x in range(10):
    #lista.append(int(raw_input("Dame el numero:")))
    if lista[x]%2==0:
        contador+=1
print contador
menor=lista[0]
for x in lista:
    if x < menor:
        menor = x
    if x > mayor:
        mayor=x
contador
print menor
print mayor
