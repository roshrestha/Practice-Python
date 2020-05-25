def make_printer(msg):
    name = input("Enter your name: ")
    msg = msg+name
    def printer():
        nonlocal msg
        msg +=' raavan'
        print(msg)
    return printer

myprinter = make_printer("Hello there !!!")
myprinter()
myprinter()
myprinter()
