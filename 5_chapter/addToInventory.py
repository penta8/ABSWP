dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number of items: ' + str(total))

displayInventory(addToInventory(stuff, dragonLoot))
