def make_summer():
    data = []
    def summer(val):
        data.append(val)
        _sum = sum(data)
        
        return _sum
    return summer

a = make_summer()
b = a(12)
b = a(14)
b = a(15)
b = a(78)
print(b)
