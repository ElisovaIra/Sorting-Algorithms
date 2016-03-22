def QuickSort(list, low, high):
    if low < high:
#        print 'Lomuto Partition!'
        pivotLocation = Partition(list, low, high)
        QuickSort(list, low, pivotLocation - 1)
        QuickSort(list, pivotLocation + 1, high)

def Partition(list, low, high):
    pivot = list[high]
#    print 'pivot is:', pivot, 'in list', list[low:high+1]
    newpivot = low 
#    print 'place for pivot is', newpivot, 'unstead of element', list[newpivot]
    for j in xrange(low, high):
        if list[j] <= pivot:
#            print 'swapping', list[j], 'and', list[newpivot] 
            list[j], list[newpivot] = list[newpivot], list[j]
            newpivot = newpivot + 1

    list[newpivot], list[high] = list[high], list[newpivot]
    print 'The result is:\n', ' '.join(map(str, list))
    
    return newpivot 
    

usersize = int(input())

userlist = [int(i) for i in raw_input().strip().split()]

if usersize == 1 : 
        print ' '.join(map(str, userlist))
        exit()
        

QuickSort(userlist, 0, usersize - 1)


