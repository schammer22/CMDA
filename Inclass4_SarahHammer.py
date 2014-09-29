#Sarah Hammer
#CMDA 3654

#Inclass4 Part 2

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#prints "I will now count my chickens"
print "I will now count my chickens:"

#prints "Hens" then the integer value 25+30/6 (=30)
print "Hens", 25 + 30 / 6

#prints "Roosters" then the integer value 100-25*3%4 (=97)
print "Roosters", 100 - 25 * 3 % 4

#prints "Now I will count the eggs:"
print "Now I will count the eggs:"

#prints the value of the integer operations below (=7)
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

#prints "Is it true that 3 + 2 < 5 - 7?"
print "Is it true that 3 + 2 < 5 - 7?"

#prints FALSE, because 3 + 2 (=5) is not less than 5 -7 (= -2)
print 3 + 2 < 5 - 7

#prints "What is 3 + 2?" then the integer value 3 + 2 (=5)
print "What is 3 + 2?", 3 + 2

#prints "What is 5 - 7?" then the integer value 5 - 7 (=-2)
print "What is 5 - 7?", 5 - 7

#prints "Oh, that's why it's False."
print "Oh, that's why it's False."

#prints "How about some more."
print "How about some more."

#prints "Is it greater?", then TRUE because 5 > -2
print "Is it greater?", 5 > -2
#prints "Is it greater or equal?", then TRUE because 5 >= -2
print "Is it greater or equal?", 5 >= -2
#prints "Is it less or equal?", then FALSE because 5 is not >= -2
print "Is it less or equal?", 5 <= -2

#PART II
#assigns the variable days to string "Mon Tue Wed Thu Fri Sat Sun"
days = "Mon Tue Wed Thu Fri Sat Sun"
#assigns the variable months to string "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#prints "Here are the days: " and the string variable days (assigned above)
print "Here are the days: ", days
#prints "Here are the months: " and the string variable months (assigned above)
#each month is on a different line
print "Here are the months: ", months

#PART III
# assigns the variable the_count to the list of integers 1,2,3,4,5
the_count = [1, 2, 3, 4, 5]
# assigns the variable fruits to the list of strings 'apples','oranges','pears','apricots'
fruits = ['apples', 'oranges', 'pears', 'apricots']
#assigns the variable change to the list of integers and strings 1, 'pennies', 2, 'dimes', 3, 'quarters'
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# prints "This is count" then the integer for every integer
# assigned to the_count
for number in the_count:
    print "This is count %d" % number

# prints "A fruit of type" then the string for every string
# assigned to the variable fruits
for fruit in fruits:
    print "A fruit of type: %s" % fruit


# Use %r format when you don't know
#if the elements are strings or integers

#prints "I got" for every integer/string defined in 
# variable change
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts

#prints "Adding" then the values 0-5 then "to the list"
# each on separate line
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# prints values for all elements
for i in elements:
    print "Element was: %d" % i
    
    
#Inclass4 Part 3

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#Use the code from Lecture14.py to create and change the 
#'stuff' list; Then comment on each line of the code below
#what it does, and what the result is

#creates 'stuff' list
ten_things = "Apples Oranges Crows Telephone Light Sugar"
stuff = ten_things.split(' ')

#prints first element of list 'stuff'
print stuff[1]
#prints last element of list 'stuff'
print stuff[-1] 
#prints last element of list 'stuff'
print stuff.pop()
#prints first 5 elements of stuff separated by a space
print ' '.join(stuff) 
#prints 4th and 5th elements separated by a '#'
print '#'.join(stuff[3:5]) 

#PART II

#Create comments where marked with # to explain the code below

# creates dictionary with states as keys and abbreviations as values
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# creates dictionary with abbreviated states as keys and cities
#  that correspond with those states
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# adds NY and OR and their values (cities)
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# prints a border with 10 dashes
print '-' * 10
#prints 'NY state has:' then calls the value for key NY
print "NY State has: ", cities['NY']
#prints 'OR State has:' then calls the value for key OR
print "OR State has: ", cities['OR']

# prints 10 dashes
print '-' * 10
# prints 'Michigan's abbreviation is:' then calls value
# for key Michigan using states dictionary
print "Michigan's abbreviation is: ", states['Michigan']
# prints 'Florida's abbreviation is:' then calls value
# for key Florida using states dictionary
print "Florida's abbreviation is: ", states['Florida']

# prints 10 dashes
print '-' * 10
#prints 'Michigan has:' then uses both dictionaries to call values
print "Michigan has: ", cities[states['Michigan']]
# prints 'Florida has:' then uses both dictionaries to call values
print "Florida has: ", cities[states['Florida']]

# prints 10 dashes
print '-' * 10

#prints all states in dictionary states, and their abbreviations
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

#prints 10 dashes
print '-' * 10
# prints all state abbreviations in cities dictionary and the city belonging to those states
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# prints 10 dashes
print '-' * 10
# prints all states in states dictionary
# then prints their abbreviations and the city belonging to those states
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])


