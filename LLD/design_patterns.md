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
- we have a database connection class allows us to connect database 
- class where we write how to connect for database 
- we have written we can have max 5 database connection to database 
- when we have 3rd party resource or resource shared among multiple class 
- suppos when we accessing this database object from multiple class then for each object it will allows resource limit = 5
- not a good idea to have something like this one 
- suppos we are calling an api limit of 500. where we are storing count 
- wont each object have count of 500 
- its class which maintain resources 
- Key Concept of Singleton :
    - One Instance: The core principle is to restrict the instantiation of a class to a single object.  Means there a restrict on creation of object 
    - Global Access: It provides a well-known, global access point to that single instance, so other parts of the program can easily get a reference to it.
    - Lazy Initialization: Often, the instance is created only when it's first needed, a technique known as lazy initialization. This saves memory and resources if the instance is never used.



- Logging: A logging system for an application should have a single instance. If multiple parts of the program create their own logger objects, they might write to different files or conflict when writing to the same file. A singleton logger ensures all log messages are funneled through one central object, maintaining consistency.
- Configuration Management: Applications often rely on a single set of configuration settings (like API keys, database URLs, or feature flags) that need to be accessed by many different components. Using a singleton for the configuration manager ensures all parts of the app read from the exact same configuration, preventing inconsistencies.
- Database Connection Pooling: Creating a new database connection is a resource-intensive and time-consuming task. To avoid this overhead, applications use a connection pool to manage a set of reusable connections. The connection pool itself should be a singleton, so all parts of the application share the same pool of connections, leading to better performance and resource utilization.
- Thread Pools: In multi-threaded applications, a thread pool manages a collection of worker threads to execute tasks. Having a single thread pool (a singleton) ensures that thread creation and management are centralized, preventing the creation of too many threads and improving overall system efficiency.




- Singleton Design Pattern No of obect = 1 , There is a restriction on creation of object 
- How can we restrict someone of creation of object of which part of class responsible for creation of object : Constructor 
- There should be restriction on accessing constructor , How we can restrict , Make it private 
- with Private we cant make even a single object we need one object 
- if we make a constructor private how we can make even a single  object ? :
- we can access a private constructor using a public method 
- so we can call a public method in side the class and method will responsible for calling private constructor 
- Public method needs to be static so we can call it without an object 
- Particular Public method can be called multiple times 
- Thus failing Singleton design Pattern 
- We have to put somekind of check if object created or not ?
- Introduced a static veriable That will Hold The object and make the public method conditonal 
- we will create an object only if there is no object available for class 


class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


# Example usage
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True



When you call Singleton():

- Python calls type.__call__(Singleton, *args, **kwargs).
- That internally calls Singleton.__new__(cls, *args, **kwargs) to create (allocate) the object.
- Then, if an object was returned, Python calls Singleton.__init__(self, *args, **kwargs) to initialize it.
- _instance is a class attribute (shared by the class and all its instances).
- It will hold the one and only instance once created. Starting value is None (sentinel meaning “not created yet”).
- __new__ is a classmethod-like constructor: first parameter is the class (cls), not the instance.
- if not cls._instance: checks whether an instance already exists.
- On the first call, _instance is None → condition is True.
- You call super().__new__(cls) (which is object.__new__) to allocate a brand-new, empty instance of cls (no __init__ yet).
- You store that instance on the class as _instance.
- On later calls, _instance is already an object → the if fails and you return the same object.
- Returning an existing object means callers always receive the same reference.
- we only need to override the new method to get a same object everytime 
- Design pattern is language agnostic not related to any Language 
- Can be applied to any language 


Singleton With MultiThreaded :
- Suppos class for singleton ran by two threads named T1 and T2
- What if same method responsible for creating object accessed by two different thread at a same time 
- Due to multi Threading we may end up creating 2 different object 
- what if 5 Threads running it may end up creating 5 Threads 
- insted of creating a object in custom method create a object within constructor 
- constructor method will be called only once in class life time 
- Not a good approch 
- you will always get one object 
- Cons :
    - Start Time Will Increase Significantly 
    - Creating an object even if we dont need it 

