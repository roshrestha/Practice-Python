def make_counter():
    count = 0
    def inner():
        nonlocal count
        count +=1
        return count
    return inner
a = make_counter()
for _ in range(10):
    print(a())
