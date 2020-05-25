def make_printer():
    msg = 1
    
    def run():
        nonlocal msg
        msg +=1
        
        print(msg)
    return run
a = make_printer()
a()
a()
