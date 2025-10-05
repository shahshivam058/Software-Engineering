LLD : Low Level Design 

when user send request what happend ?

- Request will first gose to Load Balancer 
- Load Balancer will send a request to any of server 
- Profile stored in database 
- Before accessing database , Request Gose to cache 
- Someone Profile Being Access Multiple Time data being cached 
- we may search in cache if not available in cache then request sends to database 
- Here in above we discuss about multiple components High Level Components 
- as a human we are intelligent 
- Humans are smart then computer 
- sometime both machine have same level of load so where to divert a request 
- Human choose the shorted one . Computer are dumb one 
- Computer cant decied where to send a request 
- There are certain algo in load balancer know how to route each request 
- cache stores the data being access frequtly 
- temperory storing the data for us 


above design we say HLD : High Level Design 
- Overview of flow 
- how different components being interact with each other 
- What Makes machine Load Balance ?
    - Nothing but a software 
    - Mostly all components are same hardware 
    - Software is the one which makes actual diff 
    - all components are nothing but hardware software give correct functionality 
    - LLD Talks about details of software running on that machine 


Daily Life
- Scrume 
- Meeting 
- Coding
- Debugging
- Documentation 

we do all this in daily meeting 

Software Engineer Spend 12 Percentage of time writing code 
LLD Helps to utilise 88 percent efficiently 

- if we follow all lld concepts while writing the code 
- makes code more readable and understandable 
- Makes Requirment Gathering easy 
- application is extensible - Makes Easy to add new features - add a feature should not be rewrite whole code we should only do few changes enough
- application is maintainable - Easy to Keep System Working in current state - New Changes Should not affect our current system 
- If something change we need to write whole code then our code is not extensible . Like LOG4J
- our entire codebase doesnot know about this log4j it only know about veriable 
- to make or enable darkmode - We have to change hexadecimal color everywhere 
- we can make a veriable and veriable will be reuseed everywhere 
- Extensibility is about how easy it is to add new features (e.g., adding a new payment method). It's about building for future growth.
- Maintainability is about how easy it is to understand, fix, and modify existing code (e.g., fixing a bug). It's about managing the current health of the code.
- LLD : Kind of indian term actual they say Object Orianted Design 
- Most company definetly ask one round of LLD 
- 0 - 2 : SDE 1
- 2 - 5 : SDE 2
- 5 - 10 : SDE 3
- 10+ : Staff Engineer 

Machine Coding : Design + Coding 
Normal LLD : Only Design 

- If code is Structured Then Making changes is much easier 
- Things like estimation time will be easy 
- Machine Coding Round Build Prototype code in 2 hours 


LLD Problem Devided in 5 different Parts 
- Design Pen  (Entity Design Problem)
- Design Chess (Design Game)
- Design Book My Show OR Parking Managment System ( Managment System)
- Design Splitwise (Real Life Application)
- Design cache ( Engineering Problem)


Object Orianted Programing 

Programming Paradigms

- Procedure orianted : c
- Object Orianted Programing : JAVA, C++ , Python, JS
- Functional Programing : Haskell , Scala





- Procedure Programing : Procedure means Function or set of instruction , Nothing But Old Name for Function 
- All Function may internally call each other 
- we write code in buch of function 
- Execution start from a single function named main 
- Problem With Procedure : 
    - is that data and the functions that operate on that data are separated. This leads to a fundamental problem: a lack of data security and uncontrolled data modification.
    -  a shared office spreadsheet that everyone in the company can view and edit. There's no way to stop someone in the marketing department from accidentally changing a critical formula entered by the finance team. This leads to chaos, errors, and makes it very hard to track down who made a change.
    - Action being Performed on entity 
    - Once Application Grows Hard to manage application 
    - Difiicult to make sense in large application 
    - Readinbality and understandability is bad 
    - Spaggeti code 
    
