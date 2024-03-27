import preguntas as p


def verificar(alternativas, eleccion):
    """permite comprobar si la respuesta entregada por el usuario es correcta.

    Args:
        alternativas (str): las opciones que el usuario puede tomar
        eleccion (str): la opcion elegida por el usuario

    Returns:
        int: devuelve 1 si la respuesta es correcta y 0 si no lo es
    """
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    
    for i, dato in enumerate(alternativas):
        # print(dato[1])
        if dato[1] == 1:
            if i == eleccion:
                # print("Respuesta correcta")
                contador_respuesta = 1   
            else:
                # print('Respuesta incorrecta')
                contador_respuesta = 0



    return contador_respuesta




if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






