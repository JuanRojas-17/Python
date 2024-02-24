numero = int(input("Introduzca su numero:"))

if numero>1:

  for p in range(2, numero//2+1):
#ya que un numero no puede ser dividido por mas de su mitad, tenemos que asegurarnos de mirar los
#divisores hasta su limite. Por ejemplo: 20/2 = 10 +1 = 11. Se analizan los numeros desde 2 hasta 11
    if numero%p== 0:
      print("Tu numero no es primo")
      break

  else:
      print("Tu numero si es primo")
else:
  print("Tu numero no es primo")