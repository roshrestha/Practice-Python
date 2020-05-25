class Summer():
    def __init__(self):
        self.data = []
    def __call__(self, val):
        self.data.append(val)
        _sum = sum(self.data)
        return _sum
    
summer = Summer()
summer(12)
summer(12)
summer(45)
print(summer(13))
print(summer.data)
