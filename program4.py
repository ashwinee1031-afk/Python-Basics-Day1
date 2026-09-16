#Write calculator program 

x =int(input("Enter 1st number:"))
y =int(input("Enter 2nd number:"))
while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3Multiplication.")
    print("4.Division")
    print("5.Factorial")
    print("6.Exit")
    
    choice = int(input("Enter your choice:"))
    if choice==1:
        print("Addition",x+y)
    elif choice==2:
        print("Subtraction",x-y)
    elif choice==3:
        print("Multiplication",x*y)        
        
        
    
    


