import orient

test_data1 = [
    (1940, 861),
    (1094, 211),
    (257, 857),
    (1096, 1604),
    ]

test_data2 = [
    (1941, 860),
    (1097, 1603),
    (1095, 211),
    (258, 857),
    ]

test_data3 = [
    (1088, 106),
    (1094, 1499),
    (1934, 850),
    (251, 850),
    ]

print(orient.planes(test_data1))
print(orient.planes(test_data2))
print(orient.planes(test_data3))
