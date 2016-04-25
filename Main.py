from Funciones.Modulos import *

op = raw_input("Seleccione el ejercicio que desea realizar:")


if op == 'a':
	k = int(input("Ingrese un numero: "))


elif op == 'b':
	n = input("Ingrese un numero natural n :")
	s = suma(n)
	print ("La suma de los %s numeros naturales es %s "%(n,s))

elif op == 'c' :
	m=int(input("ingrese un NUmero"))
	resto=int(m%2)

	if resto==0:
			PAR(m)
	else:
			IMPAR(m)


elif op == 'd':
	ba= int (raw_input("ingrese un numero: "))
	exp= int (raw_input("ingrese un numero: "))
	print(exponente(ba,exp))


elif op == 'e':
	numero = int (input("Inserta un numero: "))
	print factorial(numero)


elif op == 'f':
	radio = input("Ingrese el Radio para el Cono:")
	gen = input("Ingrese la generatriz del Cono:")
	print areaCono(radio,gen),"m2"


elif op == 'g':
	caracter = raw_input("Ingrese un un caracter :")
	mayus= mayuscula(caracter)

	print("Letra obtenida: % s" %(mayus))


elif op == 'h':

	n = int (input ('ingrese un numero '))
	prom(n)


elif op == 'i':
	n= int(input("Ingrese un numero: "))
	Perfecto(n)


elif op == 'j':
	x = int(raw_input("Ingrese un numero: "))
	suma(x)


elif op == 'k':
	valor = int(input("Ingrese numero:"))		
	z = armonico(valor)				
	print (z)



elif op == 'l':
	lengLado = input("Ingrese valor de longitud de lado del cuadrado :")
	perimetro = calPerimetro(lengLado)
	area = calArea(lengLado)

	print ("El perimetro del cuadrado es %s" %(perimetro))
	print ("El area del cuadrado es %s" %(area))


elif op == 'm':
	l1 =int(input ('ingrese un valor L1 '))
	l2 = int(input('ingrese un valor L2 '))
	z = int(input('ingrese un numero: '))

	rango(l1,l2,z)


elif op == 'n':
	x = int(input ("ingrese numero a convertir: "))
	Conversion(x)


elif op == 'o':
	a = int(raw_input("Ingrese un numero: "))
	b = int(raw_input("Ingrese un numero: "))
	c = int(raw_input("Ingrese un numero: "))

	suma(a,b,c)

elif op == 'p':
	print digito(15)


elif op == 'q':
	x = int(raw_input("Ingrese un numero: "))
	y = str(raw_input("Ingrese una cadena: "))

	verificador(x,y)

elif op == 'r':
	y = 2
	resto = 1
	n =int (input ('ingrese un numero '))
	while (resto != 0 ) and (y < n):
		resto = n % y
		y = y + 1 

	if resto==0:
		print ('el numero ingresado no es primo ')
		multiplo(n)
	else:
		print ('el numero ingresado es primo ')
		print ("Su factorial es ",factorial(n))




elif op == 's':
	a = int (raw_input ("ingrese una edad: "))
	b = int (raw_input ("ingrese una edad: "))
	Edades(a,b)

else :
	print ("Opcion ingresada no valida")