Solution 2 : Syncronize :
    - Make Method syncronize 
    - What if One thread coming at a time in webserver 
    - Once even object created Will Thread Go Inside Once Object created 
    - For each User One Thread 
    - If object already created then no issue for even multi threading 
    - Multi Threading Only only there till no object 
    - syncronize make code slow 
    - why we need to make code slow everytime 
    - A synchronized block is a section of code that ensures only one thread can execute it at a time. It's like putting a lock on a shared resource, such as a cutting board in our kitchen analogy. When a thread wants to access that resource, it must first acquire the lock. If another thread already has the lock, the new thread has to wait its turn. Once the first thread is done, it releases the lock, and another waiting thread can proceed. This mechanism prevents race conditions, which happen when multiple threads try to access and change the same data simultaneously, leading to unpredictable results.

    Cons of Using synchronized Blocks
    - Performance Overhead: synchronized blocks introduce a performance cost. Acquiring and releasing locks takes time, and if many threads are competing for the same lock, they'll spend a lot of time waiting. This can reduce the benefits of multithreading.

    - Potential for Deadlock: If not used carefully, synchronized blocks can lead to a deadlock. A deadlock occurs when two or more threads are stuck, each waiting for a lock that the other holds. For example, Thread A has lock 1 and needs lock 2, while Thread B has lock 2 and needs lock 1. Neither can proceed.

    - Reduced Concurrency: Because only one thread can be inside a synchronized block at a time, it reduces the degree of parallelism in your program. If the block contains a lot of work, it can become a bottleneck that limits overall performance.

    - Granularity Issues: Using synchronized on a large block of code might be too restrictive. It might lock resources that aren't even being used by other threads, unnecessarily limiting concurrency. Fine-grained locking is often better but can be more complex to implement.


Solution 3: Double Checking :
    - Double-checked locking (DCL) is a design pattern used to optimize the creation of a Singleton object, particularly in a multithreaded environment.  The core idea is to reduce the overhead of acquiring and releasing a lock by checking the instance twice.
    
    Here's the logic:
    - First Check (without a lock): The code first checks if the instance is null. If it isn't, the instance is already created, so the method returns it immediately, avoiding any synchronization overhead.
    - Lock Acquisition: If the instance is null, the thread enters a synchronized block to ensure exclusive access to the critical section.
    Second Check (with a lock): Inside the synchronized block, the code checks if the instance is null again. This is the "double-check" part. This is crucial because multiple threads might have passed the first check and are now waiting to enter the synchronized block. The second check prevents multiple instances from being created.
    - Instance Creation: If the instance is still null, the new singleton instance is created and assigned to the variable.



Builder Design Pattern : 
    - The Builder Design Pattern is a creational pattern that separates the construction of a complex object from its representation, allowing the same construction process to create different representations. It's particularly useful when dealing with objects that require numerous parameters, many of which are optional.
    - we have a class with lots of attribute 
    - Example Student : A class with Lots of attributes 
    - create an object of student them set each and every attribute 
    - or we can use constructor to pass each and everydetails 
    - Work : Create lots of student object with lots of attribute  and we want to validate few more things before creating an object 
    - we want multiple validation ,, On age , Mobile Number 
    - No object should be creatted before validation are done  
    - Complex Object Construction: When an object has many parts that need to be initialized in a specific order or with different configurations.
    - Telescoping Constructors: When a constructor has a long list of parameters, some of which are optional, leading to multiple overloaded constructors. The Builder pattern replaces this with a fluent, readable API.
    - Immutability: To create immutable objects, where an object's state cannot be changed after it's been created. The builder gathers all the necessary parameters, then a build() method creates the final immutable object.

    - with setter : There is no possible way 
    - constructor : Technically NO 
    - Lots of constructor required duplication of code 
    
    Task we are solving :
    - Create Object with Lots of argument 
    - Validate all the objects before creating Objects 
    - Helps in creating Immutable objects 

    - Immutable : Object that once created cant have any change  In any of its value Its called Immutable  Object
    - cant call setter without object 
    - if we validate inside the object Then prone to error ( What if we pass argument in wrong order)
    - TOO Many Constructor Combination 
    - Better Solutuon :
        - Take Help from another class 
        - Create a helper class which contains all Attributes of student and no Logic 
        - Validation will be done side setter method  of helper class
        - create constructor inside a class which takes helper object as input and create a object 
        - Is there any need of helper class except Validation : Nope 
        - Helper class Known as Builder 
        - We can create an inner class  or we can build it as inner class

The Builder pattern consists of four main components:

- Product: This is the complex object being built. It's the final result of the construction process. The Product class doesn't need to know anything about the building process itself. In our sandwich analogy, the Product is the completed sandwich 🥪, with all its ingredients.

