### Tuples ###

# Definicion

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "fermin", "garcia", "profesor")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

# acceso a elementos y busqueda

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[5])
#print(my_tuple[-6])

print(my_tuple.count("fermin"))
print(my_tuple.index("garcia"))
print(my_tuple.index("profesor"))

#my_tuple[1] = 1.80 #'tuple' objet does not suport item asignament
# en las tuplas el valor no puede ser cambiado

#concatenacion

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

#suptuplas

print(my_sum_tuple[3:6])

#tupla mutable con comversion a lista

my_tuple = list(my_tuple)
print(type(my_tuple))


my_tuple = (35, 1.77, "fermin", "garcia", "profesor")
my_other_tuple = (35, 60, 30)

my_tuple[4] = "CECyTEM"
my_tuple.insert(1, "azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# eliminacion

#del my_tuple[2] #TypeError: 'tuple' objet doesn't support  item deletion

del my_tupla
# print(my_tuple) #nameerror: name my 'tuple' is not definied
