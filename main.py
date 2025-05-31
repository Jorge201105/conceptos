# sistema de notas
# 1 ingresar notas
# calcular estadisticas de notas
#notas mas bajas
#cantidad de aprobados
# menu

def menu():
    print("""
Menu
1. ingresar notas
2. calcular estadisticas de notas
3. notas mas bajas
4. cantidad de aprobados
""")

def main():
    notas = []

    while True:
        menu()
        opcion = input("ingrese una opcion")
        if opcion== "1":
            n = input("ingrese las notas (el formato debe ser separado por espaciode esta forma 3.4 4.5 4.6)")
            n = n.split(" ")
            notas = [float(nota) for nota in n]
            print(notas)
        elif opcion == "2":
            try:    #promedio
                #mayor
                #menor
                #aprobado
                promedio = sum(notas)/len(notas)
                mayor = max(notas)
                menor = min(notas)
                aprobado = [a for a in notas if a>= 4]
                print(aprobado)
            except ZeroDivisionError:
                print("No hay notas agregadas")
                


        elif opcion == "3":
            print(f"""
promedio : {promedio}
minimo : {menor}
mayor : {mayor}
aprobados : {aprobado}





""")
            
        else:
            print("terminado")
            break
        

if __name__ == "__main__": 

    main()