- Builder: This is an abstract interface that defines the steps for building the Product. It includes methods for each part of the object's construction. For our sandwich, the Builder interface would define methods like addBread(), addCheese(), addMeat(), etc.

- Concrete Builder: These are the specific classes that implement the Builder interface. Each Concrete Builder provides a different implementation of the building steps, which results in a different type of Product. For example, a VeggieSandwichBuilder and a ChickenSandwichBuilder would both implement the Builder interface, but they would add different ingredients.

- Director: This class orchestrates the building process. It uses the Builder interface to construct a Product step-by-step. The Director doesn't know the specific Concrete Builder being used; it just knows the steps to follow. This is what allows the same Director to create different types of products. In our analogy, the Director is the person taking your order and telling the sandwich maker (the Concrete Builder) what to add in which order.



Prototype Design Pattern :

    - Every Design Pattern help us to solve a Issue 
    - The Prototype is a creational design pattern that lets you create new objects by copying an existing object (called the prototype), rather than constructing them from scratch (e.g., using the new keyword).
    - This is particularly useful when the construction of a new object is computationally expensive or complex (e.g., involves database calls, complex calculations, or is built from a complex configuration).
    - There are Two ways To do IT ?
        - Copy Constructor 
        - USE Getters and setters to copy value from object 
    - Does Client Need To know all the internal implementation and attributes to copy using getter and setter 
    - what if we copy and attributes are hidden . They are Private and No Getter and setter 
    - Now The remaining way is copy constructor 
    - Just Use The Copy Constructor 
    - what if we pass the object of child class for copy constructor 
    - Ideal Situation : Client class should not worrry about creating copy of object work should be outsourced 
    - Shallow Copy: Copies the object's value types (e.g., int, String) but copies the references of its object types. Both the original and the clone point to the same mutable sub-objects. Changing a sub-object in the clone changes it in the original, and vice-versa. This can be a major source of bugs.
    - Deep Copy: Copies the object and all objects it refers to, recursively. The original and the clone are completely independent.
    - Use deep copy if your object has references to mutable objects (e.g., arrays, collections, other complex objects) and you need the clones to be truly independent.
    - Use shallow copy only if the object's references are to immutable objects (like String) or if you intentionally want to share state.
    When to Use the Prototype Pattern
    - To Avoid Expensive Initialization: When creating a new object is resource-intensive (e.g., requires database queries, reading files, complex calculations) and you need similar objects frequently.
    - To Avoid a Complex Constructor Hierarchy: When your code would otherwise require a lot of creational subclasses just to configure an object, but the differences are minor. Cloning a pre-configured prototype is often simpler.
    - To Hide the Concrete Classes from the Client: The client code can work with objects through their prototype interface (Document), without being coupled to the concrete classes (ReportDocument, LetterDocument).
    - we dont need to create a object repetedly Just clone existing available object 



    The Process Of 
    - The Prototype Interface: Declares the clone() method.
    - The Concrete Prototype: The actual object that implements the clone() method to return a copy of itself.
    - The Client: Asks the prototype to clone itself to create a new object.
    - This will make things easier with lesser code 


Registry Pattern :
-  The Registry Pattern is a structural design pattern that provides a centralized place to store and retrieve objects, services, or configurations. It acts as a global point of access for these resources without requiring them to be passed throughout the application.
- Global Access Points: When you need global access to objects or services
- Service Location: For implementing a service locator pattern
- Configuration Management: To centralize application configuration
- Plugin Systems: To manage pluggable components
- Dependency Management: As a simple dependency injection container




Factory Design Pattern :

- The Simple Factory Pattern (a variation of the Factory Pattern) provides a way to create objects without exposing the instantiation logic. 
- The Factory design pattern is a creational pattern that provides a way to create objects without specifying the exact class of object that will be created
- Imagine you're building a video game where you have different types of enemies: Goblin, Ogre, and Dragon. A simple way to create these enemies would be to use the new keyword directly in your code:
- This works fine for a simple case, but what if your game gets more complex? What if you need to create enemies based on the current game level or player's location? Your code would quickly become a mess of if-else or switch statements scattered throughout your application, like this:
- This approach has a major drawback: if you decide to add a new enemy type, say a Troll, you'd have to find and modify every single if-else statement. This makes your code hard to maintain and prone to errors. This is what's known as tight coupling—your code is directly tied to the specific classes it creates.



