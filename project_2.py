#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to the Pattern Generator and Number Analyzer!")
while True:
    print("Select an option")
    print("1. Generate a Pattern")
    print("2. Analyze a range of numbers")
    print("3. Exit")
    
    choice = int(input("Enter Your Choice: "))
    
    if choice >= 1 and choice <= 3:
        
        if choice == 1:
            rows = int(input("Enter the number of rows: "))
            for i in range(1, rows + 1):
                print("*" * i)
                
        elif choice == 2:
            a = int(input("Enter the start of range: "))
            b = int(input("Enter the end of range: "))
            total = 0
            for i in range(a, b + 1):
                total += i
                if i % 2 == 0:
                    print("value", i, "even")
                else:
                    print("value", i, "odd")
            print("Sum of all numbers:", total)   
            
        else:
            print("Exiting the Program. Goodbye!")
            break
    else:
        print("Invalid choice")   


# In[ ]:




