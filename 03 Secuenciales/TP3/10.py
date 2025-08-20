hemisferio : str = str(input("Ingrese hemisferio:(sur S o norte N)").upper())
mes : int = int(input("¿Qué mes es?(1-12)"))
dia : int = int(input("¿Què día es?(1-31)"))

if (hemisferio == "N"):
    if (mes, dia) >= (12, 21) or (mes, dia) <= (3,20):
        estacion = "Invierno"
    elif (mes, dia) >= (3, 21) or (mes, dia) <= (6,20):
        estacion = "Primavera"
    elif (mes, dia) >= (6, 21) or (mes, dia) <= (12,20):
        estacion = "Verano"
    else: 
        estacion = "Otoño"

if (hemisferio == "S"):
    if (mes, dia) >= (12, 21) or (mes, dia) <= (3,20):
        estacion = "Verano"
    elif (mes, dia) >= (3, 21) or (mes, dia) <= (6,20):
        estacion = "Otoño"
    elif (mes, dia) >= (6, 21) or (mes, dia) <= (12,20):
        estacion = "Invierno"
    else: 
        estacion = "Primavera"
    
    print(f"La estación es: {estacion}")