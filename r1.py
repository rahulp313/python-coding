x=int(input("Enter the first number: "))
y=int(input("Enter the secound number: "))
add=x+y
sub=x-y
multy=x*y
divide=x/y
power=x**y
print("enter")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for divide")
print("5 for power")
i=1
while i==1:
    z=int(input("Enter: "))
    if z==1:
        print(add)
    elif z==2:
        print(sub)
    elif z==3:
        print(multy)
    elif z==4:
        print(divide) 
    elif z==5:
        print(power) 
    else :
        print("enter corect number")

    i=int(input("enter 1 to continue: "))
        
    

