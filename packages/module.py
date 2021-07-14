def leapyear(start,end):
    for year in range(start,end+1):
        if year%400==0 or (year%4==0 and year%100!=0 ):
            print(year,end= " ")
            
            

# duplicates[20,30,40,30,20,36,29,20,1,2,3,4,5]   =====>[1,2,3,4,5,20,30,40,36,29]

def duplicates1(iteration1):
    li=[]
    for i in iteration1:
        if i not in li:
            li.append(i)
            
    print(li)
            
            
            
            
            
def evenorodd(n):
    if n%2==0:
        return "EVEN"
    else:
        return "ODD"
    
    

