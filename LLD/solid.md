# 👉 What is Low-Level Design, their formats, and expectations from the interviewers?

- What it is?
	* Uber/Notification/Twitter
	* Its about thinking the classes that will go in a service.

- Formats
	* 45 mins round
		* ~30 mins.
		* Given a problem, you have to write the basic classes, properties, method signatures.
		* Pseudo code of the core of the system.
		* Full running/compiling is not required.
	* Machine Round
		* Duration: 1.5 hrs - 2.5 hrs.
		* Full running/compiling is required.


* Functional reuirements
* Able to explain your approach.

* Goals
	* Handling changes in code: 
        * extensibility
		* Follow SOLID principles.
		* Maintanability
		* Reusability
	* Readbility
	* Testability	
		* Unit testable.
	
* Non Goals
	* Complexity: Algorithmic complexity, space complexitites: looping through array or keeping a map.
	* Multi-threading: 
	* Scability in terms of # of users. : Problem OF HLD 
	* Using external databases/queues. : Problem OF HLD 
	* Knowledge of specific frameworks. java - lombok, spring


what is principal ? SOLID , YAGNI , DRY

-  A principle is a fundamental rule or guideline that guides software design toward a desired quality, such as maintainability, extensibility, and reusability. They are high-level concepts, not specific code implementations.
-  Low-Level Design (LLD) is where you get into the nitty-gritty of class and object design. The primary goal of LLD is to create a design that adheres to these principles, ensuring the final code is robust and easy to work with.
-   When you analyze a software design, you evaluate how well it adheres to these principles. For example, you might ask: "Does this class have a single responsibility?" or "Is this module open for extension?"

