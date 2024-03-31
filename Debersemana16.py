#Crea un nuevo archivo llamado my_notes.txt.
my_notes = open('my_notes.txt', 'w')
#Método write(): escribir una linea a la vez
my_notes.write('1.Nilson Alexis López Miranda.\n')
my_notes.write('2.Estudiante de la carrera de tecnologias de la información\n')
#Método writelines(): escribir una line
lineas = ['3:Cedula.-0605563421.\n', '4:Vivo en la ciudad del Puyo.\n']
my_notes.writelines(lineas)
#abre el archivo my_notes
my_notes =open('my_notes.txt', 'r')
#lee el contenido linea por linea
#Metodo 1.  read()
print('Metodo 1: read()')
print('------------------------')
print(my_notes.read())
my_notes.close()
#Metodo 2.  readlines()
my_notes =open('my_notes.txt', 'r')
print('Metodo 2: readlines()')
print('------------------------')
for linea in my_notes.readlines():
    print(linea.rstrip('\n'))
my_notes.close()



