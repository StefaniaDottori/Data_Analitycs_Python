'''Crea una lista con el nombre de 4 personas.
Agrega una persona mas a la lista ya creada y que aparezca en el segundo lugar.
Genera una lista nueva con los últimos dos nombres de tu lista anterior y únela a tu lista 
anterior.
Utiliza una función para determinar cuantos elementos tienes en la lista
Borra el 3er elemento de la lista
Genera una lista de listas utilizando la lista anterior y donde las listas internas estan 
conformadas por las letras separadas que conforman los dos primeros nombres. 
Pista: La función list() aplicada a un string.
'''

list_A = ['John', 'Joe', 'Mary', 'Tommas']
print(list_A)

list_A.insert(1, 'Paul')
print(list_A)

list_B = list_A.copy()
print(list_B)

list_B.extend(list_A[-2::]) 
print(list_B)

print(len(list_B))

list_B.pop(3) #'Mary' deleted - position 3
print(list_B)

final_list = list((list(list_B[0]), list(list_B[1]), list(list_B[2]), list(list_B[3]), list(list_B[4])))
print(final_list)

'''Genera un diccionario con 3 ciudades como keys y su número de habitantes. Una de las ciudades debe ser Barcelona.
Devuelve el valor de cada etiqueta y obtiene el número total de habitantes sumando todas las ciudades.
Al mismo diccionario, agrega una ciudad con su número de habitantes.
Construir un diccionario anidado solo en la key Barcelona que tenga su num de habitantes y PIB.
Borra los valores de Barcelona del diccionario'''

dict_A = {'Barcelona' : 2.5 , 
       'Madrid' : 5.5, 
       'Sevilla' : 1.2}
print(dict_A)

print(dict_A.values())

total_hab = sum(dict_A.values())
print(total_hab)

dict_A['Bilbao'] = 0.8
print(dict_A)

dict_A['Barcelona'] = {'population' : dict_A['Barcelona'], 'PBI' : 3.25}
print(dict_A)

dict_A.pop('Barcelona')
print(dict_A)

'''Ejercicio: Escribir un programa que guarde en una variable el 
diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una 
divisa y muestre su símbolo o un mensaje'''

currency_dic = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

print('Introduce la divisa del diccionario:')
divisas = input()



'''Ejercicio: Escribir un programa que cree un diccionario vacío y lo vaya llenado con 
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo 
electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe 
imprimirse el contenido del diccionario.'''

user_data = {}

print('Tipo de informacion')
tipo = input()
print('Dato de la informacion')
data = input()
user_data[tipo] = data

print(user_data)