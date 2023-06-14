
class student:
    
    def __init__(self,name,age):
            #public 
            self.name   = name
            # private
            self.__age    =  age    
    
    def get_data(self):
        print(self.name, self.__age)
        
    def set_data(self,age):
        self.__age = age
        
sud1 = student('Hruthik',23)

# accessing the data :
print('befor  update')
sud1.get_data()
sud1.set_data(44)
print('After update')
sud1.get_data()