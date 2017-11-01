import itertools, math

def planes(data):
    pairs = list(map(tuple, itertools.combinations(data, 2)))
    def distance(i, j): return math.hypot(i[0] - j[0], i[1] - j[1])
    sorted_distances = sorted([(i, distance(i[0], i[1])) for i in pairs], key=lambda tup: tup[1], reverse=True)
    return({'length': sorted_distances[0][0], 'width': sorted_distances[1][0],})
