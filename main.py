from notas.menu import menu
from notas.ingresar_notas import ingresar_notas
# from notas import *        asi importo todo de la carpeta notas
from notas.calculos import calcular_estadisticas



def main():
    notas = []

    while True:
        menu()
        opcion = input("ingrese una opcion")
        if opcion== "1":
            notas = ingresar_notas()
            print(f"notas ingresadas {notas}")
           
        elif opcion == "2":
           if calcular_estadisticas(notas) == None:
               print("no se agregaron notas por favor agreguelas!!!")
               notas = ingresar_notas()               
           estadisticas = calcular_estadisticas(notas)
          


        elif opcion == "3":       
            print(estadisticas) 

        else:
            print("terminado")
            break
        

if __name__ == "__main__": 

    main()


