#NUMBERS
varium = 123
pi = 3.141

#STRINGS
varString = "Hello World!"
varText = "This is a string"

#LIST
varlist = ["abc", 123]

#TUPLE
varTuple = {'abc', 123, 'HELLO'}

#DICTIONARY
var = 3
varDict ={'first': 1 , '2':'2nd' , 3:var}

varDict = {}
varDict['first'] = 1
varDict['2'] = '2nd'
varDict[3] = var


#ADDITION
a = 5 + 3
print (a)

#SUBTRACTION
a = 5 - 3
print (a)

#MULTIPLICATION
a = 5 * 3
print (a)

#EXPONENT
a = 5 ** 3
print (a)

#DIVISION
a = 5 / 3
print (a)

a = 5 % 3
print (a)

a = 5 // 3

#INCREMENT
a = 5
a += 1
print (a)

#DECREMENT
a = 5
a -= 1
print (a)

#STRING CONCATENATION
a = 'HELLO ' + 'WORLD'
print(a)

#COMPLEX EXPRESSIONS
a = 3 + 5 - 6 * 2 / 4
print (a)

print('\n')

#BOOLEAN CONDITIONS
x = True

if x:
    print("var x is True")
else:
    print("var x is False")
    
#STRING CONDITIONS
x = "HELLO WORLD!"

if x == 'Hello World!':
    print("var is x Hello World!")
else:
    print("var x is not Hello World!")
    
#NUMERICAL CONDITIONS
x = 10

if x == '10':
    print("var x is a string")
elif x == 10:
    print("var x is an integer")
else:
    print("var x is none of the abover")
    
print('\n')    
    
# FOR LOOPS
for var in range(0, 5, 2):
    print(var)

#WHILE LOOPS
var = 0
while var < 5:
    print(var)
    var += 2

#NESTED LOOPS
x = 0
while x < 5:
    for y in range(0, x):
        print(y, end=' ')
    x += 1
    print()

print('\n')

#LISTS
pi = 3.14159
varList = [ 1, 2, 'A', 'B', 'Hello!', pi]
print(varList[0])

print(varList[4])

varList.append('World!')
print(varList[6])

print(len(varList))

print(varList[5])

varList.remove(pi)
print(varList[5])

print('\n')

#DICTIONARIES
var = "Hello World!"
varDict = {'first' :  123, 2 : 'abc', '3': var, 4 : ['lista', 'listb']}
print(varDict['first'])
print(varDict[2])
print(varDict['3'])
print(varDict[4])
print(varDict[4][1])
print(len(varDict))

print('\n')

#LIST GENERATORS AND COMPREHENSION
def gen_num_up_to(n):
    num = 0
    while num < n:
        yield num
        num += 1
        
print(gen_num_up_to(5))

varList = gen_num_up_to(5)
print([var for var in varList])

def gen_num_up_to(n):
    num = 0
    while num < n:
        yield num
        num += 2

varList = gen_num_up_to(5)
print([var for var in varList])

varList = range(0, 5, 2)
print([var for var in varList])

print('\n')

#SLICING
varList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(varList[:5])
print(varList[5:])
print(varList[:-2])
print(varList[-2:])
print(varList[2:-2])
print(varList[2:8:2])

print('\n')
#FUNCTIONS
def remainder(n, m):
    while True:
        if n -m < 0:
            return n
        else:
            n = n - m

print(remainder(10, 4))
        
        