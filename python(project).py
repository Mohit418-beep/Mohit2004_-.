print("Welcome to the Interactive personal data collector")

name = str(input("Enter your name: "))
age  = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
fev_num = int(input("Enter your fevorite Number: "))

print("thank you! here is the information we have collected:")

print("Name :",name,("Type:", type(name),"Memory Address:",id(name)))
print("age :",age,("Type:", type(age),"Memory Address:",id(age)))
print("height :",height,("Type:", type(height),"Memory Address:",id(height)))
print("fevorite number :",fev_num,("Type:", type(fev_num),"Memory Address:",id(fev_num)))

print("your birth year is approximately: ",2025-age,(("based on your age of"),age))

print("thank you for using the personal data collector, Goodbye")
