import random
array = []
for i in range(0,100):
    array.append(int(round(random.random()*10000)))
print array

def bubbleSort(arr):
    sortNum = len(array) - 1
    while sortNum > 0:
        for i in range(0,sortNum):
            if (arr[i] > arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        sortNum -= 1
    print arr

bubbleSort(array)
