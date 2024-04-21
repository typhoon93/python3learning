class Cookie:
    
    def __init__(self, color): #constructor
        self.color = color
        
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        

cookie_one = Cookie('green')
cookie_two = Cookie('blue')
print(cookie_one.get_color())
print(cookie_two.get_color())

#example for a linked list class & methods
class LinkedList:
    def __init__(self, value):
        pass
    
    def append(self, value):
        pass
    def pop(self):
        pass
    def prepend(self, value):
        pass
    def insert(self,index, value):
        pass
    def removed(self, index):
        pass
    
