#!/usr/bin/env python
# coding: utf-8

# In[9]:


print("welcome to the Data Analyzer and transformer program")
L1=None
A_choice=None
while True:
    print("Main menu:")
    print("1.Input data")
    print("2.Display data summary")
    print("3.calculate factorial")
    print("4.Filter data by threshold")
    print("5.Sort data")
    print("6.Display dataset statisticts")
    print("7.Exit program")

    choice=int(input("please Enter your choice:"))
    if choice==1:
        A_choice=int(input("Enter 1 for 1D array and 2 for 2D array:"))
        if A_choice==1:
            print("Enter data for 1D Array (seperated by spaces):")
            L1 = list(map(int, input().split()))
            print("Data has been stored successfully!")

        elif A_choice==2:
            rows=int(input("Enter number of rows:"))
            cols=int(input("Enter number of columns:"))
            L1=[list(map(int,input(f"Enter row {i+1} elements (seperated by spaces)").split())) for i in range(rows)]
            print(L1)
    elif choice==2:
        if L1 is None:
            print("No data available! Please input data first.")
            continue
        print(L1)
        if A_choice==2:
            flat=[num for row in L1 for num in row ]

            print("Data summary:")

            print(f"- Total elements: {len(flat)}")
            print(f'- Minimum Value: {min(flat)}')
            print(f'- Maximum Value: {max(flat)}')
            print(f'- Sum of all Values: {sum(flat)}')
        if A_choice==1:
            print("Data summary:")

            print(f"- Total elements: {len(L1)}")
            print(f'- Minimum Value: {min(L1)}')
            print(f'- Maximum Value: {max(L1)}')
            print(f'- Sum of all Values: {sum(L1)}')
    elif choice==3:
        fact=int(input("Enter a number to calculate its factorial:"))
        if fact<=0:
            print("please enter a positive number.")
        else:
            def factorial(n):
                if n==0 or n==1:
                    return 1
                else:
                    return n*factorial(n-1)
            result=factorial(fact)
            print(f"the factorial of {fact} is :{result}")
    elif choice==4:
        if L1 is None:
            print("No data available! Please input data first.")
        value=int(input("enter a threshold value to filter out data above this value:"))
        if A_choice==1:
            filtered=list(filter(lambda x:x>value,L1))
            print(f'filtered data (values>{value}):{filtered}')
        if A_choice==2:
            flat=[num for row in L1 for num in row ]
            filtered=list(filter(lambda x:x>value,flat))
            print(f'filtered data (values>{value}):{filtered}')
    elif choice==5:
        if L1 is None:
            print("No data available! Please input data first.")
        print("choose sorting option:")
        print("1.Ascending")
        print("2.Descending")
        S_choice=int(input("Enter your choice:"))
        if S_choice==1:
            if A_choice==1:
                L1.sort()
                print("sorted data in acending order:")
                print(L1)
            if A_choice==2:
                flat=[num for row in L1 for num in row ]
                flat_sort=sorted(flat)
                print("sorted data in acending order:")
                print(flat_sort)
        if S_choice==2:
            if A_choice==1:
                L1.sort(reverse=True)
                print("sorted data in acending order:")
                print(L1)
            if A_choice==2:
                flat=[num for row in L1 for num in row ]
                flat_sort=sorted(flat,reverse=True)
                print("sorted data in acending order:")
                print(flat_sort)

    elif choice==6:
        if L1 is None:
            print("No data available! Please input data first.")
            continue

        def calculate_average(data):
            """Calculates the average of the provided data."""
            if len(data) == 0:
                return 0
            return sum(data) / len(data)

        def dataset_stats(*args, **kwargs):
            """Returns dataset statistics such as min, max, sum, average, and total count."""
            data=args[0]
            if A_choice == 2:
                data = [num for row in data for num in row]
            total = len(data)
            minimum = min(data)
            maximum = max(data)
            total_sum = sum(data)
            average = calculate_average(data)
            return minimum, maximum, total_sum, average, total

        minimum, maximum, total_sum, average, total = dataset_stats(L1)
        print("Dataset statistics:")
        print(f"- Total elements: {total}")
        print(f"- Minimum value: {minimum}")
        print(f"- Maximum value: {maximum}")
        print(f"- Sum of all values: {total_sum}")
        print(f"- Average value: {average:.2f}")
    elif choice==7:
        print("Thank you for using data Analyzer and transformer program. Goodbye!")
        break
    else:
        print("invalid choice")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




