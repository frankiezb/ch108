print("hello world!")
var = 10
print (var)

#variables
x = 5
y = 3

#operations
sum = x + y
print (sum)

# srting operations
name = "donald"
greeting = "hello" + name + "!"
print (greeting)

#list // this is the array
numbers = [1, 2, 3, 4, 5]

age = 22
if age > 21:
        print("youre an adult")
else:
        print ("youre a minor")

# define the function in python
def greet(name) :
    return "Hello " + name
# call the function in python 
result = greet("Donald")
print(result)

#function to calculate the power of a number 
def power(base, exponent=2):
    return base ** exponent
#call the function 
result = power(2)
result2 = power(3,3)
#print result
print(result)
print(result2)
#createa function that multiply 2 parameters (numbers)
def multiply( number1, number2):
    multiplyResult = number1*number2
    return multiplyResult
#call the function 
product = multiply(12,12)
print(product)
