class fat():
    def __init__(self,x):
        self.x = x
        self.A=[]
        for y in range(2,x):
            while x%y==0:
                x=x/y
                self.A.append(y)
        if sum(self.A)==0:
            self.A.append(x)
        for i in self.A[::-1]:
            print(i, end=' ')
a = fat(3960)