OOP : Object Orianted Programing 
- Entity are core of application 
- entity are consist of 
    - Property  or attributes 
    - Bhaviours or function

- 1 Principal of OOP - Abstraction 
- 3 Pillers of OOP - Encapsulation , Polymorphisam , Inheritence
- Principals = Something you want to achive 
- Piller = way we can achieve principals 


Abstraction :
- Making something abstrect 
- Hideing Implimentation Detail 
- Abstrect is nothing but idea 
- Representation In terms of  Idea
- Do we care how platform is being created 
- We just know input and output we dont know what is logic being implemented internally 
- we dont know how it created or what is the main logic 
- abstrection comes at lot of places 
- beliving on idea of something and then doing your action 
- Abstrection helps in understanding system really well 
- Other dont need to know 
- Example : we use sort() function to sort array but we don't know how it sorts the array


Encapsulation :
- In capsule we have medicine 
- Capsule save medicine from actual enviouments 
- It holds medicine togather 
- Protect medicine from outside env 
- Encapsulation Object orianted programing holds the attribute and methods togather of entity 
- It protects the attributes and bhaviour from Illigitment access from other class
- Prevents Direct access of a class 
- Class Package attribute and methods Togather 


Two Terms :
- Class : Represents Blue Print of something  : Class Is nothing but cake tin
- Object : Object is real world representation of class : Real Class : Object Oocupy memory Something we can use to interact with class 
- No metter how many object we will create it might have same property but different values 
- For each object we may pass different value 
- Class is not physical it doesnt oocupy any memory 
- Function Only Logic they dont hold data

- if all 100 cakes being built by cake tin size of all will be same 
- No worry how many cake we create all will be of same size 
- we can create a 10 cake size will be same but what if we add different creams taste it will be different



Access Modifires :
- 4 Types of access modifires 
- Public - Can be access from class and outside the class 
- Private - Can be only access within the class cant access from outside the class
- Protected  - Can be access from from class in a subclass and s (and sometimes same package/namespace).
- Default

Python's Philosophy: 
- Python follows the principle "We are all consenting adults here." It trusts developers to use good judgment rather than enforcing strict access rules.
- Convention Over Enforcement: The single underscore is a signal to other developers that an attribute/method is intended for internal use or for subclassing, but Python doesn't prevent access.
- Practicality: Python values flexibility and practicality. There are legitimate cases where accessing protected members from outside might be necessary (e.g., testing, debugging, or framework development).


In Python, the double underscore (__) prefix for private members is not strict enforcement - it's a mechanism called name mangling that makes access more difficult but not impossible.

When you use __ before an attribute/method name, Python changes the name to _ClassName__attribute to make it harder to accidentally override in subclasses and to signal that it's intended for internal use.



Oven responsible for creating cake :
construction responsible for creating objects 
we cant create an object without constructor 
There is always a default constructor 


Types of contructor : 
1) Default : if we dont add any constructor in our class Language By default adds conttucor in class. Not visible to us but in class . Create an object and insilize the value of all veriables inside the class with intial values . if we dont add any languaghe compiler will add by default and add a defult value for each veriable . each veriable will have an default value . default contructor is just function with nothing inside the body . also known as no args constructor means we are not passing any values while creating object . default construction : not creatd by us , no args constrctor : when we provide intial value for some veriable .
we can provide value of constructor veriable from outside the class 
just use object to pass values 
everytime we are assing the value using object we are assign the value to veriable inside 
2) Perameterized  or Custom Constructors or argumented : A parameterized constructor is a constructor that accepts one or more arguments. It allows you to initialize the member variables of an object with specific values at the time of its creation. You must explicitly define this constructor, and once you do, the compiler will no longer provide the default constructor automatically.  This is useful for ensuring an object is created in a valid state with meaningful data.

