class Calc:
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2
    def mul(n1,n2):
        return n1*n2
    def div(n1,n2):
        return n1/n2
    def mod(n1,n2):
        return n1%n2
    
    
class Math:
    def __init__(abc,val1,val2):
        abc.val1=val1
        abc.val2=val2
    def show(abc):
        print(abc.val1)
        print(abc.val2)
        
    def add(abc,val3):
        print(abc.val1+abc.val2+val3)
    
