menu = {

    'Dulce':{
       'Torta de chocolate': 7500,
       'Torta de vainilla': 7500,
       'Postre de limon': 5000,
       'Postre de arequipe': 5000,
       'Galleta dulce': 3500,
       'Dulce de leche': 6000,
       'Postre de leche': 5500,
       'Flan': 4750,
       'Alfajores': 5000,
       'Pastel de bocadillo': 7000,
       },

    'Salado': {
       'Pan de queso': 3500,
       'Pan de trigo': 4000,
       'Pan de maiz': 3500,
       'Pan de espelta': 4500,
       'Pan de centeno': 3500,
       'Pan relleno': 6000,
       'Palito de queso': 5500,
       'Pan rollito': 4750,
       'Galletas': 5000,
       'Tarta de queso': 6500,
    },

    'Bebidas': {
       'Limonada': 4000,
       'Batido dulce': 6500,
       'Jugo de mango': 5000,
       'Jugo de uva': 5000,
       'Limonada de panela': 4500,
       'Jugo de frutas': 6000,
       'Cafe': 5000,
       'Tinto': 3000,
       'Granizado': 5750,
       'Frappe': 6500
    }
}

descuentos = {
  'Dulce': ['Torta de chocolate', 'Torta de vainilla'],
  'Salado': ['Pan de queso', 'Pan de trigo'],
  'Bebidas': ['Limonada', 'Batido dulce']
}

print("Bienvenido a la panderia, estas son las categorias disponibles:")

for categorias in menu:
    print("-", categorias)
seleccion = input("Por favor seleccione una categoria:").capitalize()

if seleccion in menu:
    print(f"Estos son los productos en la categoria {seleccion}:")
    print("---Los dos primeros productos cuentan con un 30% de descuento si se compran 2 unidades o más---")

    for producto, precio in menu[seleccion].items():
     print(f"-{producto} / Precio: ${precio}")
    producto = input("Escriba el nombre del producto que desea:").capitalize()

    if producto in menu[seleccion]:
      cantidad = int(input("Escriba la cantidad de su producto que desea:"))
      precio_producto = menu[seleccion][producto]
       
      if producto in descuentos.get(seleccion, []) and cantidad >= 2:
        descuentos = 0.30 * precio_producto * cantidad
        
      else:
        descuentos = 0

      sin_descuento = precio_producto * cantidad
      con_descuento = sin_descuento - descuentos

      print(f"Usted va a comprar: {cantidad} unidades del producto de {producto}")
      print(f"Costo total sin descuento: ${sin_descuento}")
      print(f"Descuento aplicado ${descuentos}")
      print(f"Costo total con descuento: ${con_descuento}")

      dinero = int(input("¿Con cuanta plata va a pagar?:"))

      if dinero < con_descuento:
        print("Plata insuficiente")
      else:
        print("---Perfecto, muchas gracias por su compra. Vueltos:$", dinero - con_descuento)

    else:
      print("Lo lamento. Su producto no existe")

else:
 print("Lo lamento. La categoria no esta disponible")