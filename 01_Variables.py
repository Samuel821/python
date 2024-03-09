### Variables ###

my_string_variable = "my string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion devariables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("este es el valor de:",my_bool_variable)

# Alguna sfunciones del sistema
print(len(my_string_variable))

# variables en una sola linea. ¡Cuidado con abusar de esta sinaxis
name, surname, alias, age = "Hugo","Equihua Lemus", 'estudiant', 15
print("Me llamo:", name, surname, ". Mi edad es:", age, ". y mi alias es:", alias)



# Inputs
name = input('¿cual es tu nombre?')
age = input('¿cuantos años tienes?')
print(name)
print(age)

#Cambiamos su tipo
name = 15
age = "carlos"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi direccion"
address = True
address = 5
address = 1.2
print(type(address))
