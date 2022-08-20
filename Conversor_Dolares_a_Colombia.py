dolares=input('¿Cuantos dolares tienes?: ')
peso = 1/3875
dolares=float(dolares)
pesos=dolares/peso
pesos=round(pesos, 3)
pesos=str(pesos)
print('Tienes $'+pesos+' pesos colombianos')