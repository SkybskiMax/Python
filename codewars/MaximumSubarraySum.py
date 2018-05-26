arr = [-2,1,-3,4,-1,2,1,-5,4]

def maxSequence(arr):
    if is_negative(arr):
        return 0
    max=sum(arr)
    idx=0
    for i in arr:
        idx+=1
        sum_seq=0
        for j in arr[idx-1::]:
            sum_seq+=j
            if sum_seq > max:
                max=sum_seq
            print(sum_seq)
    return max

def is_negative(arr):
    for i in arr:
        if i < 0:
            pass
        else:
            return 0
    return 1

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
