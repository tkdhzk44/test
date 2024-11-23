class MyClass:
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
    def method1(self):
        adding = self.a1 + self.b1
        return adding
    def method2(self):
        subbing = self.a1 - self.b1
        return subbing
    def method3(self, n, m):
        self.multi = n * m
        return self.multi
    
mc = MyClass(2, 3)
ans = mc.method1()
print(ans)
print(mc.method3(2, 10))
print(mc.a1, mc.b1)

# 
class Mycalss:
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
    def method1(self):
        adding = self.a1 + self.b1
        return adding
    def method2(self):
        subbing = self.a1 - self.b1
        return subbing
    def method3(self, n, m):
        self.multi = n * m
        return self.multi

    mc = MyClass(3, 8)
    ans = mc.method1()
    print(ans)
    print(mc.method3(3,10))
    print(mc.a1, mc.b1)

    # 
class Myclass:
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
    def method1(self):
        adding = self.a1 + self.b1
        return adding
    def method(self):
        subbing = self.a1 - self.b1
        return subbing
    def method3(self, n, m):
        self.multi = n * m
        return self.multi
    mc = MyClass(2, 2)
    ans = mc.method1()
    print(ans)
    print(mc.method3(3, 10))
    print(mc.a1, mc.b1)