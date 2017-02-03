import re

# has 8 or more characters
length = re.compile(r'[a-zA-Z0-9]{8,}')

# contains upper a lower case
upper = re.compile(r'[A-Z]')
lower = re.compile(r'[a-z]')

# contains at least 1 number
number = re.compile(r'[0-9]')


def isStrong(password):
    return length.search(password) and upper.search(password) and \
           lower.search(password) and number.search(password)

message = 'Enter a new password: '
password = input(message)
while not isStrong(password):
    print('Password not strong, It should have 8 or more characters ' +
          'including both uppercase and lowercase characters plus  number')

    password = input(message)