3) Copy :
A copy constructor is a special type of constructor that creates a new object as a copy of an existing object. It takes a single argument, which is a reference to an object of the same class. Like the default constructor, if you don't define a copy constructor, the compiler will provide one automatically.  This is called a member-wise copy or shallow copy.

- The copy constructor is invoked in several situations:
- When an object is initialized with an existing object.
- When an object is passed by value to a function.
- When a function returns an object by value.

For simple classes, the default shallow copy often works fine. However, for classes with dynamic memory allocation (e.g., using pointers), a shallow copy can lead to problems where two objects point to the same memory location. This is where a deep copy is required, which involves explicitly defining your own copy constructor to allocate new memory and copy the contents, ensuring the two objects are independent.


s = New Student ()

Making New constructor 

S = Holds Refrance Veriable 
We have 2 types of memory 
Heap Memory 
Stack Memory 

Refrance veriable stored in stack 
Its nothing but where object stored in memory 
S.id = 10

It will go to heap anc in object for id change value = 10 

both values are allocated in runtime 

Untill code doesnt compile memory isnt allocation in stack 

t = s 

new refrance created a named t which points to s 
This is called shallow copy 
we only copy the refrance veriable we dont create actual object 

if we want to make a deep copy 

In heap create a new object and ref stored in stack 
for a deep copy 
t = new student(s)

read data from orignal object replicate to another object 

deeop copy we create both the ref copy of ref and copy of object 


copy constrructor isnt built in python 


when you have multiple types of constructor in class = Constructor overloading 


Destructor : 

- Object is Real Instance of type class 
- Creation of Object when the data when memory is getting allocated 
- Class Doesnt occupy any memory 
- Java has destructor 
- we have made an use of object and no more revelt action pending on it  it should be destructed otherwise  it will keep occupying memory .
- an object with no refrance  
- Object is in heap and refrance is in stack when refrance points to null
- we cant reach to object 
- Java as something called garbage collector which frees memory. Runs Automatically in Java 
- There is a function in java which can schedule a gc 
- GC Process is expensive 
- each programing language has gc algo somekind of 
- What if object is not null
- Some language has distructor 
- responsible for moving object out of memory 


Inhrtitance :
- Inherit the property of parents 
- Father has 300 and we have 3 child every child get 100 rs
- Father has some dna sample . same sample will be given to all 3 childs 
- in real life we inherit the attributes as property and bhaviour from parents 
- Height - Property , 
- Spending Money = Bhaviour 
- form a hierarchy in relationship level 
- mael is animal 
- animals can breath 
- can mamel breath 

- Wants to build scaler platform 
- we have different kind of people in scaler 
- instructor , student , ta all are inherited from user 
- each user have same bhaviour like login , Logout 
- each users are of spasefic type 
- it became more spasefic 
- this will have all of attributes and methods of user class but also have more 
- more attribute and more methods for each users 
- Parent class -> child class
- Super class - > Sub class 
- all kind of users 
- as we go downwards in child classs they have more attributes and more methods and more details 
- going downwards we are going more spasefic 
- upwards we are going genralization 
- if required we can have more attribute and bhaviour in child class or we can have it empty as well 
- wants to maake code more readable and extendable then 
- parents class is nothing but genralization - Will have morr comman method and attributes among all class 
- child class spasefication  - spasefic methof or attribute belongs to class
- More generic 
- Inheritence provide code reusibality child class can access all values in parent class


How objects of child classing are getting created :
- as soon as we call constructor of instructor it will call user constructor 
- user constructor insilize all of his attributes , this value copied to child class 
- child class we havent created any constructor = no 
- we will have a default one which will automaticall call parent class constructor 
- user object not being used by anybody 
- each class calls constructor of parent class 
- first thing in each constructor in subclass will call constructor of super class 
- super needs to be always first line in constryctor 
- in general multiple inheritence should be avoided 
- 4 Types of Inheritence 
    - General Inheritence
    - Multiple Inherotence a , b -> c(a , b) - Cause  A dimond problem 
    - Multi level Inheritence a - > b -> c
    - Hierarchicle 




