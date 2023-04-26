import numpy

def cores_aleatorias():
    color = list(numpy.random.choice(range(256), size=3))
    return color
