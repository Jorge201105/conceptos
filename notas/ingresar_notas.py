
def ingresar_notas() -> list[float]:
    """
    solicita al usuario ingresar notas separadas por espacio
      se separan y se transforman en una lista de flotantes
    
    """

    n = input("ingrese las notas (el formato debe ser separado por espaciode esta forma 3.4 4.5 4.6)")
    n = n.split(" ")
    notas = [float(nota) for nota in n]
    return notas
    