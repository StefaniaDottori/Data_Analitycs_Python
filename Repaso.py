#inico de repaso variables 

x = 12
y = 1.23
type(x)
type(y)
print(type(x))
print(type(y))

#creacion de listas
nombres = ['Jorge', 'mariana', 'elias', 'josefa']
print(nombres)

nombres.append('rocio')
print(nombres)
nombres[2]
print(nombres[:2])

#repaso ejercicios asignados de clase
 
a = 'Charles'
b = 34
h = 6
print('Mi nombre es', a, 'tengo', b, 'años', 'y tengo', h, 'hermanos')

#otra manera de hacerlo
print('Mi nombre es {}, tengo {} años hasta septiembre y tengo {} hermanos en total'.format(a,b,h))

#data type
x = 1
print(type(x))
y = 'Hola che'
print(type(y))

print('El nombre que usted eligio para este ej es {}'.format(a, type(a)))

num = 1.3455
num2 = '36'
print(int(num), int(num2))

num2 = 3
num4 = '658'
print(float(num2), float(num4))

print(str(num), str(num2))

#existen tres tipos de numeros: entero INT, decimal FLOAT, complejo COMPLEX
x = 2
y = 3.14
z = 1j

print(type(x), type(y), type(z))

print(int(num), complex(num))

#calculos de suma
x= 236
y = 2658
print( x+y)

#resta , suma y division de estos numeros
print(round( x-y))
print(round(x/y))

#area del cuadrado : lado * lado 
lado = 3
area_c = lado * lado
print(area_c)

import math #con esto tenemos acceso a variables matematicas conoci

#calcula circunferencia de radio 2 : pi * radio al 2
r = 2
circunf = math.pi * r**2
print(round(circunf, 3))
print(round(circunf,2))

#Ej de edades en el ano 2000 a hoy
ano_nac = 1986
ano_ref = 2000
edad_2000 = ano_ref - ano_nac
print(round(edad_2000),2)
print(edad_2000)

# con menos lineas de codigo 
mi_edad = 36
mi_edad_2000 = 36 - (2023-2000)
print(mi_edad_2000)

#ejercicio repartija de galletas
n_galletas = 10
n_estudiantes= 15
galleta_est = n_galletas/n_estudiantes
print(round(galleta_est,2))

#nro de caramelos - q no se pueden dividir - refiere a modulo
n_caramelos = 15
print(n_caramelos // 2)

#Boleanos 
elena = 15
jorge = 20
print(elena > jorge) 
print(jorge > elena)
print(elena < jorge)
print(elena == jorge)

#ejercicios Strings  en C-style
x = 12
print('huevos : %d' %(x))
print('Huevos: {}'.format(x))

print(len('abecedario'))
palabra = 'abecedario'
print(palabra.capitalize())
print(palabra.upper())

x = ' m e qui e ro f e  li ci tar p o r e s tu diar e s to'
print(x.replace(' ', ''))

xx = "no quiero aprender python, no quiero pasármelo genial!" 
print(xx.replace('no', 'yo'))

text_python = """Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective."""

print(text_python.count('Python'))

