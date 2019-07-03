arr=[6,6,6,4,4,4,6,4,4,4]
def migratoryBirds(arr):
    count=1
    maxd=1
    b=arr[0]
    a=sorted(arr)
    for i in range(len(arr)):
        if arr[i-1]==arr[i]:
            count+=1
        else:
            if count>maxd:
                maxd=count
                b=arr[i-1]            
            count=1
        if count>maxd:
            maxd=count
            b=arr[len(arr)-1]
        
        print(b)
        return b
    
                
        
        
        
                
               
           
       
       
migratoryBirds(arr)
