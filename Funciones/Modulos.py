#Ejercicio a)
def printNat(k):
	for i in range(k):
		print(i+1)

#Ejercicio b)
def suma(n):
	total = 0
	for i in range (1,n+1):
		total += i
	return total

#Ejercicio c)
def PAR(npar):
	for x  in range(2,npar+2,2):
		print(x)
def IMPAR(rimpar):
	for x in range(1,rimpar+2,2):
		print(x)


#Ejercicio d)
def exponente(base,exponente):
	contador = 1
	if exponente != 0:
		resultado=base
		contador = contador +1
		while contador <= exponente:
			resultado= resultado * base
			contador= contador + 1
		return resultado
	else:
	     base = 1
	     return base

#Ejercicio e)
def factorial (x):
	total=1
	while x > 1:

		total = total * x
		x = x - 1
	return total

#Ejercicio f)
def areaCono(radio,gen):
	resultado = (3.14*radio*gen) + 3.14*(radio**2)
	return round (resultado,2)


#Ejercicio g)
def mayuscula(c) :

	if c == c.upper() :
		print("EL caracter ingresado ya esta en mayuscula")
		return c

	else :
		return c.upper()


#Ejercicio h)
def prom(m):
	suma=int(0)
	for x in range(1,m+1) :
		suma = suma + x
	
	promedio = float(suma / m)

	print("el promedio es", promedio)


#Ejercicio i)
def Perfecto(n):
	suma=0
	for i in range(1,n):
		if (n % i == 0):  
			suma = suma + i
	if (n == suma):
		print"el numero es perfecto"
	elif (n> suma):
		print "el numero es deficiente"	
	else:
		print "el numero es abundante"



#Ejercicio j)
def suma(x):
	n = 1
	p = 0
	i = 0
	while n <= x:
   		if n%2 == 0:
			p += n
		else:
			i += n
		print n,
		n += 1
   	print '\nLa suma de los pares es igual a %i' % p
	print 'La suma de los impares es igual a %i' % i


#Ejercicio k)
def armonico(n):
	resultado = 0			
	for i in range(1,n+1):
		resultado = resultado + 1/i

	return resultado


#Ejercicio l)
def calPerimetro(a) :
	perimetro = a * 4
	return perimetro

def calArea(a) :
	area = a ** 2
	return area


#Ejericio m)
def rango(p1,p2,x):
	ver = bool
	ver= False

	for a in range(p1,p2+1):
		if a == x :
			ver = True 

	if ver :
		print ('el numero ingresado esta dentro del rango')

	else:
		if x < l1 :
			print ('el numero ingresado esta a la izquierda del rango,')
		else :
			print ('el numero ingresado esta a la derecha del rango, ')


#Ejercicio n)
def Conversion(x):
     r1= x * 3.28 
     r2= x * 39.27
     
     print "convertido a pies es: %s" %(r1)
     print "convertido a pulgadas es: %s" %(r2)



#Ejercicio o)
def suma(a,b,c):
	if a + b == c:
		print (c,"es la suma de",a, b)
	if b + c== a:
		print (a,"es la suma de",b, c)
	if c + a== b:
		print (b,"es la suma de",c, a)

#Ejercicio p)
def digito(n):
	resultado = 0
	resg = n
	for i in range(len(str(n))):
		resultado = resultado + (resg%10)*(10**i)
		resg = resg // 10

	return resultado


#Ejercicio q)
def verificador(x,y):
	
	if x == len(y):
		print("La cadena %s tiene la misma cantidad de letras que se indica en el numero %s" %(x,y))

	else:
		print("La cadena %s NO tiene la misma cantidad de letras que se indica en el numero %s" %(x,y))



#Ejercicio r)
def factorial(x):

	fac = int (1)
	for a in range (1,x+1):
		fac = fac * a
	
	return(fac)
	
def multiplo(x):
	i=int(1)
	mult=x*i
	while (mult<1000):
		print(mult)
		i=i+1
		mult=x*i



#Ejercicio s)
def Edades(a,b):
	if a > b :
		falta = a - b
   		print a,"es mayor que",b
   		print "lo que falta a",b,"para llegar a",a,"es: ",falta

	else:
		falta = b - a
		print a,"es menor que",b
		print "lo que falta a",a,"para llegar a",b,"es: ",falta
