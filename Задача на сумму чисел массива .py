def sum_array(a):
    storage = []
    for i in range(len(a)):
        storage.append(a[i])
    return sum(storage)


def new_array(a):
    return sum(a)

array = [1,1]
array2 = [1,1]


def array_plus_array(arr1,arr2):
    storage = []
    for i in range(len(arr1)):
        storage.append(arr1[i])
    for z in range(len(arr2)):
        storage.append(arr2[z])
    return sum(storage)

def array_new_array(arr1, arr2):
    return sum(arr1 + arr2)

print(array_plus_array(array,array2))