# Demonstrates a function with a positinal argument

print ("Hello World")

# Demonstrates a function with a positional argument and a return value

name = input ("What's your name ")
print ("hello,")
print (name)

# Demonstarates concatenation of strings

name = input ("What's your name : ")
print ("hello, " + name)

# Demanstrates a function with a positional and a named argument

name = input ("What's your name ? ")
print ("Hello, ", end="")
print (name)

# Demonstrates a format string

name = input ("What's your name ? ")
print (f"hello, {name}")

# Demonstrates str functions

name = input ("What's your name ? ").strip().title()
print (f"hello, {name}")

# Demonstrates str functions

name = input ("What's your name ? ").strip().title()
first, last = name.split (" ")
print (f"hello, {name}")


# Demonstrates addition

x = 11
y = 12

z = x + y
print (z)

# Demonstrates (unintended) concatenation of strings

# Prompt user for two integers

x = input ("What's x ")
y = input ("What's y ")

# # Print sum

z = x + y
print (z)

# Output

# What's x 5
# What's y 9
# 59


# Demonstrates conversion from string to int

x = input ("What's x ")
y = input ("What's y ")

z = int(x) + int(y)
print (z)

# Output

# What's x 5
# What's y 9
# 14

# Demonstrates nesting of function calls

x = int (input ("What's x ? "))
y = int ( input ("What's y ? "))

z = x + y
print (z)

# Output

# What's x ? 6
# What's y ? 6
# 12

# Demonstrates conversion from string to float

x = float (input ("What's x ? "))
y = float (input ("What's y ? "))

z = x + y
print (z)

# Output

# What's x ? 6
# What's y ? 6
# 12.0

# Demonstrates rounding to nearest int

x = float (input ("What's x ? "))
y = float (input ("What's y ? "))

z = round (x + y)
print (z)

# Output

# What's x ? 4.3
# What's y ? 4.3
# 9

# Demonstrates fewer variables

x = float (input ("What's x ? "))
y = float (input ("What's y ? "))

print (round (x + y))

# Output

# What's x ? 4.2
# What's y ? 4.2
# 8

# Demonstrates formatting with commas

x = float (input ("What's x ? "))
y = float (input ("What's y ? "))

z = x + y
print (f"{z:,}")

# Output

# What's x ? 1000
# What's y ? 20000
# 21,000.0

# Demonstrates division

x = float (input ("what's x ? "))
y = float (input ("What's y ? "))

z = x / y
print (z)

# Output

# what's x ? 4.5
# What's y ? 6.7
# 0.6716417910447761

# Demonstrates rounding after the decimal point

x = float (input ("What's x ? "))
y = float (input ("What's y ? "))

z = round (x / y, 2)
print (z)

# Output

# What's x ? 4.654646
# What's y ? 3.453556
# 1.35

# Demonstrates formatting after the decimal place

x = float (input ("What's x ? "))
y = float (input ("What's y ? "))

z = x / y
print (f"{z:.2f}")

# Output

# What's x ? 4.353534
# What's y ? 3.343455
# 1.30

# Demonstrates defining a function without parameters

def hello ():
    print ("hello")

name = input ("What's your name ? ")    
hello ()
print (name)

# Output

# What's your name ? Aman Kumar
# hello
# Aman Kumar

# Demonstrates defining a function with a parameter

def hello (to):
    print ("hello,", to)

name = input ("What's your name ? ")    
hello (name)

# Output

# What's your name ? Aman Kumar
# hello, Aman Kumar

# Demonstrates defination of main function

def main():
    name = input ("What's your name? ")
    hello (name)

def hello (to= "world"):
    print("hello, ", to)

main()     

# Output

# What's your name? Aman Kumar
# hello,  Aman Kumar

# Demonstrates defining a function with a return value

def main():
    x = int (input ("What's x? "))
    print ("Square is", square (x))

def square (n):
    return n * n;

main()    

# Output
# What's x? 69
# Square is 4761