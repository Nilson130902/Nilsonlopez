#creacion de un diccionario
informacion_personal = {
    'Nombre':'Nilson',
    'Edad':21,
    'Ciudad':'Puyo',
    'Provincia':'Pastaza'
}
print('----------------------')
print('Diccionario principal')
for key, value in informacion_personal.items():
    print(f'{key}: {value}')

#Accede al valor asociado con la clave "ciudad"
# y modifícalo con una ciudad diferente.
informacion_personal['Ciudad'] = 'Quito'
informacion_personal['Nombre'] = 'Alexis'

#Ingreso de una nueva clave
informacion_personal['Profesion']= 'Estudiante'

#Verifica si la clave "telefono" existe en el diccionario.
# Si no existe, agrégala con un número de teléfono ficticio.
if 'Telefono' not in informacion_personal:
    informacion_personal['Telefono']= '0987654321'

#Elimina la clave "edad" del diccionario,
# ya que esa información no es necesaria.
informacion_personal.pop('Edad')

print('----------------------')
print('Diccionario Modificado')
print('----------------------')
for key, value in informacion_personal.items():
    print(f'{key}: {value}')