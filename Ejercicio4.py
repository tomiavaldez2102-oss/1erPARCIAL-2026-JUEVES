i = ['kermes', 'partido', 'fiesta', 'aterrizaje','concierto']

def organizacion(i,ii = False):
    if ii == True:
        i.sort(reverse =True)
    else:
        return sorted(i)