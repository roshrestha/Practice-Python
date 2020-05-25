'''
__call__ in Python enables us to write classes where the 
instances behave like functions and can be called like a function. 
When the instance is called as a function; if this method is defined 
as x.__call__(arg1, arg2,....)
object() is shorthand for object.__call__()

'''
class Product:
    def __init__(self):
        print("Instance created")
        
    #Defining call method
    def __call__(self, a,b):
        print(a*b)

ans = Product() #Instance created
ans(10,20) #calling __call__method is same as ans.__call__(10,20)
ans.__call__(10,20)

