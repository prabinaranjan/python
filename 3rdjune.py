'''class calculator:

    def sum(self,a,b):
        return a+b
    def mul(self,a,b):
        return a*b
#class call
object=calculator()
print(object.sum(1,2))
print(object.mul(1,2))'''

#call by value
# #call by reference

'''class myclass:
    def __init__(self,name,age,):
        self.name=name
        self.age=age
    def find(self,name):
        if(name==self.name):
            return True
        else:
            return False
obj=myclass("praveen", "26")
print(obj.find("praveen"))'''


'''class myclass:
    def __init__(self,num):
        self.num=num

    def sum(self,num):
        self.num=num+num
        return self.num+num

obj=myclass(1)
print(obj.sum(1))
'''

'''class myclass:
    def __init__(self,num):
        self.num=num
        self.div(num)
    def sum(self,num):
        num=num+self.num
        return self.num+num
    def mult(self,num):
        return self.sum(num)
    def div(self,num):
        self.num=self.num-num
        num=self.sum(num)
        return num
obj=myclass(1)
print(obj.sum(1))'''

t


