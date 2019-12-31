# Few examples of List and its operations

projects = ['EVO', 'QTT', 'EBS', 'B4C', 'Mainframe Migration']  # List of project names

print("List of Projects: ", projects)
print("EVO is in the project list?: ", 'EVO' in projects)
print("Number of Projects: ", len(projects))
print("Last item of Projects: ", projects[-1])
print("First item of Projects: ", projects[0])

# This will not include the upper bound, smiler to [0,3) in maths
print("The range item of Projects: ", projects[0:3])

# if no upper bound, then it will go up to the last item of the list
print("The range item of Projects till upper bound: ", projects[2:])

projects.append('NFT')
projects.insert(0, 'Claims')
print("Append and insert at 0th index: ", projects)

projects_1 = ['Digital', 'DL4B', 'BAU']

projects.extend(projects_1)
print("Extended list of projects: ", projects)

projects.remove('DL4B')

print("Removed 'DL4B': ", projects)

popped_value = projects.pop()

print("Remove the last project using pop() method: ", projects)
print("Popped value: ", popped_value)
test = sorted(projects)  # This will not alters the original list of projects

print("Sorted list of projects: ", test)
projects.reverse()
print("Reversed list of projects: ", projects)
projects.sort()  # This alters the original list of projects
print("Sorted list of project by altering the original list: ", projects)

# Tuples are smiler to list, but you can't modify them. Need to use () instead of [].

tuple_1 = ('One', 'Two', 'Three')
tuple_2 = tuple_1
print("Tuple_1 values: ", tuple_1)
print("Tuple_2 values: ", tuple_2)

# Sets, duplications are not allowed. All mathematics sets operation can be performed

a1c_courses = {'Maths', 'Tamil', 'English', 'Comp Sci', 'Physics', 'Chemistry'}
a1b_courses = {'Maths', 'Tamil', 'English', 'Biology', 'Physics', 'Chemistry'}
a2_courses = {'Tamil', 'English', 'Physics', 'Chemistry', 'Botany', 'Zoology'}
art_courses = {'Tamil', 'English', 'History', 'Env. Sci', 'Economics', 'Accountancy'}

print("The common subjects between a1c and a1b: ", a1b_courses.intersection(a1c_courses))
print("All subjects between a1c and a1b: ", a1b_courses.union(a1c_courses))
print("The common subjects between a2_courses and art_courses: ", a2_courses.intersection(art_courses))

# Empty list

empty_list1 = []
empty_list2 = list()
print("Empty list: ", empty_list1)

# Empty tuples

empty_tuple1 = ()
empty_tuple2 = tuple()
print("Empty Tuple: ", empty_tuple1)

# Empty sets

empty_set1 = {}  # This is not the right way to create empty set as this is used for dict
empty_set2 = set()
print("Empty Set: ", empty_set1)