- YAGNI (You Ain't Gonna Need It): A principle from Extreme Programming (XP) stating that you should not add functionality until it is necessary. This prevents over-engineering and keeps the design simple.
- DRY (Don't Repeat Yourself): A principle aimed at reducing repetition of code and logic. Every piece of knowledge should have a single, unambiguous, authoritative representation within a system.


 
 


What is Pattern ?  Singleton , factory 
- A pattern is a formalized, reusable solution to a common design problem. It's a template, not a direct implementation, and it provides a proven approach to structuring code to solve a specific issue.


SOLID Principles :

SOLID : Short name for 5 different design principals 
S : SRP : Single Responsibility Principle
O : OCP : OPEN CLOSED PRINCIPAL 
L : LSP : Liskov Substitution Principle
I : ISP : Interface Segregation Principle
D : DIP : Dependency Inversion Principle

- Many People think as DIP as dependancey inversion principal but its not 

SOLID = Set of principals / Set of rules or guideline to design best software system 
Design Pattern : Some Logic by following SOLID principles 
LLD : USE DESIGN PATTERNS AND DESIGN SYSTEM FOLLOWING SOLID 

Software system should be 

- extensible
- maintainable 
- reusable 
- easy to test 
- moduler 
- understandable 

- Good code no one needs to ask you what is implemented they already knew about that one 


Design a bird :
Assume you have to build software  where you want to store information about bird and what actions bird performs 
Keep In mind diversity of bird 


- we have created a clss represents the bird class and class will be consist of attributes and methods 

- class can be accessed by any object 
- each object represents the 3 birds
- is it good we write method consit of multiple if else 
- low reusibality 
- class viOlates s in SOLID 




- proble 
	- Understandiability 
	- difficult to test 
	- difficult to work with 





Single Responsibality Principals :
- A class should have only one reason to change,  or just single responsibaality
- This is the most accurate and powerful definition. It doesn't mean a class should only have one method or do only one thing. Instead, it means that all the elements within a class should be related to a single, cohesive responsibility.
- Think of it from a maintenance perspective. When a requirement changes, you should ideally only have to modify one class. If a class has multiple "reasons to change," a change in one area could unintentionally break another, leading to a ripple effect of bugs and making your code fragile.
- A class might have multiple methods, but if they all serve a single, cohesive purpose, they adhere to SRP. The key

- Makesound() : Method just to make sound by bird 
- Fly() : how away bird flu 
- Bird class should hold all attributes and bhavipir of birds that exists 
- we should not over engineer 
- 

class Report {
  generateReport() {
    // Logic to fetch data from the database
    // Logic to format the report
    // Logic to save the report to a file
    // Logic to email the report to a manager
  }
}


How To Identify SRP Violation ?

- Methods with if else  might not always True Sometime Business Logic Needs Multiple If else 

example :

if type == crow :
	makesoundcrow()
elif type == pigon :
	makesoundpigon()
elif type = sparrow :
	makesoundsparrow()

Logic Under if else will be different 


- Each Block Completly Sepret and independent code 
- Make Sound Do two diff job : Identidy Bird and make sound 


we have method doAction() :
- we can write a code within do action to perform action based on action type 
- Insted of making action in function under we can create a sepret method to do so 
- Sepret Block of code for each kind of action 
- Write Node its violating logic as all things are implemented at once 
- we can do like take the action as input based on action perfom function call 
- after replacing implementation with function call no violation of srp 

Monster Methods :

- Methods with Lots of Logic inside them Mainly Holding Logic Doesnot Match with method name 
- There is a method name save to database : created a query to insert in database 
- Method should only do to save data 
- This method create a query , Create a connection  and cursor , insert , close
- There should be sepret method for each  , Method it self not have whole code that performs violation 


def SaveToDatabase(data) :
	insert into (" --------------------------------------")
	q = connection.query()
	cursor = connection.cursor()
	cursor.execute(insert)
	cursor.close()


Package , Common , Utils :
- Ends Up becoming a garbage case for all code that engineer doesnot know where to put 
- There can be converter that convert time to normal time 
- Insted a implement global package regarding Time conversion 
- we have to write robust code saves us from 


Constant : 
- Dont recommanded to have generic constant class across the project 
- Put it in the class 
- either put constant in clas it self 
- spasefic package across add constant data 
- spasefic class for each module 



Open Closed Principals : 

- Open for Extension: This means you can add new functionality to the system without changing existing code. You can extend the behavior of a module by adding new code.
- Closed for Modification: This means you should not have to change the code of an existing, well-tested module to add new features. Once a module's behavior is defined and it works, you shouldn't need to alter its source code.
- The key to applying the OCP is through abstraction. Instead of depending on concrete implementations, your code should depend on abstractions (interfaces or abstract classes). This allows you to introduce new behaviors by creating new classes that implement these abstractions, without touching the existing code that uses them.



- Bird class Hold Attribute And perform Functionality 
- Let The bird class only hold attribute and generic details and not  spasefic implementation 
- we can create a bird class and abstrect class each child class inherit parents class and implement method and have spasefic method  it will implement all generic method and own implementation and also have spasefic method 
- to add a new bird we just need to add a new implementation class 
- this bird class example of SRP 
- Bird class has method then child  clalss need to implement it you will be forced to implement that method 
- if we have bird which doesnt fly then we can just pass none in child class for method or we can just raise an exception 
- we can do bird v3 : 
	- have generic methods inside that and keep methods abstrect 
	- in method we can return boolean 
	- anyway to enforce code for fly interface : 
	- we can have implement fly as part of interface now fly is not important 
	- there can be class explosion problem 

- this one is not right also 

The Problem Violating OCP :

Let's imagine you're building a reporting system that generates reports in different formats. Initially, you only need to create PDF reports.


class ReportGenerator:
    def generate_report(self, report_format, data):
        if report_format == "PDF":
            # Logic to generate PDF report
            print("Generating PDF report...")
        else:
            raise ValueError("Unsupported report format")

# Usage
generator = ReportGenerator()
generator.generate_report("PDF", {"title": "Monthly Sales"})

Now, your boss asks for an Excel report format. To add this feature, you must modify the generate_report method by adding another elif block.



class ReportGenerator:
    def generate_report(self, report_format, data):
        if report_format == "PDF":
            # Logic for PDF
            print("Generating PDF report...")
        elif report_format == "EXCEL":
            # New logic for Excel
            print("Generating Excel report...")
        else:
            raise ValueError("Unsupported report format")

# Usage
generator = ReportGenerator()
generator.generate_report("EXCEL", {"title": "Monthly Sales"})

This violates the OCP. Every time a new report format is needed (e.g., CSV, JSON), you have to change the ReportGenerator class, which makes it brittle and increases the risk of introducing bugs.



The solution is to use abstraction and polymorphism. We can create a base Report class that defines a common generate method, and then have specific report types inherit from it.

from abc import ABC, abstractmethod

# Abstraction: A base class for all report types
class Report(ABC):
    @abstractmethod
    def generate(self, data):
        pass


# Concrete implementation for PDF reports
class PDFReport(Report):
    def generate(self, data):
        print("Generating PDF report...")

# Concrete implementation for Excel reports
class ExcelReport(Report):
    def generate(self, data):
        print("Generating Excel report...")

class ReportGenerator:
    # This method is now closed for modification
    def generate_all(self, reports, data):
        for report in reports:
            report.generate(data)

This design is highly scalable. The ReportGenerator is now closed to modification. To add a new feature, you simply extend the system by creating a new class that inherits from Report. This approach is clean, reduces risk, and is the standard for building robust systems in modern software engineering.


Liskov Sabsitution principal : 

- the LSP states that if you have a base class (or parent type) and a subclass (or subtype), you should be able to use an object of the subclass wherever an object of the base class is expected, without the program's correctness being affected.

- Object of Any child class Should be sabsitutable in parent type without requiring any code change 

- We should not need to accomodate or give any spacial preferance to child object for accomodating to parent type 

- Code is more predictable: You can trust that a subclass will behave like its parent, honoring the parent's contract.

- New features can be added with confidence: You can introduce new subtypes without worrying about breaking existing code that uses the base type.

- Polymorphism works as intended: The principle is a formal definition of what proper subtype polymorphism should be.

- LSP Says Dont Over write things that dont go togather 

Rule 1: The "Is-A" Test is Not Enough
This is the most fundamental concept to grasp. Just because something "is a" in the real world doesn't mean it should be an inheritance relationship in your code. The classic "Square is a Rectangle" example is the perfect illustration.

The rule: Don't just model the real world. Model the behavior you need. If a subclass cannot be used exactly like its parent without causing problems, then the inheritance is wrong.

Example:

Bad: Square inherits from Rectangle. Why? Because Rectangle has setters for width and height that work independently. A Square's setters must change both, breaking the expected behavior of anyone using a Rectangle object.

Good: Don't use inheritance. Instead, have both Rectangle and Square implement a common Shape interface that defines methods like get_area(), but no methods that would cause a behavioral clash (like independent setters).



Rule 2: Don't Break the Contract
Every class has an unwritten "contract" with the code that uses it. This contract is made up of its methods, their expected inputs (preconditions), and their guaranteed outputs (postconditions). A subclass must not violate this contract.

The rule: A subclass can't require more from you (stronger preconditions) or give you less (weaker postconditions).

In plain terms:

Preconditions (What you need to provide): If a method in the base class requires a number greater than 0, the overridden method in the subclass can't suddenly require a number greater than 100. It must accept the same or a wider range of inputs.

Postconditions (What the method guarantees to do): If a base class method guarantees to return a positive number, the subclass method must also return a positive number. It can't suddenly start returning negative numbers.




Rule 3: Don't Throw Unexpected Exceptions
This is a specific type of contract violation. If a base class method doesn't throw a certain type of exception, a subclass method should not suddenly start throwing it.

The rule: A subclass method can't throw new, unexpected exceptions. It can throw the same exceptions as the base class, or a subclass of those exceptions. It's also okay if it throws fewer exceptions.

Example:

Bad: You have a base File class with a read() method that never throws an IOError. A subclass NetworkFile overrides read() and throws an IOError if the network connection drops. This violates LSP because client code expecting a File might not be prepared to handle an IOError.

Good: The base File class should declare that its read() method might throw an IOError. This way, any code that uses a File is aware of the potential exception, and any subclass is free to throw it.

Rule 4: No "Empty" or NotImplemented Methods
If you find yourself writing a subclass that overrides a base class method just to leave it empty or to throw a NotImplementedException, that's a huge red flag that you're violating LSP.

The rule: If a subclass can't implement a method from its base class in a meaningful way, the inheritance relationship is probably wrong.

Example:

Bad: You have a Bird class with a fly() method, and a Penguin class that inherits from it. Since penguins can't fly, the Penguin.fly() method is empty or throws an exception.

Good: Refactor your design. A Bird interface might be too broad. Instead, you could have a FlyingBird interface that only birds that can fly implement, and a SwimmingBird interface for penguins. This avoids forcing a subclass to inherit a behavior it doesn't have.

Rule 5: Keep Properties and State Consistent
The state of the subclass should always be consistent with the state of the base class. In other words, adding new methods or properties to a subclass should not alter the behavior of the inherited methods in an unexpected way.

The rule: Any new properties or methods you add to a subclass must not change the meaning or behavior of the base class's properties and methods.

Example:

Bad: The "Square and Rectangle" example perfectly fits this rule too. When you call set_width() on a Square, it also changes the height, which is an unexpected side effect for a method that's supposed to be an independent setter. This change in state breaks the Rectangle contract.





Interface Segregation Principle (ISP) : 

- it's better to have many small, specific interfaces than one large, general-purpose interface. When you have a big interface with many methods, any class that implements it is forced to provide an implementation for all those methods, even if it only needs to use a few of them. This can lead to "fat" interfaces and a bloated class that has to include methods it doesn't need, potentially with empty or "throw new exception" implementations.


Why Is This a Problem?
- Bloated Classes: A class implementing a large interface becomes a jack-of-all-trades, master of none. It's forced to support functionalities it doesn't actually need, making the class larger and more complex than necessary. This violates the Single Responsibility Principle (SRP), which states that a class should have only one reason to change.

- Unnecessary Dependencies: When a client (another class or module) depends on a large interface, it is indirectly dependent on all the methods within that interface. This means that if a method in that interface changes (even one the client doesn't use), the client might need to be recompiled or redeployed, creating unnecessary coupling and making the system more fragile.

- "Leaky" Abstractions: A large, generic interface can be a "leaky" abstraction. It exposes details and methods that are irrelevant to a specific client, making the code harder to understand and use.


The Solution: Segregate! ✂️

The solution is to break down large interfaces into smaller, more specific ones. Each of these smaller interfaces should serve a single, cohesive purpose.

Imagine you're designing an interface for a multi-function printer.

Violation of ISP (Fat Interface):


interface IMultiFunctionPrinter {
    void Print(string document);
    void Scan(string document);
    void Fax(string document);
}


class SimplePrinter : IMultiFunctionPrinter {
    public void Print(string document) {
        // Implementation for printing
    }

    public void Scan(string document) {
        // Not a good solution:
        throw new NotSupportedException("This printer cannot scan.");
    }

    public void Fax(string document) {
        // Not a good solution:
        throw new NotSupportedException("This printer cannot fax.");
    }
}


Good Solution :

interface IPrinter {
    void Print(string document);
}

interface IScanner {
    void Scan(string document);
}

interface IFax {
    void Fax(string document);
}


// The SimplePrinter only needs to print
class SimplePrinter : IPrinter {
    public void Print(string document) {
        // Implementation for printing
    }
}

// A more advanced machine can implement multiple interfaces
class AllInOnePrinter : IPrinter, IScanner, IFax {
    public void Print(string document) {
        // Implementation
    }

    public void Scan(string document) {
        // Implementation
    }

    public void Fax(string document) {
        // Implementation
    }
}



DIP : 

- The DIP states that high-level modules should not depend on low-level modules; both should depend on abstractions. Additionally, abstractions should not depend on details; details should depend on abstractions.

- a high-level module is a class that contains complex business logic, like a Store class that processes orders. A low-level module is a class that performs a basic, detailed operation, such as a PaymentProcessor or a DatabaseConnector.

- Without DIP, a high-level module would directly interact with a concrete low-level module. For example, a Store class might create an instance of a PayPalPaymentProcessor class. This creates a strong, "brittle" dependency. If you want to switch from PayPal to Stripe, you have to modify the Store class, which violates the Open/Closed Principle (OCP).

The "Inversion" Part :
- The term "inversion" refers to the inversion of the traditional dependency flow. Instead of the high-level module dictating which low-level module it uses, both now rely on an abstraction (like an interface or abstract class).

- Traditional Flow: High-level module (e.g., Store) depends on low-level module (e.g., PayPalPaymentProcessor).

- Inverted Flow: Both the high-level module (Store) and the low-level module (PayPalPaymentProcessor) depend on an abstraction (e.g., IPaymentProcessor).

- This "inverts" the control. The high-level module doesn't control the low-level module's implementation; it only specifies the required behavior through the abstraction.



How to Apply DIP
To apply DIP, you need to introduce an abstraction (like an interface) that both the high-level and low-level modules can depend on.

Let's use an example of a Notifier that sends messages.

❌ Bad Design (No DIP)
Java

// Low-level module
class EmailSender {
    public void sendEmail(String message) {
        System.out.println("Sending email: " + message);
    }
}

// High-level module
class Notifier {
    private EmailSender emailSender;

    public Notifier() {
        this.emailSender = new EmailSender(); // Direct dependency on a concrete class
    }

    public void notifyUser(String message) {
        emailSender.sendEmail(message);
    }
}
Here, the Notifier class is tightly coupled to EmailSender. If you want to add an SMS or push notification option, you have to modify the Notifier class, which is a big no-no in LLD.

✅ Good Design (Applying DIP)
Create an Abstraction: Define an interface.

Java

// Abstraction (Interface)
interface IMessageSender {
    void sendMessage(String message);
}

Make Low-Level Modules Depend on the Abstraction: Implement the interface in your concrete classes.

Java

// Low-level module depends on abstraction
class EmailSender implements IMessageSender {
    @Override
    public void sendMessage(String message) {
        System.out.println("Sending email: " + message);
    }
}

// Another low-level module
class SmsSender implements IMessageSender {
    @Override
    public void sendMessage(String message) {
        System.out.println("Sending SMS: " + message);
    }
}
Both EmailSender and SmsSender are now "details" that depend on the IMessageSender abstraction.

Make High-Level Modules Depend on the Abstraction: The Notifier now takes the IMessageSender interface as a dependency, usually through constructor injection.

Java

// High-level module depends on abstraction
class Notifier {
    private IMessageSender messageSender;

    // Constructor Injection
    public Notifier(IMessageSender messageSender) {
        this.messageSender = messageSender;
    }

    public void notifyUser(String message) {
        messageSender.sendMessage(message);
    }
}


This design is much more flexible. The Notifier doesn't care if it's sending an email or an SMS; it just knows it has a messageSender that can send a message. You can create different Notifier instances with different types of message senders:


Notifier emailNotifier = new Notifier(new EmailSender());
emailNotifier.notifyUser("Your order is complete!");

Notifier smsNotifier = new Notifier(new SmsSender());
smsNotifier.notifyUser("Your order is complete!");

This is a perfect example of how DIP promotes loose coupling and allows for easy swapping of implementations, which is crucial for scalable, maintainable software.


Design Patterns ? What are Design Patterns ?


Design patterns are reusable solutions to common problems in software design. Think of them as blueprints or templates you can adapt to solve recurring design challenges. They aren't finished code snippets you can copy and paste. Instead, they're abstract concepts that provide a framework for building robust, maintainable, and scalable software.

Imagine you're building a house. Instead of figuring out how to construct a door, a window, or a wall from scratch every single time, you use pre-established architectural patterns. This saves you time, ensures the structures are sound, and makes it easier for others to understand and work on the house.

Design patterns serve the same purpose in software development. They:

- Provide a common language: When developers discuss "the Singleton pattern" or "the Factory method," everyone understands the underlying structure and intent, leading to more efficient communication.

- Improve code quality: By using well-tested solutions, you can avoid common pitfalls and create more flexible and maintainable code.

- Increase development speed: You don't have to reinvent the wheel for every problem. You can apply a known solution, saving significant time and effort.

- Make code more readable and easier to debug: Code that follows a known pattern is often easier for other developers to understand and troubleshoot.


- There are total 23 design patterns we dont need them all for low level design 
- we just need to some of them


3 Types of Design Pattern 

- Creational design patterns
    - Singleton
    - Factory
    - Builder
    - Prototype
- Structural design patterns
    - Adapter
    - Bridge
    - Composite
    - Decorator
    - Facade
    - Proxy
- Behavioral design patterns
    - Chain of Responsibility
    - Command
    - Interpreter
    - Iterator
    - Mediator
    - Memento
    - Observer
    - State
    - Strategy
    - Template Method
    - Visitor



- Creational Design Pattern :
    These patterns deal with object creation mechanisms. They aim to create objects in a way that is suitable for the situation while increasing the flexibility and reusability of the code.

    How Objects are getting created.
    How Many Objects are getting created.

-  Behavioral Patterns 🏃
These patterns are concerned with algorithms and the assignment of responsibilities between objects. They describe how objects communicate with each other.



- Structural Patterns 🏗️
These patterns are concerned with how classes and objects are composed to form larger structures. They simplify the structure by identifying relationships between entities.

