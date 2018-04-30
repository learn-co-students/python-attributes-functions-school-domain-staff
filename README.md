
# Python Attributes Functions Lab

## Introduction
We've been learning a lot about different parts of object oriented programming. We learned about classes and what purpose they serve. We've seen instance objects, instance variables, and instance methods and how these things all work with each other. In this lab, we will talk about what a **domain model** is and how it ties into object oriented programming.

## Objectives

* Understand the concept of a domain model
* Create a domain model
* Define instance methods that operate on nested data structures

## What Is a Domain Model?

A domain model is the representation of a real-world concept or structure translated in to software. This is a key function of object orientation. So far, our Python classes have been used as blueprints or templates for  instance objects of that class. As an example, a Driver class would create driver intsance objects, and the class would define a basic structure for what that driver instance object should look like and what capabilities it should have. But a class is only one part of a domain model just as, typically, a driver is only one part of a larger structure.

A domain model is meant to mirror that larger, real-world structure. It is more than just one class, it is an entire environment that often depends on other parts or classes to function properly. So, in keeping with a Driver class, we could use the example of a taxi and limousine service as our domain model. There are many more parts to a service like this than drivers alone. We could imagine dispatchers, mechanics, accountants, passengers, etc., all being part of the structure of this domain model. In a simplified example, we could have instance and class methods handle things like `dispatch_driver`, `calculate_revenue_from_rides`, `service_taxi`, or any other function of a taxi and limousine service.

As we become more fluent in object oriented programming and our programs become more complex, we will see that the other parts of a domain model like passengers, dispatchers, etc., will be classes of their own which interact with each other. 

In this lab, we will be using a school as our domain model.

### Part 1:
Create a class, School, in the school.py file in your local directory that can be initialized with a name. The School class would be referred to as a "model" in the domain model context.


```python
from school import School
```


```python
school = School.new("Middletown High School")
```

### Part 2:
A school should have a roster, which should be an empty dictionary upon initialization but will be built-out to contain keys of grade levels. The value of each key will be a list of student names (i.e. `{"9": ["John Smith", "Jane Donahue"]}`).


```python
school.roster() #{}
```

### Part 3:
You should be able to add a student to the school by calling the add_student method and giving it an argument of the student's name and their grade.


```python
school.add_student("Peter Piper", 12)
school.roster() #{"12": ["Peter Piper"]}
```

## Summary

