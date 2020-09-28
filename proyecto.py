from colorama import Fore, Back, Style

cl = float(input(Back.BLUE + "Ingrese un Numero->"))
ls = float(input("Ingrese otro Numero->"))

print(Back.RED + "S = Suma")
print("M = Multiplicacion")
print("D = Division")
print("R = Resta")

t = str(input(Back.GREEN + "Ingrese una S,M,D,R->")).upper()

if t =='S':
	suma = cl+ls
	print(suma)
elif t =='M':
	multi = cl*ls
	print(multi)
elif t =='D':
	divi = cl/ls
	print(divi)
elif t =='R':
	resta = cl-ls
	print(resta)
else:
	print("La letra ingresada es Incorrecta")