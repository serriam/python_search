from data import *

# students = data

# search_query = input('Search a student by typing a letter: ')
# result = []

# for a in students:
#     if a.lower().startswith(search_query.lower()):
#         result.append(a)

# if result:
#     print('Found students:')
#     for r in result:
#         print(r)
# else:
#     print('No students found matching query:', result)

students = data

def search_students(query):
    result = []
    for a in students:
        if a.lower().startswith(query.lower()):
            result.append(a)
    return result

search_term = input("search student by typing first letter: ")

print( "search term returned: ",search_students(search_term))