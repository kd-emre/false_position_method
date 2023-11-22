iteration = 1

#The function whose root we want to find
def f(x):
    f = float(x) * float(x) - float(x) - 1
    return f

#Generating the third point
def uc(f0, f1, x0, x1):
    uc = ( float(x0) * float(f1) - float(x1) * float(f0) ) / ( float(f1) - float(f0))
    return uc

#We are examining which two out of three points might enclose the root.
def yeni(a, b, c):
    if ( float(f(a)) * float(f(c)) < 0):
        x0 = a 
        x1 = c
        return (x0,x1)
    
    elif (float(f(c)) * float(f(b)) < 0):
        x0 = c 
        x1 = b 
        return (x0,x1)
    else :
        print("Root of function is" , c)


print("Our function is, f = x*x - x - 1")

x0 = input("Please enter a begining point: ")
x1 = input("Please enter a end point: ")

aiteration = input("Please enter the number of iterations you'd like to perform: ")


if (f(x0) * f(x1) < 0) :  
  

    while (iteration <= int(aiteration)):
        print(iteration , ". iteration result is " , uc(f(x0), f(x1), x0, x1))
        (x0, x1) = yeni(x0, x1,uc(f(x0), f(x1), x0, x1))
        iteration = iteration + 1
    
elif (f(x0) * f(x1) == 0) :
        if ( f(x0) == 0 ) :
            print("Root of function is" , x0)
            
        else :
            print("Root of function is" , x1)

else :
    print("There is no root between these two point.")
    
    
