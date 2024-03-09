### Lists ###

# Definicion

my_list = list()
my_oter_list = []
prnt(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Fermin", "garcia"]

print(type(my_list))
print(type(my_other_list))

# acceso a elementos y busqueda

print(my_oter_list[0])
print(my_oter_list[1])
print(my_oter_list[-4])
print(my_oter_list[30])
#print(my_oter_list[4]) # index error
#print(my_oter_list[-5]) # index error

print(my_oter_list.index(fermin))

age, height, name, surname = my_other_list
print(name)

name, heigt, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]

# concatenacion

print(my_list + my_other_list)
#print(my_list - my_other_list)


#creacion , insercion, actualizacion y eliminacion

my_other_list.append("CECYTEM")
print(my_other_list)

my_other_list.insert(1, "rojo")
print(my_other_list)

my_other_list[1] = "azul"
print(my_other_list)

my_other_list.remove("azul")
print(my_other_list)

my_list.remove(30)

my_list = [35, 24, 62, 52, 30, 30, 17]
my_other_list = [35, 1.77, "Fermin", "garcia"]

# opeeraciones con listas
my_new_list = my_list.copy()

my_list.clear()
print(my_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print()my_new_list)

#sublistas

print(my_new_list[1:3])

#cambio de tipo

