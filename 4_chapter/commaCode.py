def commaCode(value):
    """
    in: list containing integers, floats, strings, lists
    out: string separated by comma and space, with and
    inserted before the last item.
    """
    result = ''
    for index in range(len(value)):
        if index == len(value) - 1:
            result += 'and ' + str(value[index])
        else:
            result += str(value[index]) + ', '
    return result

spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaCode(spam))
