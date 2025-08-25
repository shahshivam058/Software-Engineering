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
- Design Pen   (  Entity Design Problem)
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
    -  Bhaviours or function

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


