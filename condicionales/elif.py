ingreso_mensual = int(input("Ingresa tu ingreso mensual: "))
gasto_mensual = int(input("Ingresa tu gasto mensual: "))

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estás bien")
    else:
        print("estás gastando muchisimo!, hay que ver si te alcanza")
    
elif ingreso_mensual > 1000:
    if ingreso_mensual - gasto_mensual < 0:
        print("en deficit")
    elif ingreso_mensual - gasto_mensual > 200:
        print("estás bien")
    else:
        print("estás gastando muchisimo!, hay que ver si te alcanza")

elif ingreso_mensual > 600:
    if ingreso_mensual - gasto_mensual < 0:
        print("en deficit")
    elif ingreso_mensual - gasto_mensual > 100:
        print("estás bien")
    else:
        print("estás gastando muchisimo!, hay que ver si te alcanza")
    
elif ingreso_mensual > 400:
    if ingreso_mensual - gasto_mensual < 0:
        print("en deficit")
    elif ingreso_mensual - gasto_mensual > 50:
        print("preocupante")
    else:
        print("estás gastando muchisimo!, hay que ver si te alcanza")
    
else:
    print("eres pobre")