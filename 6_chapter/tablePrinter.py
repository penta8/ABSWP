tableData = [['apples', 'oranges','cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    sizes = []
    for row in tableData:
        bigger = 0
        for column in row:
            if len(column) > bigger:
                bigger = len(column)
        sizes.append(bigger)

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            if j < len(tableData) - 1:
                ending = ''
            else:
                ending = '\n'
            print(tableData[j][i].rjust(sizes[j] + 1), end=ending)

printTable(tableData)