Polymorphisam , Interface , Abstrect Class :
- Combination of 2 diff words :
    - Poly = Many
    - Morph : Forms 
- ability of having multiple forms 
- example : man as a instructor or he can be student , Son , Friend , Uncle 
- woman can be also multiple things 
- user can be a , Instructor , Student , TA 
- user has multiple forms 
- user as a student and instructor and ta will be having different bhaviours 
- we can pass all users to function itrate over all users and print user.
- user is a list can be consist of student , TA and Instructor 
- User is a genralized form 
- when we create a user a refrance will be stored in a stack and actual object stored in HEAP.
- u = new user()
- allows us to access spasefic attribute within a class 
- 2 ways to use tv : Remote , TV Buttons 
- New version of tv becomes S2 , it will have all things s1 has + Some New Features 
- S2 Also have new remote 
- Remote will works with s2 tv 
- With R1 We can also access s2 , It can use but new features cant be used 
- R1 -> S1 , R2 -> S2 ,R1 -> S2 ,
- UpCasting from child to parent object , Older remote new tv 
- Downcasting Object of parent access class of chile 
- Since Upcasting we are not writing anyextra thing = Implicit type 
- Where we have to write child  class : Down Cating 
- we can force compiler to do down castinh +
- Upcasting will not leads to error 
- Downcasting may lead to error we try to access feature that is not available in parent class 


Method Overloading and method overriding :
- Same method name . Different Type , Different no of args
- Function take multiple kind of inputs and returns result 
- we cam go through code in println whcih may take different types of arguments 
- but return redukt sk
- same function different type of argument , Diff no of arguments  Method overloading 
- Method overload makes thing easier for us 
- Method Signatue = Method name + Parameters
- Two different method same name of argument same type perameter - Then same method 
- Multiple Methods inside a class having a same but different signature 
- if we want to perform same kind of opretion but no of argument might be different or types of argument might be different then method overloading might be used, Rather then we need to create a different function for different argument and diff names 
- we dont want our users to worry about input 
- also known as compile time polymorphisam 
- which method to call decided at compile time 


Method OverRiding :
- we have a vehical class has a method : start engine 
- 2 Types of car : ICE , Electric 
- Both types of cars have method start engine 
- Completly diff way of startig a car
- Insted of startengine we can write startICEEngine or StartElectricEngine 
- N No of class we dont remember everythig 
- 2 Ways we can start : Button , Key 
- It kind of abstraction 
- we override the method = Same Signature + Diff iMPLEMENTATION 
- we can create a different method with a same name each class have their spasefic one - each class linked through inheritence 
- it will invoke the method for a class for which we have created an object 
- each class have their own method but name will be same in all class but impmementation is different 
- 2 class linked through inheritence but both have same method - but different implementation which method to run defined at 
- based on the object method will be called 
- its also called run time polymorphisam
- Method overriding is when a child class provides its own version of a method that is already in its parent class. This lets the child class change how a specific task is done without changing the method's name or its input and output. It's a fundamental concept in object-oriented programming (OOP).
- Imagine you have a family. The parent (the parent class) has a rule: "Clean your room" (the method).
- The parent's default way to "clean the room" might be to just put clothes in the closet.
- Now, one of the children (the child class) is very neat and has their own, better way of cleaning. They decide to override the parent's rule. Their version of "Clean your room" means they will not only put clothes in the closet but also make the bed and vacuum the floor.
- The parent's rule still exists, but when you tell the child to "clean your room," they use their own, more specific method instead of the parent's default one.





