class Example:
    def __init__(self):
        print("Instance created")
    # Defining __call__method which enables the instance to be 
    # called like a function
    def __call__(self):
        print('Instance is called via special method')
    
# Instance created
e = Example()
# __call__method will be called
e()