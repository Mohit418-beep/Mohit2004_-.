Employee Management System (Python OOP Project)
This project is a simple command-line application that demonstrates fundamental concepts of Object-Oriented Programming in Python, including classes, inheritance, encapsulation, and polymorphism.

Key OOP Concepts Illustrated
Classes and Objects: Defines four main classes: Person, Employee, Manager, and Developer.

Inheritance:

Employee inherits from Person (though the Person class is not explicitly set as the parent in the code provided, it shares common attributes like name and age, suggesting it was intended to be the base). Note: A correction/enhancement to the code would be to explicitly make class Employee(Person):.

Manager inherits from Employee (class Manager(Employee):).

Developer inherits from Employee (class Developer(Employee):).

Encapsulation: Uses private-like attributes (conventionally indicated by a single leading underscore, e.g., _employee_id, _salary, _department, _language) with public setter and getter methods (e.g., set_employee_id, get_employee_id).

Polymorphism: The display() method is overridden in the subclasses (Employee, Manager, Developer) to provide class-specific information, demonstrating method overriding.

Destructors (__del__): The __del__ method is implemented in each class to demonstrate how resources can be cleaned up when an object is destroyed (though its execution timing in Python can be unpredictable).

The application runs in a continuous loop, allowing the user to perform the following actions via a menu:

Create a Person (Option 1): Instantiates a Person object and sets its name and age.

Create an Employee (Option 2): Instantiates an Employee object and sets basic details (name, age, ID, salary).

Create a Manager (Option 3): Instantiates a Manager object (inheriting from Employee) and sets all employee details plus a department. It also explicitly checks and prints that Manager is a subclass of Employee.

Create a Developer (Option 4): Instantiates a Developer object (inheriting from Employee) and sets all employee details plus a language. It also explicitly checks and prints that Developer is a subclass of Employee.

Show Details (Option 5): Presents a submenu to display the stored details for the last-created object of the chosen type (Person, Employee, Manager, or Developer) using the polymorphic display() method.

Exit (Option 6): Exits the program and explicitly calls del on all created objects, triggering the __del__ destructor method for demonstration.
