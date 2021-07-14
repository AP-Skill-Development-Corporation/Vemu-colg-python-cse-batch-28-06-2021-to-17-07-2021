def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def leapyear(start,end):
    for year in range(start,end+1):
        if year%400==0 or (year%4==0 and year%100!=0 ):
            print(year,end= " ")
            