Interface : 
- Class Consist of method attributes and constructor 
- class is blue print of entity 
- constructor used for entity creation 
- attributes and methods are part of bhaviour 
- interface doesnt represent real entity . excet not real entity it defines bhaviour or blue print of bhaviour 
- interface categorize in terms of bhaviour 
- any living being eat talk or breath is human 
- using above you can categorize human from other living being 
- we can write an interface animal eact walk run : animal
- interface only has method defination not implementation 
- now every animal should have this bhaviour 
Core Concepts
- Imagine an interface is like a contract or a blueprint. It doesn't actually build anything itself. Instead, it just lays out a set of rules for a class to follow.


- The Contract: An interface says, "If you want to be a 'something,' you must have these specific abilities." For example, an IDrivable interface (the "I" often stands for interface) might have rules like:

    startEngine()
    accelerate()
    brake()

- The Class: Now, let's say you have a Car class and a Bus class. Both of them can be "drivable." To prove this, they can implement the IDrivable interface. This means they are both promising to follow the rules of the contract by providing their own unique way to startEngine(), accelerate(), and brake().

- The Code: You could then write code that works with anything that is IDrivable, without caring if it's a Car or a Bus. This is incredibly powerful because it makes your code flexible.

- Abstraction: Interfaces provide a high level of abstraction. They hide the internal implementation details of an object, exposing only the necessary methods for interaction. This allows for a clean separation of concerns.

- Multiple Inheritance: In languages that don't support multiple inheritance of classes (like Java and C#), interfaces are a way to achieve a similar result. A class can implement multiple interfaces, thereby inheriting multiple "contracts" of behavior.


Why Use Interfaces?
- Flexibility: It lets you swap out one object for another without changing the rest of your code. For instance, you could upgrade from an old Car class to a new ElectricCar class, as long as the new class also implements IDrivable.

- Organization: They help organize your code by defining clear roles and responsibilities. It's easy to see what a class is supposed to do by looking at the interfaces it implements.

- Teamwork: In a team project, one programmer can design the interface (the contract), while another programmer works on the actual implementation (the class). They can work independently, as long as they agree on the rules of the interface.

- Loose Coupling : Interfaces help to decouple your code, meaning one part of your program doesn't need to know the specific details of another. Your code can interact with an object through its interface, which is a common set of methods, rather than with its specific, concrete class. This makes your system more adaptable to change.

- Testability : Interfaces make unit testing much easier. When a class depends on another object, you can replace the real object with a mock or fake object that also implements the same interface. This mock object can be programmed to return specific data or track how it was used, allowing you to test your code in isolation without relying on external services like a database or a network call.


- Polymorphism : Interfaces are the foundation for polymorphism, which means "many forms." A variable can be declared as an interface type, and at runtime, it can hold an object of any class that implements that interface. This allows you to write more generic and reusable code.

- Simulating Multiple Inheritance: Many programming languages like Java and C# don't allow a class to inherit from multiple parent classes (multiple inheritance). This is to avoid a complex problem known as the "diamond problem." However, a class can implement multiple interfaces, which lets it "inherit" multiple sets of behaviors. This provides a clean way to add capabilities to a class without the complexities of multiple inheritance.



The Role of the Interface: The UPI Standard
The National Payments Corporation of India (NPCI) created the Unified Payments Interface (UPI) as the core interface. Think of UPI as a formal, nationwide contract. This contract, or set of technical specifications, dictates exactly how a payment application (like PhonePe, Google Pay, or Paytm) and a bank's system (like Yes Bank, ICICI Bank, or SBI) should communicate to process a payment.

This interface specifies things like:

How a user's Virtual Payment Address (VPA) is created (user@ybl).

The format of a payment request.

The data required for a transaction (amount, unique transaction ID).

The expected response from the bank (success, failure, pending).

The security protocols for data encryption and authentication.

This standardized interface is the foundation of the entire UPI ecosystem.

Yes Bank: The Implementation
Yes Bank is a Payment Service Provider (PSP) bank. In the UPI ecosystem, this means they have implemented the UPI interface. They built a robust, secure, and scalable system on their end that can handle millions of API calls every day, all following the rules of the UPI contract. When a request comes in to user@ybl (the "ybl" stands for Yes Bank), their system knows exactly what to do:

