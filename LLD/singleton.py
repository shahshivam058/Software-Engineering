class Singleton :
    _instance = None 
    
    @classmethod
    def get_instance(cls):
        if  not cls._instance :
            cls._instance =  super().__new__(cls)
        return cls._instance

s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

"""
Here in above when we create only object and comparing it will return False as we are not restriction on creation 


s1 = Singleton() 
s2 = Singleton()

both s2 and s1 will be diff object we need to call get instance method to get the the same object 
"""

print(s1 is s2)


class Singleton :
    _instance = None 
    
    def __new__(cls):
        if  not cls._instance :
            cls._instance =  super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)

