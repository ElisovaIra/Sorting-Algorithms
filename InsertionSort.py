def insertionSort(userlist):
    lastnumber = userlist[usersize - 1]
    print 'last number is:', lastnumber
#    print ' '.join(map(str, userlist))
     
    for n in xrange(usersize - 2, -1, -1) : 
        
        if userlist[n] > lastnumber :
            print lastnumber, '<', userlist[n]
            userlist[n + 1] = userlist[n]
            if n == 0 : 
                print ' '.join(map(str, userlist))
                userlist[n] = lastnumber
        
        else:
            print lastnumber, '>', userlist[n]
            userlist[n+1] = lastnumber
            print ' '.join(map(str, userlist)) 
            break 
                 
        print ' '.join(map(str, userlist))

usersize = raw_input('Enter list size:')

if usersize == '0' : 
    print 'List should be longer than 0'
    exit()
    
try:
    usersize = int(usersize)
    
except:
    print 'Error! Please enter only numbers'
    usersize = None
    exit()

userlist = [int(number) for number in raw_input('Enter list:').strip().split()]

print 'You entered the size:', usersize
print 'You entered the list:', userlist

insertionSort(userlist)