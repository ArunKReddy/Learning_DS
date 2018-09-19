# Syntax of Python Dictionaries
Dict = {'Akruthi': 3,'Aishu':28,'Arun':34}
print(Dict['Akruthi'])

# Copying from one dictionaries to another
Dict = {'Sunil': 18,'Chidu':12,'reddy':22,'Appu':25,'SB':30}
Boys = {'Sunil': 18,'Chidu':12,'reddy':22,'Appu':25}
Girls = {'SB':30}
studentXX = Boys.copy()
studentXXX = Girls.copy()

print(studentXX)
print(studentXXX)

studentXXX.update({'JB':35})
print(studentXXX)
print(Dict)

del Dict['Sunil']
print(Dict)
print(studentXX)

# Sorting using Dictionaries

Dict = {'Sunil': 18,'Chidu':12,'reddy':22,'Appu':25,'SB':30}
Students = list(Dict.keys())
Students.sort()
for S in Students:
    print(":".join((S,str(Dict[S]))))

# Data Type of the dictionaries
print(type(Dict))


