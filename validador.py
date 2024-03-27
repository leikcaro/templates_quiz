
def validate(opciones, eleccion):
    """valida que la elección esté dentro de las opciones disponibles 

    Args:
        opciones (list): lista de opciones disponibles
        eleccion (str): la elección escogida

    Returns:
        eleccion: la elección escogida validada
    """
         
    while eleccion not in opciones:
        print('Opción no válida, ingrese una de las opciones válidas: ')
        eleccion = input('Ingresa una Opción: ').lower()  
            
    return eleccion




if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(letras, eleccion)
    
    
