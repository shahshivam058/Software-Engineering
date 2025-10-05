- 3 Major Types of LLD Interviews 
    - Theoratical Interview  : 
       - Old Tech Company , Mid Level StartUps , MID Tier company , 
       - Walmart , Oracle , JPMC 
       - Test OOPS and Design Pattern Knowledge  
       - 45 - 60 Mins
    - Design : 
        - Problem solving round
        - WANTS TO DESIGN SOMETHING
        - Case Study 
        - They just want structure 
        - MNC Like Microsoft , Atlassian , 45 to 60 mins 
    - Machine Coding 
        - Problem Solving  with implementation 
        - Case Study will be given without details 
        - working code needed write code from strach 
        - asked by top startup and company 

Main Diff between design and machine coding 

Design :
- Single Line Problem statement was given 
- Expected Gather requirments and ask question and clarrify requirments 
- Use case diagram 
- Class Diagram 
- Come Up with all class you have all level of abstraction , Design Pattern 
- Schema Design - Not always required 
- Create a design of platform 
- Discuss what you did 

Machine Coding :
- Detailed Problem statement or document is given on information and requirments 10 mins 
- Read and clarrify  5 mins 
- Use case diagram if needed 10 mins 
- Class Diagram - If needed  10 mins
- Schema design 5 mins
- write working code  1 hour
- discuss with interview 20 mins
- ask interviewer for what kind of application : Terminal based (Command Line) or api based 



How we design :
- Gather requirments always first step :
- Clarrify requirments and 
- Class Diagram / API Design 



Genrally 3 types of system : 

- Entity : Class and relation ship no code needed 
- Interactive : No storage , TIC TAC TOE , No need to store anything 
- web system : Actually need storage , Book my show 
- Controller - service - dao 
- Models - Entiti

Problem Statement : Design a pen 

- Gather requirments 
    - Suggest Idea with rationals 
    - 5 TO 8 : Core features of system : 3 TO 4 also works 
    - 


- Anything that helps to write a pen 
- Different Types of pen : Jel Pen , Fountain pen  
- Closer Type : Cap based Button based or click based , role based 
- Pens have inside that : Refill , or ink , or spring 
- pen might or might not have refill 
- Ink can be of different colors 
- Pen might have grid or might not 
- foundation pen takes  ink directly 
- refill change type 
- non refillable pen 
- details of pen 
- how pen writes 



- Clarrify the requirments 

Understand the Problem Domain
Before jumping into the design, let’s clarify what a Pen is and what it does:

A Pen is an object used for writing or drawing.
It has certain physical attributes (e.g., ink color, type) and behaviors (e.g., write, refill).
It interacts with other entities like Paper, InkRefill, and possibly User.


What types of pens are we designing? (e.g., ballpoint, fountain, gel)
Should the pen support refilling ink or replacing parts?
Does the pen have any constraints? (e.g., limited ink capacity, durability)
Are there any advanced features? (e.g., erasable ink, pressure sensitivity)



- A pen seems simple in real life, but if you analyze carefully, it has:
- Attributes (state) → brand, color, ink type, nib size, ink level, etc.
- Behaviors (methods) → write, refill, change nib, remove/put cap.
- Different types → BallPen, FountainPen, MarkerPen, etc.


- So, the main challenge is:
- Capture common properties of all pens.
- Model differences in behavior for different types of pens.
- Keep the design extensible (so if tomorrow we add a MarkerPen, we don’t have to rewrite everything).




(a) Abstraction

We created an abstract class Pen which defines what every pen should be able to do:
write(text) (but how it writes depends on the type).
refill(new_ink)
change_nib(new_nib)
This lets us hide implementation details (e.g., a fountain pen needs a cap, a ball pen doesn’t).



(b) Encapsulation

We created separate classes for the components:
Ink → holds color, type (gel, oil-based, etc.), and current ink level.
Nib → holds size (0.5mm, 0.7mm) and material (steel, gold, plastic).
Each class controls its own state using methods like consume(), refill(), etc.
This makes the code cleaner and reduces duplication.




(c) Inheritance

We defined Pen as a base (abstract) class, then created specialized pens:
BallPen
FountainPen
Both inherit common properties (brand, ink, nib) but can override behavior.
For example:
BallPen.write() just writes text.
FountainPen.write() first checks if the cap is removed.


3. Why Break into Ink and Nib Classes?

You might ask: why not just keep ink_color and nib_size as simple attributes in Pen?
The reason is Single Responsibility Principle (SRP).
Ink manages ink operations: consumption, refill, checking empty.
Nib manages nib properties: size, material.
Pen manages higher-level behavior (writing, refilling, etc.).
This modularity makes the system easier to extend and maintain.