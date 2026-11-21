#Integer pass by value
def pass_by_value(x):
    x=15
    print(x,id(x))
    
x=10
pass_by_value(x)
output--> 15 140731666113896

print(x,id(x))
output--> 10 140731666113736

"""whenever you are passing Objects like int, string it will pass values the function, hence the changes within the function will not reflect outside of the function."""

#string pass by value
def pass_by_value(str):
    str='hello'
    print(str,id(str))

str='hi'
pass_by_value(str)
#hello 1512650608000
print(str,id(str))
#hi 140731666157440

#pass by reference
def pass_by_reference(lst):
    lst.append(50)
    print(lst,id(lst))

# call pass_by_reference() function and pass lst

lst = [10,20,30,40]
pass_by_reference(lst)
#output: [10, 20, 30, 40, 50] 1512653114816

"""whenever you are passing Objects like list, tuple, range, bytes, bytearray, set, frozenset and dictionary, it will not pass values, it will pass memory location of the object, hence the changes will reflect to the function as well."""

print(lst,id(lst))
#output: [10, 20, 30, 40, 50] 1512653114816

