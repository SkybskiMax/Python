x=[1,2,3,4,5,6,7,8,9,10]
target=8

def binary_search(array,target):
    n=len(array)
    min = 0
    max = n-1
    while(min<max):
        avg=(max+min)//2
        if array[avg]==target:
            return avg
        if array[avg]>target:
            max = avg
        else:
            min = avg

print(binary_search(x,target))
