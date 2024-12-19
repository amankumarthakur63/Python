# Get a number from user

x = int (input ("What's your number? "))
print (f"x is {x}")

# Catches the value error

try:
    x = int (input ("What's x? "))
    print (f"x is {x}")
except ValueError:
    print ("x is not an integer")    

# Demonstrates a NameError    

try:
    x = int (input ("What's x? "))
except ValueError:
    print ("x is not an integer")    

print (f"x is {x}")    

# Demonstrates else

try:
    x = int (input ("What's x? "))
except ValueError:
    print ("x is not an integer")    
else:
    print (f"x is {x}") 

# Demonstrates a loop

while True:
    try:
        x = int (input ("What's x? "))
    except ValueError:
        print ("x is not an integer")    
    else:
        break

print (f"x is {x}") 

# Adds functions, uses break and return

def main ():
    x = get_int ()
    print (f"x is {x}")

def get_int ():
    while True:
        try:
            x = int (input ("Whst's x? "))    
        except ValueError:
            print ("x is not an integer")
        else:
            break
    return x     

main()      


# # Removes break

def main():
    x = get_int ()
    print (f"x is {x}")

def get_int ():
    while True:
        try:
            x = int (input ("What's x?"))    
        except ValueError:
            print("x is not an integer")
        else:
            return x       

main()         


# Removes else

def main():
    x = get_int ()
    print (f"x is {x}")

def get_int ():
    while True:
        try:
            x = int (input ("What's x?"))    
        except ValueError:
            print("x is not an integer")      

main()  

# # Adds pass

def main():
    x = get_int ()
    print (f"x is {x}")

def get_int ():
    while True:
        try:
            x = int (input ("What's x?"))    
        except ValueError:
            pass     

main()  


# Adds prompt

def main():
    x = get_int ()
    print (f"x is {x}")

def get_int (prompt):
    while True:
        try:
            x = int (input (prompt))    
        except ValueError:
            pass     

main()  


