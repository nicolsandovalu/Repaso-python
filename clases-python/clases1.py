productos = "galletas"
stock = int(input(f"Ingrese cantidad de {productos}:")) #la f y {variable} son para llamar a la variable

if stock >= 20:
    print("Revisar fecha de caducidad de los productos") 
elif stock >= 5 :
    print("Hay productos suficientes")
elif stock > 0:
    print("Quedan pocas existencias")
else:
    print("No hay existencias")

for precio in range (1000, 500):
    print(f"Precio del producto: ${precio}")
