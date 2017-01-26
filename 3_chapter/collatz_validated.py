def collatz(number):
    if number % 2 == 0:
        even_op = number // 2
        print(even_op)
        return even_op
    else:
        odd_op = 3 * number + 1
        print(odd_op)
        return odd_op

objective = 1

try:
    number = int(input('Enter an integer equal or plus to 1: '))
except ValueError:
    print('You entered an invalid integer. Try again')

while objective != collatz(number):
    try:
        number = int(input('Enter a different integer equal or plus to 1: '))
    except:
        print('You entered an invalid integer. Try again')
