arr=[1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
def migratoryBirds(arr):
    count=[0]*len(arr)
    b=sorted(arr)
    for i in range(len(arr)):
        if b[i-1]==b[i]:
            count[i]+=count[i-1]+1
    
    print(b[count.index(max(count))])
            
    

    
                
        
        
        
                
               
           
       
       
migratoryBirds(arr)
