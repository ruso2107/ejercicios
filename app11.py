# dicccionarios -> almacen a pares de clave-valor
mi_diccionario = {'nombre':'bruno diaz','edad':25,'ciudad':'la paz'}
print(mi_diccionario)

# acceder a un valor 
print(mi_diccionario['nombre'])
print(mi_diccionario['ciudad'])
    
# agregar elementos
mi_diccionario['profesion'] = 'ingeniero'
print(mi_diccionario)

# eliminar un elemento
del mi_diccionario['ciudad']
print(mi_diccionario)

# obtener claves del diccionario
print(mi_diccionario.keys())

# obtener los valores del diccionario
print(mi_diccionario.values())

#verificar si una clave exista
if 'ciudad' in mi_diccionario:
    print("clave encontrada")

# recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print("[clave: ]",clave,"[valor: ]",valor)