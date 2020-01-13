class Shape:
    global shape 
    
    shape = {"cirlce", 'triangle', 'square'}
    def __init__(self,name, width, height):
        self.name = name
        self.width = width
        self.height = height
        
    def initialize(self, name=0, width=0, height=0):
        self.name = name
        self.width = width
        self.height = height
        
    
    @property
    def peremeter(self):
        p = self.width * self.height
        return ("Peremeter of {} is equal to {}").format(self.name, p)
        
    
    
    @peremeter.setter
    def peremeter(self, shape_info=0):
        self.name = name
        self.width = width
        self.height = height

    if __name__ == '__main__':
        name = input("Please input the name of the shape  ")
        width = int(input("Please input the width of the shape  "))
        height = int(input("Please input the height of the shape  "))
        a = Shape(name, width,height)
        print(a.peremeter)
        
