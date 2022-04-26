"""PROGRAMA PARA CALCULAR
EL VALOR DE UNA LLAMADA"""

print("""----------------------------------------------------""")
print("""----------Calcular el valor de una llamada----------""")
print("""----------------------------------------------------""")

# input

m = int(input("Ingresa el numero de minutos usados: "))

# processing

if m <= 3:
    msj = "el valor es de 300 "
else:
    msj = 300 + (50 * (m - 3))

# output

print("El costo es : " + str(msj))