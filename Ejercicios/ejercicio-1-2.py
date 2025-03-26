import time

temperaturas = []
tiempos = []
limite_registros = 7  
tiempo_limite_minutos = 1  # Cambia esto para definir cuántos minutos deben pasar

while True:
    temp = input("Ingresa una temperatura (o 'salir' para terminar): ")

    if temp.lower() == "salir":
        break  

    if len(temperaturas) >= limite_registros:
        print("⚠️ No se pueden ingresar más temperaturas.")
        continue  

    temperaturas.append(temp)
    tiempos.append(time.time())  # Guardamos la hora actual

    tiempo_actual = time.time()
    
    for i in range(len(tiempos)):
        diferencia_minutos = (tiempo_actual - tiempos[i]) / 60  # Convertimos segundos a minutos

        if diferencia_minutos >= tiempo_limite_minutos:
            print(f"⚠️ La temperatura '{temperaturas[i]}' fue ingresada hace {diferencia_minutos:.2f} minutos.")

print("\nTemperaturas registradas:", temperaturas)
print("Programa finalizado.")
