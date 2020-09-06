# from __future__ import print_function
# for i in range(1, 5):
#     for j in range(1, 10):
#         print(j, end='')
#         if i > 1:
#             print('.', end='')
#             for k in range(1, i):
#                 print(j, end='')
#         print(' ', end='')
#     print('\n')

# a = [1, 2, 3, 4]
# b= a[::-1]
#
# b[0] = 100
#
# print(a)
# print(b)


# a, b, c = (1, 2, 'Reshma')
# print(c.split())

# a = ('a', 'z', 'k')
#
# del a[2]

# person = {
#     "name": "Ganesh",
#     "age": 33
# }
#
# print(person.items())

# addNumbers = lambda num1, num2: num1 + num2
#
# print(addNumbers(1, 2))

# a= {
#     "name": "Ganesh"
# }
#
# b = a.copy()
# print(b is a)

# from datetime import date
#
# print(date.today())

# import time
#
# print(time.localtime())

import time


class User:
    def __init__(self, firstname, lastname):
        self.fName = firstname
        self.lName = lastname

    def greet(self, timeOfTheDay):
        print('Hello {0} {1}, Good {2}!'.format(self.fName, self.lName, timeOfTheDay))


class Customer(User):
    def __init__(self, fName, lName, projectName):
        self.fName = fName
        self.lName = lName
        self.project = projectName

    def sayHello(self):
        print('Hello {0}, {1}. Thanks for your {2} project.'.format(self.fName, self.lName, self.project))


brett = Customer('Brett', 'Cohen', 'TicTac Shake 2.0')
brett.sayHello()





