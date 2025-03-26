
productos = int(input("Ingrese número de productos: "))

print("Stock en casino:")
for i in range(productos):   #i indice del arreglo y range
    print(i)
    if i > 5:  # Aplicar descuento solo a los productos mayores a 3000 pesos
        print(f"La cantidad de productos es {i} {productos}")
    else:
        print("No hay suficientes productos")

"""
# Ejemplo de bucle for sin estructuras de datos
print("--- Revisando stock de productos ---")
numero_productos = int(input(f"Ingrese número de productos para revisión de stock: "))

for i in range(numero_productos):
    print(f"Verificación número {i + 1} realizada.")
    #agregar un if por producto"""