Authenticate the user.

Verify the UPI PIN.

Debit the sender's bank account.

Credit the recipient's bank account.

Send a real-time confirmation back to the requesting app.

PhonePe: The User of the Interface
PhonePe is a Third-Party Application Provider (TPAP). They built their consumer-facing application, with its user-friendly UI and features, on top of this UPI interface. PhonePe's developers do not have to know how Yes Bank's internal systems work, how their databases are structured, or what specific programming language they used. All PhonePe cares about is that Yes Bank provides an API that follows the UPI contract.

When a PhonePe user sends money, the PhonePe app simply makes an API call to Yes Bank's UPI service, formatted exactly as specified by the UPI interface. The app says, "Hey Yes Bank, can you please process a payment for this user with this amount?" and Yes Bank's system responds with a simple "yes" or "no" (along with a transaction ID).

The "Switching" Moment: A Perfect Example of Interface Value
The genius of this interface-based design was powerfully demonstrated in March 2020. Due to a financial crisis at Yes Bank, the Reserve Bank of India (RBI) placed a moratorium on the bank, which temporarily halted many of its services.

Because PhonePe was, at the time, primarily partnered with only Yes Bank to provide UPI services (all their users had the @ybl VPA), millions of transactions for PhonePe users immediately failed. The user@ybl virtual addresses couldn't connect to a working bank system.

Here is where the interface truly saved the day:

No Code Rewrite: PhonePe's core application code for handling payments did not have to be rewritten. The IPaymentProvider contract (the UPI interface) remained the same.

Plug-and-Play Migration: The NPCI and PhonePe worked quickly to activate new partnerships with other PSP banks like ICICI Bank and Axis Bank. This was possible because these new banks also implemented the exact same UPI interface.

Seamless Transition: PhonePe could then easily transition its users to the new bank handles (e.g., @ibl for ICICI Bank or @axl for Axis Bank) by simply changing the _paymentProvider object in their system from the YesBankProvider implementation to the ICICIBankProvider implementation.

Abstrect Class : 

- An abstract class is a special kind of class that can't be used to create objects directly. Instead, it acts as a blueprint or a semi-finished template for other classes. It can have both regular methods with code inside them and special abstract methods that have no code at all. Any class that inherits from an abstract class must provide its own code for all the abstract methods.

- The model kit for a "Vehicle" might come with a frame and four wheels already attached (these are the regular methods with code).

- But the kit also has instructions that say "add an engine here" and "attach the exterior body here" (these are the abstract methods). The instructions tell you what to do, but not how to do it. You have to buy your own engine and design your own body.

- You can't just take the "Vehicle" kit and drive it. You have to first choose what kind of vehicle you want to build, like a "Car" or a "Truck," and then add the unique parts for that vehicle. A "Car" class would add a car engine and car body, while a "Truck" class would add a truck engine and truck bed.

- In low-level design, an abstract class is used to provide a common base for a group of related classes. It allows you to share code and enforce a specific structure, which leads to more organized and maintainable systems.

- Shared Logic and Enforced Structure: You'd create an abstract class called Employee. All employees share some common characteristics, so you can put that shared code right into the Employee class. For example, every employee has a name and an ID, so you can have regular methods to set and get those values.
However, the way each employee gets paid is different. A full-time employee gets a salary, while a contractor gets paid by the hour. To handle this, you declare an abstract method called calculatePay(). You don't write any code in this method in the Employee class; you just declare it.

- Concrete Implementations: Now, you create specific classes that inherit from Employee. Because they inherit from an abstract class, they are required to provide a concrete implementation for calculatePay().

The FullTimeEmployee class would implement calculatePay() to return a fixed monthly salary.

The Contractor class would implement calculatePay() to multiply their hourly rate by the number of hours worked.