from abc import ABC, abstractmethod

# 1. Product Interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# 2. Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 3. Simple Factory
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# 4. Usage
if __name__ == "__main__":
    # Create animals using the factory
    dog = AnimalFactory.create_animal("dog")
    cat = AnimalFactory.create_animal("cat")
    
    print(dog.speak())  # Output: Woof!
    print(cat.speak())  # Output: Meow!



- There is a class called User Service. Has a database Can Opt for more than one database Type 
- Can OPT FOR Postgresql or MONGODB 
- To Insert In database we need a query 
- Once Query Is created 
- We can Update Create User Delete User.
- Once query created execute it againest the database




- if database is concrete class then user server depending Upon it which violate dependancy inversion principal 
- if we have to change database leter it will be complex 
- create database as interface 
- Interface has 4 Mthod 
    - CreateQuery 
    - Connect
    - Execute 
    - getVersion
- all of them should return the same query - which is an interface apart from what kind of database return same query
- Create query return query type object depending upon the database type
- For NOSQL Database : Mongodb query 
- SQL Database - sql query 
- Orignal purpose of create query : Create Query Object whenever needed 
- This Method is called Factory Method 
- which return object repetedly 


- We dont want concrete class for database we want abstraction 
- based on dtabase instance type :
- query object will be created 
- we will be adding more and more if else : FOR CREATE : Clear Violation of OCP 
- Devide database into 2 class 
- One will take care of 
- First class will take care of attributes and methods for database functionality 
- Another part : Contains all factory Methods 
- We are taking part of database should we worry about factory 
- we can just add a method createfactory method which returns factory object 

db factory = create a database factory 



Factory Method design Pattern :
- The Factory Method design pattern is a creational pattern that provides an interface for creating objects in a superclass, but lets subclasses decide which class to instantiate.

- Product: This is an interface or an abstract class that defines the common behavior for all the objects you're creating. In your database example, this would be the Query interface. Both a SQLQuery and a MongoDBQuery would implement this.
- Concrete Product: These are the actual implementations of the Product interface. For you, this would be the SQLQuery class and the MongoDBQuery class. They provide the specific logic for their respective query types.
- Creator: This is the abstract superclass (or interface) that contains the factory method. The factory method is a method that returns an object of the Product type. For example, your Database interface would have an abstract method: createQuery(). This class doesn't know which concrete product to create, it just knows that it needs to create a product.
- Concrete Creator: These are the subclasses that implement the Creator and are responsible for overriding the factory method to return a specific Concrete Product.  For example, the PostgreSQLDatabase class would override createQuery() to return a new SQLQuery(), while the MongoDBDatabase class would override it to return a new MongoDBQuery().

- Dependency Inversion Principle (DIP): It helps your UserService depend on abstractions (the Database and Query interfaces) rather than concrete implementations (the PostgreSQLDatabase or MongoDBDatabase classes). This means your UserService code doesn't need to change if you switch databases.
- Open/Closed Principle (OCP): You can add new database types (e.g., a RedisDatabase) to your system without modifying existing classes like UserService or the Database interface. You simply create a new Concrete Creator class and a new Concrete Product if needed. This makes your codebase more scalable and maintainable.
- Code Duplication: Without this pattern, you might have if-else or switch statements scattered throughout your application to determine which concrete object to instantiate. The factory method centralizes this creation logic, making it easier to manage and change.




Abstract Factory design pattern :

- The Abstract Factory design pattern is a creational pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. 

- While the Factory Method pattern focuses on creating a single type of object, the Abstract Factory pattern deals with creating a whole family of objects that work together. 🏭

- we'll create a family of objects for two types of databases: SQL and NoSQL. This family might include not just a Query, but also a Connection and a Transaction object, all of which must be compatible with a specific database type.

- Abstract Factory: This is the main interface for creating all the related objects. It defines methods for each type of product in the family. In our example, this would be the DatabaseFactory interface with methods like create_query(), create_connection(), and create_transaction(). It doesn't implement any of these methods; it just declares them.

- Concrete Factory: These are the actual implementations of the Abstract Factory. Each concrete factory is responsible for creating a family of products that are compatible with each other. For us, this would be the PostgreSQLFactory and the MongoDBFactory.

    - PostgreSQLFactory will create a SQLQuery, a PostgreSQLConnection, and a SQLTransaction.
    - MongoDBFactory will create a MongoDBQuery, a MongoDBConnection, and a NoSQLTransaction.

