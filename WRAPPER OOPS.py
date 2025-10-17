#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Person:
    def _init_(self):
        self.name=None
        self.age=None
    def set_person_name(self,name):
        self.name=name
    def set_person_age(self,age):
        self.age=age

    def display(self):
        print("Person details:")
        print(f"Name :{self.name}")
        print(f"age :{self.age}")

    def _del_(self):
        print(f"person {self.name} is destroyed")
class Employee:
    def _init_(self):
        self._employee_id=None
        self.name=None
        self.age=None
        self._salary=None

    def get_employee_id(self):
        return self._employee_id
    def get_employee_name(self):
        return self.name

    def set_employee_id(self,ID):
        self._employee_id=ID
    def set_employee_name(self,name):
        self.name=name
    def set_employee_age(self,age):
        self.age=age
    def set_employee_salary(self,salary):
        self._salary=salary

    def display(self):
        print("Employee details:")
        print(f"Name :{self.name}")
        print(f"age :{self.age}")
        print(f"ID :{self._employee_id}")
        print(f"salary :{self._salary}")

    def _del_(self):
        print(f"employee {self.name} is destroyed")


class Manager(Employee):
    def _init_(self):
        super()._init_()
        self._department=None
    def set_department(self,department):
        self._department=department
    def display(self):
        print("Manager details:")
        print(f"Name :{self.name}")
        print(f"age :{self.age}")
        print(f"ID :{self._employee_id}")
        print(f"salary :{self._salary}")
        print(f"departmment :{self._department}")
    def _del_(self):
        print(f"Manager {self.name} is destroyed")

class Developer(Employee):
    def _init_(self):
        super()._init_()
        self._language=None
    def set_language(self,lan):
        self._language=lan
    def display(self):
        print("Developer details:")
        print(f"Name :{self.name}")
        print(f"age :{self.age}")
        print(f"ID :{self._employee_id}")
        print(f"salary :{self._salary}")
        print(f"language :{self._language}")
    def _del_(self):
        print(f"Developer {self.name} is destroyed")

print("--- python OOP project :Employee management system ---")
per1=None
emp1=None
mng1=None
dev1=None
while True:
    print("choose an option:")
    print("1.Create  a person")
    print("2.Create  a employee")
    print("3.Create  a manager")
    print("4.Create  a Developer")
    print("5.Show details")
    print("6.Exit")
    try:
        choice=int(input("Enter your choice:"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice==1:
        per1=Person()
        name=str(input("Enter Name:"))
        age=int(input("Enter Age:"))

        per1.set_person_name(name)
        per1.set_person_age(age)
        print(f"A person created with Name :{name} and age :{age}")
    elif choice==2:
        emp1=Employee()
        name=str(input("Enter Name:"))
        age=int(input("Enter Age:"))
        ID=str(input("Enter ID:"))
        salary=int(input("Enter salary:"))

        emp1.set_employee_name(name)
        emp1.set_employee_age(age)
        emp1.set_employee_id(ID)
        emp1.set_employee_salary(salary)
    elif choice==3:
        mng1=Manager()
        name=str(input("Enter Name:"))
        age=int(input("Enter Age:"))
        ID=str(input("Enter ID:"))
        salary=int(input("Enter salary:"))
        department=str(input("Enter Department:"))

        mng1.set_employee_name(name)
        mng1.set_employee_age(age)
        mng1.set_employee_id(ID)
        mng1.set_employee_salary(salary)
        mng1.set_department(department)

        if issubclass(type(mng1), Employee):
            print(f"{type(mng1).__name__} is a subclass of Employee")
    elif choice==4:
        dev1=Developer()
        name=str(input("Enter Name:"))
        age=int(input("Enter Age:"))
        ID=str(input("Enter ID:"))
        salary=int(input("Enter salary:"))
        lan=str(input("Enter Language:"))

        dev1.set_employee_name(name)
        dev1.set_employee_age(age)
        dev1.set_employee_id(ID)
        dev1.set_employee_salary(salary)
        dev1.set_language(lan)

        if issubclass(type(dev1), Employee):
            print(f"{type(dev1).__name__} is a subclass of Employee")

    elif choice==5:
        print("Choose details to show:")
        print("1.Person")
        print("2.Employee")
        print("3.Manager")
        print("4.Developer")
        try:
            Choicee=int(input("Enter your choice:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if Choicee==1:
            if per1==None:
                print("there is no data of any person. please enter any data first")
            else:
                per1.display()
        elif Choicee==2:
            if emp1==None:
                print("there is no data of any employee. please enter any data first")
            else:
                emp1.display()
        elif Choicee==3:
            if mng1==None:
                print("there is no data of any manager. please enter any data first")
            else:
                mng1.display()
        elif Choicee==4:
            if dev1==None:
                print("there is no data of any developer. please enter any data first")
            else:
                dev1.display()
        else:
            print("invalid option")

    elif choice==6:
        del emp1
        del mng1
        del per1
        del dev1
        print("Exiting the system All resources have been freed")
        break
    else:
        print("invalid option")


# In[ ]:




