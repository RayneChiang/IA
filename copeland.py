import numpy as np

a = ['1', 'a', 'c', 'e', 'd', 'b']
b = ['1', 'a', 'd', 'c', 'b', 'e']
c = ['1', 'b', 'a', 'e', 'd', 'c']
d = ['1', 'b', 'a', 'd', 'e', 'c']

e = ['1', 'e', 'b', 'a', 'c', 'd']
# e = ['1', 'C', 'B', 'A']
# f = ['1', 'Sp', 'P', 'M', 'Su']
# a = ['1', 'A', 'B', 'D', 'C']
# b = ['1', 'C', 'B', 'D', 'A']
# c = ['1', 'D', 'A', 'C', 'B']
# d = ['1', 'C', 'D', 'A', 'B']
# e = ['9', 'M', 'J', 'T', 'I', 'B', 'A']
# f = ['6', 'A', 'B', 'I', 'M', 'T', 'J']

list = ['a', 'b', 'c', 'd', 'e']
num = len(list) + 1
data = np.array([a, b, c, d, e])


def compare_in_copland(object_1, object_2):
    result_1 = 0
    result_2 = 0
    for i in range(len(data)):
        index_1 = np.where(data[i] == object_1)[0][0]
        index_2 = np.where(data[i] == object_2)[0][0]
        voter = int(data[i][0])
        if index_1 < index_2:
            result_1 += voter
        else:
            result_2 += voter
    if result_1 < result_2:
        win = object_2
    else:
        win = object_1
    print(object_1 + " vs " + object_2 + " : " + str(result_1) + " , " + str(result_2) + " winner " + win)


def compare_in_bordas(object):
    result = 0

    for i in range(len(data)):
        index = num - np.where(data[i] == object)[0][0]
        voter = int(data[i][0])
        result += index*voter
    print(object + " : " + str(result))


for i in range(len(list) - 1):
    for j in range(i + 1, len(list)):
        compare_in_copland(list[i], list[j])

print("/////////////////")

for i in range(len(list)):
    compare_in_bordas(list[i])