- Abstract Product: These are the interfaces for the individual objects in the product family. In our example, this would be the Query, Connection, and Transaction interfaces, each defining a common set of operations.

- Concrete Product: These are the specific implementations of the Abstract Products. Each concrete factory will produce a specific set of these.

    SQL Family: SQLQuery, PostgreSQLConnection, SQLTransaction.
    NoSQL Family: MongoDBQuery, MongoDBConnection, NoSQLTransaction.



- Ensures Compatibility: It guarantees that the products created by a factory are compatible with each other. You can't accidentally mix a SQLQuery with a MongoDBConnection.

- Encapsulates Object Creation: It separates the client code from the concrete product types. Your UserService only interacts with the DatabaseFactory interface, so it doesn't need to know if it's getting a PostgreSQLFactory or a MongoDBFactory. This makes the code very flexible.

- Centralizes Family Creation: All objects in a related family are created in one place, making it easier to manage and modify.







Adapter Design Patterrn :

- In real Life adapter is nothing but plug and play 
- Its nothing but connector 
- Kind of plugs we have and kind of plugs another country have totally different 
- we cant use our plug in us or europe we cant charge our mobile 
- we need an device named adapter 
- adapter allows us to use our plug in us . It acts has intermediate layer between two connecting points 
- transforms one form to another 
- Think of the Adapter pattern as an electrical travel adapter. Your laptop's power cord has a specific plug (the Adaptee), but the wall outlet in another country has a different shape (the Target interface). You can't plug your laptop directly into the wall. You need a travel adapter (the Adapter) that has a plug compatible with the wall outlet and a socket compatible with your laptop's plug. The adapter handles the conversion, so you don't have to change your laptop's power cord.
- Complexity of code will increase 
- Increase size width and price of adapter 
- apple choose universal adapter and kept rest of things added via adapters 
- client ----------> adapters -----------------> AWS/GCP/AZURE
- Client interact with adapter adapter interact with one of cloud provided default aws 
- what if you only want to use azure
- change in adapter 
- to only allows to interact with client 

- adapter makes code maintainable and independent of 3rd party depemndancy 
- we can change 3rd party dependancy 
- when we communicating with 3rd party depemdancy 
    - change our code base 
    -  we should never connect directly insted use interface in between 
    - interace acts as adapter 
    - PhonePe and different apis 
    - phone pe created an interface between actual client and bank apis 
    - changes only need to performed in interface between client and server 
    - entire code bas talking to inteerface 
    - we call adapte not actual client 
    - client -----> interface ---> multiple bank apis 

- Client: The object that uses the adapter. It expects a specific interface (the Target interface) to perform its actions.
- Target Interface: The interface that the client expects to use. This is the desired standard for communication.
- Adaptee: The existing class with the incompatible interface that you want to reuse. It's the object that needs to be adapted.
- Adapter: The class that implements the Target interface and contains an instance of the Adaptee. It's the bridge that translates the client's calls into calls that the adaptee understands.


Facade Design Pattern :

- The Facade design pattern is a structural pattern that provides a simplified, unified interface to a complex system of classes, objects, or subsystems.  
- Suppos amazon class and list out all of its method as well as Attributes , Inventory Managment CRM , Supply Chain , Notification Via SMS OR EMAIL  
- Facade: A single class that provides a simplified interface to a complex subsystem. It knows which subsystem classes are responsible for a client's request and delegates the requests to the appropriate objects.
- Subsystem Classes: The complex set of classes that perform the actual work. The facade interacts with these classes, but the client does not interact with them directly.
- Imagine you are in a restaurant. You don't go to the kitchen to order from the chef, get your ingredients from the pantry, and then ask the bartender for a drink. Instead, you interact with a single entity: the waiter. The waiter is the facade. You, the client, make a simple request to the waiter ("I'd like the steak and a glass of wine"). The waiter then handles the complex process of communicating with the kitchen (Chef class), the pantry (Pantry class), and the bar (Bartender class), and brings you what you requested.
- The facade pattern works similarly in software. The client makes a simple request to the facade class. The facade then coordinates the complex interactions between the various subsystem classes to fulfill the request. This approach provides several benefits:




