"""Write a python program to create a function which expects an unknown number of
arguments."""
def fun(*arguments):
    { 
    
        print(arguments,"length =",len(arguments))
       
    }
fun(5,8,9,1,2,3,4)