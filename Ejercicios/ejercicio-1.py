import time #para manejar tiempos reales
temperaturas = []
tiempos = []
limite_registros = 7  #establece un límite de 7 temperaturas que se pueden ingresar
tiempo_limite_minutos = 1  # Cambia esto para definir cuántos minutos deben pasar

#iniciamos el bucle while para recibir temperaturas 

while True: #se usa para mentener el programa en ejecución hasta que el usuario decida salir
    temp = input("Ingresa una teperatura (o 'salir' para terminar): ") #el input solicita al usuario que ingrese una temperaturo y si el usuario escribe "salir", el programa termina.
    
    if temp.lower() == "salir":  #temp.lower() convierte el texto ingreso a minúsculas para evitar problemas con Salir o SALIR
        break #si el usuario escribió "salir", el break detiene el chile, terminando el programa. 
    
    if len(temperaturas) >= limite_registros: #len(temperaturas) obtiene la cantidad de temperaturas ingresadas, si hay 7, se muestra un mensaje de advertencia
        print("No se puede ingresar más temperaturas.")
        continue #evita que el código siga ejecutandose y vuelva  a pedir otra temperatura
    
    temperaturas.append(temp) #guarda la nueva temperatura en la lista 
    tiempos.append(time.time()) #guardamos la hora exacta
    
    tiempo_actual = time.time() #revisar si alguna temperatura tiene más de 24 horas
    
    for i in range(len(tiempos)): #for para recorrer todos los valores de la lista tiempos
        diferencia_minutos = (tiempo_actual - tiempos[i]) / 60 #convertimos segundos a minutos
        #tiempos[i] += 1 #simulamos el paso del tiempo. Aumenta el tiempo de cada temperatura en 1 hora simulada
        
        # if tiempos[i] >= 24:}
        if diferencia_minutos >= tiempo_limite_minutos: 
            print(f"La temperatura '{temperaturas[i]}' fue ingresada hace{diferencia_minutos: .2f}.")

print("\nTemepraturas registradas:", temperaturas)
print("Programa finalizado.")