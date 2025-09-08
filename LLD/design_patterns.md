Singleton Design Pattern :  

- Static Keyword : Associated with class veriable or function 
- Attributes and methods : In General Present in object and accessed via the object 
- Static Oocured at class level and  and doesnot need object to be used 
- we call static attributes or method from class . Via class name not object 
- Static members are declared with the static keyword. They are not part of any specific object's state but are tied directly to the class itself. Think of it like a universal property for all members of a family, not just one person.
- While static members are useful, they can introduce problems if overused.
- Global State: Static variables are like global variables. Modifying them from one part of the code affects all other parts. This can make your code harder to test, debug, and maintain.
- Encapsulation: Excessive use of static members can break the principles of object-oriented programming (OOP), as it encourages procedural, rather than object-based, thinking.
- Main called by jvm 
- if its not static it needs object to call 
- so main at class level is static 
- we cant call main if non static 

Singleton Design Pattern :

- Singleton design patterns allow you to create a class such that There can be only one object of given class 
- Suppos A a single class 
    - example :
        A - Singleton class 
        # we created 2 diff object 
        a1 = new A()
        a2 = new A()

- we have to write code in a such way even when user asks for a new object they cant get it they always get  one single object 

- why do we need singleton design pattern ?
- when class have any shared resource behind it. it should be considered singleton design pattern 
- class for database connection 
- 

 