import math
def multiplicar (lista1,lista2):
    return [lista1[i]*lista2[i] for i in range (len(lista1))]

suma = 0
lista_multiplicar = [2,3,4,5,6,7,2,3]

rut = input("RUT sin DV :")
lista_rut = []

for i in rut:
    lista_rut.append(i)
lista_rut.reverse()

lista_rut_int = [int(i) for i in lista_rut]

lista_res_multi = multiplicar (lista_rut_int,lista_multiplicar)

for i in lista_res_multi:
    suma += i

suma_y_division = (math.floor(suma/11))

multiplicar11 = (suma_y_division*11)

resta_por_suma = (suma-multiplicar11)

resta_final = (11-resta_por_suma)

if resta_final == 10:
    print ("Su digito verificador es : K")
elif resta_final == 11:
    print ("Su digito verificador es : 0")
else:
    print ("Su digito verificador es :", resta_final)




    