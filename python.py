#assigning variables

#vairables are storage locations for data

#an aexample of a variable is 

name = "diana mongina"

email ="diana@gmail.com"

school = "moringa school"

print (email, name)

#Declaring varables without assgnments

#creating a vraible without assigning it to a data brings an error, good thing in python we have a non data type that allows you to pass it in variables incase you have no data to store it.

address = "none"

# unlike vaariables, data can be passed without assigning them to varibles

()

"diana mongina"

"moringa school"

print ("moringa school")

# we can combine multiple vairables to create a string (Reassigning variables)

print (" send an letter to "  + school +  " in reference to "  + name + " and " + email)


#reassigninh variables 

#incase you want to change the email and names you can reasign the variables to diffrent data

name  = "johan monica"

email = "joanmonicah@gmail.com"

school = "zelego academy"

header = "orientation"


print (" send an letter to "  + school +  " in reference to "  + name + " and " + email)

#STRINGS(datatypes.)
# infor in the  world is text and to make it usable in python or any programming, you have to make it a string.
# this is done by add  ""  or '' to the text

#other forms of data types are boolean(true or false), floats(decimals), integers(1,2,3) 
# to i dentify the type of data in program we use type()

print(type("diana"))

print(type("43"))

print(type(40))

print(type(40.2))

#methods in python

#upper() to change a string to upper case or capital letters
#endswith() to check what comes last in a name or string answers false or true


print(name.upper())

print(name.endswith("ondieki")) 


#capitalie() helps us to change the first letter to upper case

print(name.capitalize())

print(header.title())

sentence = "woW WE LOVE cOdInG and strINGS!"

#LABs
print(sentence.capitalize())

flatiron_mantra = "learn. love. code."
print(flatiron_mantra.title())

#convert integgers to strings
num_to_string = 1234

str_number = str(num_to_string)
print(type(str_number))



full_address = str_number + " abc street, HomeTown USA"


print(" this is my address " + str_number + " Abc street, HomeTown USA  ")


full_name = "diana mongina"

last_name = "ondieki"

full_name =  full_name.replace("mongina", last_name)

print(full_name)


ends_with_com = "art.vandelay@vandelay.co" # False
print(ends_with_com.endswith(".com"))

web_address = 'vandelay.com' # 'www.vandelay.com'
print("www." + web_address)

#convert number to integers

phone_num_one = "7285553334" # 7285553335
print (int(phone_num_one))

#how to access the last value

phone_num_one = "7285553334"
new_digit = "5"

# Slice the original phone number string to remove the last digit and concatenate the new digit
new_phone_num_str = phone_num_one[:-1] + new_digit

# Convert the modified phone number string to an integer
new_phone_num_int = int(new_phone_num_str)

# Print the modified phone number as both a string and an integer
print("Modified phone number as string:", new_phone_num_str)
print("Modified phone number as integer:", new_phone_num_int)



travel_month= "january"

number_of_weeks = 5

travelling_schedule = " I will be travelling " + str(number_of_weeks) + " weeks  starting in the month of " + travel_month


print (travelling_schedule)


#Conditional Loops 

#execution flow

vacation_days = 1

vacation_days = vacation_days +1

vacation_days += 1

print (vacation_days)

#+1 allows you to increament current to value

# -1 allows you decrement cureent value

#statements , we have three staments in python, if, elif, else 

#ane example is a addition of leave days if goal is met in each quater

leave_days = 21

goals = True

if goals :
    leave_days  += 1

else:
    "no leave days added"

print(leave_days)

leave_days = 21

goals = False
goals_exceeded = True

if goals :
    leave_days  += 1

elif goals_exceeded :
    leave_days += 4

else:
    "no leave days added"

print(leave_days)

#Else block comes last and it only runs if the conditions have not been met.

#we have Truthy and falsey valuees: TRuth values include :any integer above 0 an falsey values is 0, Falsey could also be empty list and strings and none data types

#to check if truthy or falsey 

print(bool(0))

print(bool(None))

print(bool(""))

print(bool([]))

print(bool(2))

# we can use them for mathematical operations, not that true is always set to 1 and false is always set to 0

print(True + 6 + False)

# this will equate to 7

#Decisions in data

#make decision to decide if budget is working for you

budget = 40000

if budget  < 39000:
   print("you are on track")

elif budget  == 40000:
    print( "mind reducing kidogo entertainment budget to 1000")

else: 
    print(" it's 2023, will you ever let money work for you sis?")


#conditional labs

number_50 = 50
my_number = None

if number_50 > 100:
    my_number = 100
    print(my_number)
    # if number_50 is greater than 100, assign the `my_number` variable to the number 100
elif number_50 > 50:
    my_number = 50
    print(my_number)
    # if number_50 is greater than 50, assign the `my_number` variable to the number 50
else:
    my_number = 0
    print(my_number)
    # else assign the `my_number` variable to 0


#days in a week

today_is = 8
day_of_the_week = None
if today_is == 4:
    day_of_the_week = "thursday"
    print(day_of_the_week)
elif  today_is == 3:
    day_of_the_week = "wednesday"
    print(day_of_the_week)
elif  today_is == 2:
    day_of_the_week = "tuesday"
    print(day_of_the_week)
elif  today_is == 1:
    day_of_the_week = "monday"
    print(day_of_the_week)
elif  today_is == 5:
    day_of_the_week = "friday"
    print(day_of_the_week)
elif  today_is == 6:
    day_of_the_week = "sartuday"
    print(day_of_the_week)
elif  today_is == 7:
    day_of_the_week = "sunday"
    print(day_of_the_week)
else :
    print ("we have no such week")


string = "Python"
sub_string = "on"
ends_with = None

if string.endswith(sub_string):
    ends_with = True;
    print(ends_with)
else:
    ends_with = False;
    print(ends_with)
# conditionals go here

#list : a collection of groups, could cities,  states, countries, mountains [ use coma to separate items in a list]


restraurants= ["cafedelli", "java", "mint and salt", "artcaffe"]

print(restraurants)

#assess items in a list, we assign them an index. (o,1,2,3 ...)

print(restraurants[0]) #this prints out cafedelli

#you can access more than two items in alist [1:2]
print(restraurants[1:2])

#slicing, a concept in list that helps you  find a specific index in a list. slice =(start:end:step)
#start is the first element that needs to be includded in your listt and end is the first element that needs to be excluded in a list"
#step is just an itterator always starts with 1

#so we are getting java alone in this print statement print(restraurants[1:2])  becuase our first element is in index 1 and the first element to be excluded in the list is in index 2.
# 
# so to get both java and mint and salt, we will write [1:3] so as to exclude the item in the 3 index and pics elements in index 1 and 2
# 



county = ["nakuru", "mombasa",  "kisii", "busia"]

print(county[0:2])

#desctructive methods

#append (adds items to a list)
#pop remmoves the last item from the list
#remove(removes specified items)
#del(deletes the list)
#clear(removes items in a array)
#len(shows no of items in a list)
#set(checks for unique values in a list)    


county.append("Eldoret")
county.append("nakuru")

county = set(county)

county = county.pop()



print(len(county))

#set(removes duplicates from a list and also arranges items in inorder)
#to find difference in new list items  after doing the method set()

#len(originlist) - len(presentlist)