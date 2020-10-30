#Functions can be treated as values in some programming languages. If a value can be used for assignment, parameters, return types, etc., 
#such a value is called as a 
#first class citizen.

For example
def check_bag(number):
    print("Number of bags checked ",number)

x=check_bag
x(4)

#Higher Order functions are those functions which can either accept another function as a parameter or return another function or both:
#Accept another function as a parameter:
def add(x,y):
    return x+y
def call_function(func1,a,b):
    ret=func1(a,b)
    return ret
print(call_function(add,10,20))

#Return another function:
def ret_function(a,b):
    a=a*a;
    b=b*b;
    return lambda :a+b
new_func=ret_function(2,3);
print(new_func())
