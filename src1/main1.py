# Demonstrates conditions

x = int (input ("What's x ? "))
y = int (input ("What's y ? "))

if x < y:
    print ("x is less than y")
if x > y:
    print ("x is greater than y") 
if x == y:
    print ("x is eqaul to y")       

# Demonstrates the mutually exclusive conditions

x = int (input ("What's x ? "))    
y = int (input ("What's y ? "))

if x < y:
    print ("x is less than y")
elif x > y:
    print ("x is greater than y")   
elif x == y:
    print ("x is equals to y")     

# Demonstrates fewer conditions

x = int (input ("What's x ? "))
y = int (input ("What's y ? "))

if x > y:
    print ("x is greater than y")
elif x < y:
    print ("x is less than y")    
else:
    print ("x is equal to y")    

# Demonstrates inequalities and logic operations

x = int (input ("What's x ? "))
y = int (input ("What's y ? "))

if x > y or x < y:
    print ("x is not equal to y")
else:
    print ("x is equal to y")    

# Demonstrates equality

x = int (input ("What's x ? "))
y = int (input ("What's y ? "))

if x ==y:
    print ("x is equal to y")
else:
    print ("x is not equal to y")    

# Demonstrates inequality

x = int (input ("What's x ? "))
y = int (input ("What's y ? "))

if x != y:
    print ("x is not equal to y")
else:
    print ("x is equal to y")   

# Demonstrates inequalities and logical operations

score = int (input ("Score : "))

if score >= 90 and score <= 100:
    print ("Grade : A")
elif score >= 80 and score < 90:
    print ("Grade : B")    
elif score >= 70 and score < 80:
    print ("Grade : C")
elif score >= 60 and score < 70:
    print ("Grade : D")         
else:
    print ("Grade : F")

# Demonstrates inequalities and logical operations    

score = int (input ("Score : "))

if 90 <= score and score <= 100:
    print ("Grade : A")
elif 80 <= score and score < 90:
    print ("Grade : B")    
elif 70 <= score and score < 80:
    print ("Grade : C")
elif 60 <= score and score < 70:
    print ("Grade : D")         
else:
    print ("Grade : F")    

# Demonstrates chained comparisons


score = int (input ("Score : "))

if 90 <= score <= 100:
    print ("Grade : A")
elif 80 <= score < 90:
    print ("Grade : B")    
elif 70 <= score < 80:
    print ("Grade : C")
elif 60 <= score < 70:
    print ("Grade : D")         
else:
    print ("Grade : F") 


# Demonstrates fewer cmparisons

score = int (input ("Score : "))

if 90 <= score:
    print ("Grade : A")
elif 80 <= score:
    print ("Grade : B")    
elif 70 <= score:
    print ("Grade : C")
elif 60 <= score:
    print ("Grade : D")         
else:
    print ("Grade : F") 

# Compares strings 

answer = input ("Do you agree? ")   
if answer =="yes":
    print ("Agreed")
else:
    print ("Not agreed")    

# Strips string before comparing  

answer = input ("Do you agree? ").strip()   
if answer =="yes":
    print ("Agreed")
else:
    print ("Not agreed")      


# LowerCases string before comparing 

answer = input ("Do you agree? ").strip().lower()  
if answer =="yes":
    print ("Agreed")
else:
    print ("Not agreed")   

# Compare multiple strings       

answer = input ("Do you agree? ").strip().lower()  
if answer =="yes" or answer == "y":
    print ("Agreed")
else:
    print ("Not agreed") 

# Compare multiple string    

answer = input ("Do you agree? ").strip().lower()  
if answer.startswith ("y"):
    print ("Agreed")
else:
    print ("Not agreed") 


# Demonstrates modulo operator

x = int (input ("what's x? "))

if x % 2 == 0:
    print ("Even")
else:
    print ("Odd")    

# Demonstrates a function thaat returns a bool

def main ():
    x = int (input ("What's x? "))
    if is_even(x):
        print ("Even")
    else:
        print ("Odd")

def is_even (n):
    if n % 2 == 0:
        return True
    else:
        return False
main()                   

# Demonstrates conditional expreesions (ternary operators)

def main ():
    x = int (input ("What's x? "))
    if is_even(x):
        print ("Even")
    else:
        print ("Odd")

def is_even (n):
    return True if n % 2 == 0 else False
        
main()                 

# demonstrates returning the value of Boolean expression

def main ():
    x = int (input ("What's x? "))
    if is_even(x):
        print ("Even")
    else:
        print ("Odd")

def is_even (n):
    return n % 2 == 0
    
main()           

# Compare multiple string with if/elif/else

name = input ("What's your name? ")

if name == "Harry":
    print ("Gryffindor")
elif name == "Hermione":
    print ("Gryffindor")    
elif name == "Ron":
    print ("Gryffindor")    
elif name == "Draco":
    print ("Slytherine")
else:
    print ("Who? ")

# Uses or

name = input ("What's your name? ")

if name == "Harry" or "Hermione" or "Ron":
    print ("Gryffindor")    
elif name == "Draco":
    print ("Slytherine")
else:
    print ("Who? ")

# Uses match with case    

name = input ("what's your name? ")
match name:
    case "Harry":
        print ("Gryffindor")
    case "Hermione":
        print ("Gryffindor")    
    case "Ron":
        print ("Gryffindor")    
    case "Draco":
        print ("Slytherin")    
    case _:
        print ("who?")    

# Uses |

name = input ("what's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print ("Gryffindor")   
    case "Draco":
        print ("Slytherin")    
    case _:
        print ("who?")  


