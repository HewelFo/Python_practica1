# problema 1.2 hewel.ochoa@utp.ac.pa
def cadenareversa(arg):
	arg.reverse()
	return arg
def combinalista(arg, argN):
	for s in range(len(argN)):
		arg.append(argN[s])
	return arg

print("ingrese su numero, para terminar ingrese YA")
arg_take = input(":")
arg_cero = [arg_take]
i=0
while arg_take != "YA":
	if ( i == 0):
		arg_cero[i] =int(arg_take)
	else:
		arg_cero.append(int(arg_take))
	arg_take = input(":")
	i += 1
print(cadenareversa(arg_cero))

print("ingrese su numero en la segunda cadena, para terminar ingrese YA")
arg_take = input(":")
arg_uno = [arg_take]
i=0
while arg_take != "YA":
	if ( i == 0):
		arg_uno[i] =int(arg_take)
	else:
		arg_uno.append(int(arg_take))
	arg_take = input(":")
	i += 1
print(combinalista(arg_cero, arg_uno))


