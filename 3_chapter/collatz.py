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
number = int(input('Enter an integer equal or plus to 1: '))

while objective != collatz(number):
    number = int(input('Enter a different integer equal or plus to 1: '))
