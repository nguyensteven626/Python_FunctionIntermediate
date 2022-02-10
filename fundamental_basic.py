x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30

def iterateDictionary(students):
    for student in range(len(students)):
    print(f"first_name-: {students[student]['first_name']},", f"last_name-: {students[student]['last_name']}")

iterateDictionary(students)

def iterateDictionary2(key_name, name_list):
    #looping through the length of name_list
	for i in range(len(name_list)):
		print(f"{students[i][key_name]}")

iterateDictionary2('first_name',students)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, val in some_dict.items():
        print(f'{len(val)} {key.upper()}')
        for elements in val:
            print(elements)

printInfo(dojo)
