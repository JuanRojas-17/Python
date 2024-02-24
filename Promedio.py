n = int(input("Cuantos numeros requieres para sacar el promedio?:"))
lista = []
suma: float = 0.0

a = 1

while a <= n:
   b=int(input("digite un numero:"))
   lista.append(b)
   a += 1
   suma = suma + b
print("El promedio es:", suma / n)