### strings ###

my_string = "Mi string"
my_other_string = "mi otro string"
print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un strig con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n Escapado"
print(my_scape_string)

# Formateo
name, surname, age = "Hugo", "Equihua", 15
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))#%S cadenas - %d enteros
print("Mi nombre es " + name + " " + surname + "y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#despaquetado de caracteres
languaje = "python"
a, b, c, d, e, f = languaje
print(a)
print(e)

#divicion
languje_slice = languaje [1:3]# inicio final y salto
print(languje_slice)

languje_slice = languaje[1:]
print(languje_slice)

languje_slice = languaje[-2]#se cuenta de derecha a izquierda
print(languje_slice)

languje_slice = languaje[0:6:2]#2 es la cantidad de letras saltadas
print(languje_slice)

#reverse
reversed_language = languaje[::-1]
print(reversed_language)


#Funciones del lenguaje
#print(languaje.capitalize()) #primera mayuscula
#print(languaje.upper()) #primera mayuscula
#print(languaje.count("t")) #conteo de letras t
#print(language.insnumeric() #el lenguaje es numerico)
#print("1".insnumeric())1 #es numerico
#print(languaje.lower()) #todas minusculas 
#print(languaje.lower().insupper()) #minusculas y luego mayus
#print(languaje.startswith("py")) #empieza en py
#print("PY" == "py") #no es lo mismo
