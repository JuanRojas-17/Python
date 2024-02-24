numero = int(input("Introduzca su numero:"))

factorial = 1
f = 1
while f <= numero:
    factorial = factorial * f
    f += 1

print ("La factorial de", numero, "es:", factorial)