Benefits
- Simplifies the Interface: The most significant benefit is that it reduces the number of objects a client has to deal with. The client only needs to know about the facade, not the multiple classes within the subsystem.
- Decouples the Client from the Subsystem: The facade creates a layer of abstraction that separates the client from the complex details of the subsystem. This means you can make changes to the subsystem without affecting the client's code.
- Improves Readability and Maintainability: By hiding complexity, the facade makes the client's code cleaner and easier to understand. This also makes the system easier to maintain, as changes are localized.
- Reduces Dependencies: The facade can prevent the client from becoming tightly coupled to the subsystem's implementation.



decorator design Pattern :

- The Decorator design pattern is a structural pattern that allows behavior to be added to individual objects dynamically, without affecting the behavior of other objects from the same class. It is a flexible alternative to subclassing for extending functionality, adhering to the Open/Closed Principle (classes should be open for extension but closed for modification).

- Intent :
    - Attach additional responsibilities to an object dynamically.
    - Provide a flexible alternative to subclassing for extending functionality.


The Decorator pattern consists of four main components:

- Component Interface: This is the interface or abstract class that defines the core functionality that both the original object and the decorators will implement. This ensures that the decorator is interchangeable with the original object from the client's perspective.
- Concrete Component: This is the original object that you want to add new responsibilities to. It implements the Component interface.
- Decorator Base Class: This abstract class or interface also implements the Component interface. It holds a reference to a Component object and serves as the base for all concrete decorators.
- Concrete Decorators: These classes extend the Decorator base class. They add specific new functionality by wrapping the original Concrete Component or another Decorator. A concrete decorator's method often calls the method of the object it wraps and then adds its own logic before or after.


Key Benefits
- Dynamic Extension: Add/remove behaviors at runtime.
- Avoids Class Explosion: Prevents a proliferation of subclasses for every combination of behaviors.
- Single Responsibility Principle: Divide functionality into smaller, reusable classes.
- Flexibility: Mix and match decorators arbitrarily.

Drawbacks
- Complexity: Can lead to many small classes, increasing complexity.
- Order Dependency: The order of decorators may affect behavior (e.g., <b><i> vs. <i><b>).
- Initialization Overhead: Decorators add layers, which might introduce performance issues if overused.

Use Cases
- Adding features to UI components (e.g., scrolling, borders).
- Enhancing I/O streams (e.g., BufferedReader, GZIPInputStream in Java).
- Adding logging, encryption, or compression transparently.



stretrgy design pattern :

- How many people used Google Maps 
- There are some spacial kind of bhaviour we might need to implement :  Strategy Design Pattern 
- The Strategy design pattern is a behavioral design pattern that allows you to define a family of algorithms, put each one into a separate class, and make their objects interchangeable. 💡 This pattern lets the algorithm vary independently from clients that use it.
- Imagine you have a class, let's say a NavigationApp, that needs to calculate a route. It can do so in different ways: by car, public transport, walking, or cycling. Without the Strategy pattern, you might have a single calculateRoute() method with a bunch of if/else statements to check the mode of transport. This makes the class rigid and hard to extend. If you want to add a new mode, like an e-scooter, you have to modify the existing NavigationApp class, which violates the Open/Closed Principle (open for extension, closed for modification).
- Insted of implement all bhaviour in same function different method for diff bhaviours 



The Strategy pattern solves this by:
- Creating a Strategy Interface: This interface (e.g., RouteStrategy) defines a common method that all concrete strategies must implement (e.g., calculateRoute()).
- Creating Concrete Strategy Classes: Each algorithm becomes a separate class that implements the strategy interface. So, you'd have a CarRouteStrategy, PublicTransportStrategy, WalkingStrategy, and so on.
- The Context Class: This is the class that uses the strategies (e.g., NavigationApp). Instead of having a bunch of if/else statements, it holds a reference to a RouteStrategy object. It can set this strategy at runtime.


- Think of it like choosing a payment method at an online store. The store's checkout system is the context. The different payment methods (credit card, PayPal, Google Pay) are the concrete strategies.
- Strategy Interface: A PaymentStrategy interface with a pay() method.
- Concrete Strategies: CreditCardPayment, PayPalPayment, and GooglePayPayment classes, all implementing the pay() method differently.
- Context: The ShoppingCart class. It has a checkout() method that takes a PaymentStrategy object and calls its pay() method.
- The ShoppingCart doesn't need to know how each payment method works; it just needs to know that it can call pay(). This makes it super easy to add new payment options in the future without changing the core ShoppingCart class. You just create a new payment strategy class.



