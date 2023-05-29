#variables(variables stores a value)

my_variable='Welcome to my game' 
print(my_variable)

#input(input promts a user to enter a value)

name=input('What is your name?')
print(name)

#converting variables(strings works with string, integers work with intergers:you cannot directly perform operations between strings and integers)

num=int(input('Enter a number')) 
num *=4
print(num)

#if and else statements(if and else are control flow statements in Python that allow you to specify different actions to be performed depending on whether a condition is True or False)

like=input('do you like chocolate?')
if like=='yes':
    print('lets be friends')
else:
    print('you are still  my friend')

#lists(a list is a collection of ordered, mutable elements. This means that once a list is created, its elements can be modified.)
    
questions=['where are you from?','what is your favorite movie?','What is your biggest fear?','What is your favorite color?']
answers=[]

#For loops

for question in questions:
    answer = input(question + ' ')
    answers.append(answer)

print(answers)

#functions

def myfunc():
    print('thanks for playing my game')

myfunc()

#Others

#While loops(a while loop is used to execute a set of statements as long as a condition is true.)

like=input('do you like chocolate?')
while like=='yes':
    print('we are friends!')

#tuples(a tuple is a collection of ordered, immutable elements. This means that once a tuple is created, its elements cannot be modified.)

my_answers = ('Joy', 'Four', 'Yes','Kenya','GirlsTrip','Spiders','Black')
for answer in my_answers:
   print(answer)

#dictionaries(a dictionary is a collection of key-value pairs. Each key in a dictionary is unique and is used to access the corresponding value.they mutable)

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1']) # prints 'value1'
my_dict['key3'] = 'value3'
print(my_dict) # prints {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}  



    



