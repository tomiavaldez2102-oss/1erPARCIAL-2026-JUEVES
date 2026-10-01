def recursiva(a,b):
    if a < 0:
        raise ValueError('Las interrupciones por hora no puede ser negativas')
    if b < 0:
        raise ValueError('Las horas de la tarde no puede ser negativas')
    if a ==0 :
        return 0
    if b == 0:
        return 0
    if a > 0:
        return a + recursiva(a, b-1)
    return recursiva

