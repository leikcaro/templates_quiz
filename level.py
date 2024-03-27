def choose_level(n_pregunta, p_level):
    """revisa si la pregunta es de cierto nivel

    Args:
        n_pregunta (int): la posicion de la pregunta
        p_level (int: la cantidad de preguntas por nivel

    Returns:
        str: nivel de la pregunta (básica, intermedia, avanzada)
    """
    # Punto de corte 
    if n_pregunta <= p_level:
        level = 'basicas'
    elif n_pregunta <= 2*p_level:
        level = 'intermedias'
    else:
        level = 'avanzadas'
    
    return level


if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(5, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias