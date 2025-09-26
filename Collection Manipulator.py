#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Welcome To The Student Data Organizer!")

records = []

while True:
    print("\nMenu:")
    print("Select an option:")
    print("1. Add Student")
    print("2. Display all Student")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    ch = int(input("\nEnter Your Choice from 1-6:"))

    if ch == 1:
        print("Enter Student Details:")
        sid = int(input("Enter Student Id:"))
        name = input("Enter Name:")
        age = int(input("Enter Age:"))
        grade = input("Enter Grade:")
        date = input("Date Of Birth (DD-MM-YYYY):")
        subject = set(input("Subjects (comma-seprated):").split(','))

        student = {
                "ID": sid,
                "Name": name,
                "Age": age,
                "Grade": grade,
                "DOB": date,
                "Subjects": subject
        }

        records.append(student)
        print("Student Added Successfully!")
    elif ch == 2:
        if not records:
            print("No Student records found.")
                els: for s in records:
                print("ID :",sid)
                print("Name :",name)
                print("Age:",age)
                print("Grade:",grade)
                print("DOB:",date)
                print("Subjects:",','.join(s["Subjects"]))

    elif ch == 3:
        uid = int(input("Enter student Id To update:"))
        found = False
        for s in records:
            if s["ID"] == uid:
                found = True
                print("1. Update Age\n2. Update subjects")
                update_choice = input("Choose what to update:")
                if update_choice == "1":
                s["Age"] = int(input("Enter Age:"))
                    print("Age Updated.")
    elif update_choice == "2":
                    new_subjects = set(input("Enter new subjects(comma-seprated):").split(","))
                    s["Subjects"] = new_subjects
                print("subjects Updated.")
                break
        if not found:
            print("Student Id not Found.")

    elif ch == 4:
        uid = int(input("Enter student Id To Delete:"))
        for s in records:
            if s["ID"] == uid:
                records.remove(s)
                print("student record deleted.")
                break
            else:
                print("student Id not Found.")

    elif ch == 5:
        all_subjects = set()
        for s in records:
            all_subjects.update(s["Subjects"])
            print("Subjects Offered:",','.join(all_subjects))

    elif ch == 6:
        print("Thank you for using the student data Organizer.GoodBye!")
    break

    else:
        print("Invalid Choice. Please try again.")


# In[ ]:




