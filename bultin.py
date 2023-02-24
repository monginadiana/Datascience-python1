#built in methods
#functions are reusable pieces of code
#objects are collection of data and functions, if we have a certain function associated to a specific object we call it a method.

#we have a number of built-in function and methods 
#built-in functions are the ones you write first e.g type(), sort(), len(), while methods you write them after e.g capitalize() uppercase()

#.lower() makes all characters in string to lowercase
#.capitalize() makes first letters in string to uppercase
#.uppercase() makes all characters in string to uppercase

name = "diana"

print (name.capitalize())
print (name.lower())
print (name.upper())

# append()to add an item in array. pop() to remove the last element in array or the specified index. and extend () to add elements in first list to a second list are mostly in array
arr1 =[1,2,3,4]
arr2 =[4,8,10,12]
arr1.append(9)
arr1.pop(1)
arr1.extend(arr2)
print(arr1)

#functions 

#print(takes as many items as you want to)
#type(takes in a single item ) to represent the data type.
#len(to check the length of the data)
#sum(to change the sum of items in the array)
#max(identity the maximum number of items)
#min(identity the minimum number of items)

#Pythonn operators

#comparison operator(takes two elements and compares the value then returns that in either true or false)
#==(equality measure)
#!=(inequality)
#<><=>=(greater,lesser, greater or equal or lesser than or equal to)


print(False == False)
"hello" == "hello"
"1" == 1
"1" != 1

#built in functions/methods labs

#Desired output: "HELLO, THERE"
yell_hello = "hello, there" 
yell_hello = yell_hello.upper()
print(yell_hello)

# Desired output: "psst, hey"
whisper_hey = "PSST, HEY" 
whisper_hey = whisper_hey.lower()
print(whisper_hey)

# Desired output: "Learn. Love. Code"
flatiron_mantra = "LEARN. LOVE. CODE." 
flatiron_mantra = flatiron_mantra.capitalize()
print(flatiron_mantra)

# Desired output: str
type_string = "i'm a string" 
type_string = str(type_string)
print(type_string)

# Desired output: list
type_list = ["i'm", "a", "list"] 
type_list = list(type_list)
print(type_list)

# Desired output: 3
length_of_list = ["i'm", "a", "list"] 
length_of_list = len(length_of_list)
print(length_of_list)


# Desired output: "list"
longest_word_in_list = ["i'm", "a", "list"]
longest_word_in_list = type(longest_word_in_list)
print(longest_word_in_list)

# Desired output: 1
smallest_number = [1, 3, 4, 78]
smallest_number = smallest_number.pop(0)
print (smallest_number)

# Desired output: 11
sum_of_numbers = [1, 2, 3, 5]
sum_of_numbers = sum (sum_of_numbers)
print (sum_of_numbers)


#comparison operators

boolean_compare = True != True # False
boolean_compare2 = False == True # False
print(boolean_compare, boolean_compare2)

number_compare = 10 == 10 # True
number_compare2 = -20 != 30 # True
number_compare3 = 4 >= 5 # False
print(number_compare, number_compare2, number_compare3)

list_compare = [0, 0, 0, 0] > [0, 0, 0] # True
list_compare2 = [1, 0, 0] > [0, 0, 0] # True
list_compare3 = [0, 0, 0] > [0, 0, 3] # False
list_compare4 = [0, 0, 3, 0] > [0, 0, 3] # True
list_compare5 = [0, 0, 4, 0] < [0, 0, 3] # False
print(list_compare, list_compare2, list_compare3, list_compare4, list_compare5)

#logical operators

#and operators (both x and y comparisons have to be true otherwise the result will be false. if x is true and y is false, the result will be false)
#the and operator returns the first operand if it evaluates to False, and the second operand otherwise. In this case, the first operand is True, which evaluates to True, so the second operand (2) is returned.

#or operators (both x and y comparisons to return true. so if x is true and y false the result is true

print("1.", 2 and 0) #  0
print("2.", False and 2) # false
print("3.", True and 2) # 2
print("4.", 2 and 3) # 3
print("5.", 2 or []) #2
print("6.", 0 or []) #[]
print("7.", not False) # true
print("8.", not True) # false
print("9.", not []) # true
print("10.", not 0) # true
print("11.", not 100) # false

#not returns the opposite of the boolen value, if it's true, it returns false and vice versa

#identity operator (checks if elements are == or !=  thte only difference is that they check on elements ewuality not value equality.

print("1.", {} is {}) # true
print("1A.", {} == {}) # true
print("2.", [] is []) # true
print("3.", "Hi" is "Hi") # true
print("4.", ["same"] is ["same"]) # true
print("4A.", ["same"] == ["same"]) #true
print("5.", 9 is not 10) # true

 
# not returns a boolean value that is the opposite of the truthy/falsy value of the element.

#terniary operators :great for comparison of variables in a single line 

val = False

val = 'diana' if val else 'elvis'
print (val)


a = []
b = a
identity_compare = {} is {} # False
identity_compare2 = a is  b # True
identity_compare3 = b is not [] # True
identity_compare4 = 9 is not 10 # True
identity_compare5 = "Same" is not "Same" # False
identity_compare6 = [1,3,4] is [1,2,3] # False
print(identity_compare, identity_compare2, identity_compare3,
      identity_compare4, identity_compare5, identity_compare6)