import preguntas as p
import random

def shuffle_alt(pregunta):
    """Mezcla las opciones de pregunta

    Args:
        pregunta (list): lista de preguntas y respuestas

    Returns:
        preg_random: preguntas en diferente orden
    """
    preg_random = pregunta['alternativas']
    random.shuffle(preg_random)
    
    return preg_random

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1']))
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]
    

