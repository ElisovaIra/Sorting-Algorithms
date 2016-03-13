def insertionSort(userlist):
    
    N = 0
    #looping from the left to the right of the list

    for n in xrange(1, usersize):

        #current number greater or equal to a previous number (good! continue to next loop through n)
        
        if userlist[n] >= userlist[n-1]:
            print 'nothing to do with', userlist[n]
            print ' '.join(map(str, userlist))
            continue
          
        #current number less than previous number (bad! need to be sorted)  
       
        else: 
            #let's store current number in a variable, and copy everybody from the left to right on 1 position
            print 'sort!'
            current_lastnumber = userlist[n]
            current_position = int(n)
            print 'number to sort is:', current_lastnumber, 'on position:', current_position
     
            for i in xrange(current_position - 1, -1, -1): 
                if userlist[i] > current_lastnumber :
                    userlist[i+1] = userlist[i]
                    N = N + 1
                    
                    if i == 0 : 
                       userlist[i] = current_lastnumber
        
                else:
                    userlist[i+1] = current_lastnumber
                    break 
            
            print ' '.join(map(str, userlist))
    
    print 'N =', N
        
usersize = raw_input('Enter size:')

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

print 'You entered the list:', userlist

insertionSort(userlist)
