"""
1. update values in dicitonaries and lists 

*remember, is the brackets or the parenthesis inside a list or dictionary or tuples. 
"""



#TODO:  Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#! this is a list inside a list

x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15 #its a list, so, [5,2,3] is array 0 and [10,8,9] array 0  [10,8,9] = 10 is value #0
print(x)


#TODO: Change the last_name of the first student from 'Jordan' to 'Bryant'
#! this is a dictionary inside a list
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}

]

students[0]['last_name'] = 'Bryant'
print(students)



#TODO: In the sports_directory, change 'Messi' to 'Andres'
#! this is a dictionary, the value inside the dictionary are list. 
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

#TODO: Change the value 20 in z to 30
z = [ {'x': 10, 'y':20}]

z[0]['y'] = 30
print(z)


************************************************************************************************************************
"""
#2. iterate through a list of dictionaries 
"""

#TODO: Create a function iterateDictionary(some_list) that, given a list of ditionaries, 
#TODO: the fucntion loops through each dictionary in the list and prints each key and the associated value.
#TODO: For example, give the following list:


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#! building this function to work on multiple things
def iterate_Dictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key, val in list[i].items():
            output += f" {key} - {val},"
        print(output)

iterate_Dictionary(students)
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel

"""
3. get values from a list of dictionaries
"""

#TODO: Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
#TODO:  the function prints the value stored in that key for each dictionary. 
#TODO:  For example, iterateDictionary2('first_name', students) should output:



students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary2(key_name, list):
    for i in range(0, len(list)):
        for key, val in list[i].items():
            if key == key_name:
                print(val)
iterate_dictionary2('first_name',students)
iterate_dictionary2('last_name',students)


"""
output:
Michael
John 
Mark
KB

output:
Jordan
Rosales
Guillen
Tonel
"""

"""
4. Iterate Through a Dictionary with List Values
"""
#TODO: Create a function printInfo(some_dict) that given a dictionary whose values are all lists
#TODO: prints the name of each key along with the size of its list
#TODO: then prints the associated values within each key's list

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dict):
    for key,val in dict.items():
        print('-----')
        print(f'{len(val)} {key.upper()}')
        for i in range(0, len(val)):
            print(val[i])

print_info(dojo)


"""
output: 

7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
-----
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon

"""

