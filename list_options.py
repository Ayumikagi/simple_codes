import textwrap

numbers = [5, 10, 15, 20, 25]
backup = []

while True:
    print(f'Current values in the list {numbers}')
    choice = input('What would you like to do? (Help for help, obviously): ').upper()
    if choice == 'HELP':
        print(textwrap.dedent('''
        Available commands (not case sensitive):
        1. Add      5. Backup
        2. Remove   6. Quit
        3. Check
        4. Sort
        '''))
    elif choice == 'ADD':
        while True:
            choice = input('Would you like to add at (pos) or (end)?: ').upper()
            if choice == 'END':
                while True:
                    edit = input('Enter a value to insert: ')
                    try:
                        edit = int(edit)
                        numbers.append(edit)
                        break
                    except ValueError:
                        print(f'"{edit}" is not a valid input!')
                break
            elif choice == 'POS':
                while True:
                    edit = input('Ensert a value to insert: ')
                    try:
                        edit = int(edit)
                        break
                    except ValueError:
                        print(f'"{edit}" is not a valid input!')
                while True:
                    pos = input(f'Insert "{edit}" what positon?: ')
                    try:
                        pos = int(pos)
                        break
                    except ValueError:
                        print(f'"{pos}" is not a valid input!')
                numbers.insert(pos, edit)
                break         
            else:
                print(f'"{choice}" is not a valid input!')
    elif choice == 'REMOVE':
        while True:
            choice = input('Remove: one, duplicates, all or last?: ').upper()

            if choice == 'ONE':
                while True:
                    edit = input('What value to remove?: ')
                    try:
                        edit = int(edit)
                    except ValueError:
                        print(f'"{edit}" is not a valid input!')
                    if edit not in numbers:
                        print(f'"{edit}" not present in the list!')
                        pass
                    else:
                        numbers.remove(edit)
                        break
                break
            elif choice in ('DUPLICATES, DUPLICATE, DUPE, D'):
                uniques = []
                for number in numbers:
                    if number not in uniques:
                        uniques.append(number)
                    numbers = uniques
                break
            elif choice == 'ALL':
                while True:
                    choice = input('Are you sure you want to remove ALL values?(Y/N): ').upper()
                    if choice in ('YES', 'Y'):
                        numbers.clear()
                        break
                    elif choice in ('NO', 'N'):
                        print('Removal cancelled.')
                        break
                    else:
                        print(f'"{choice}" is not a valid input!')
                break
            elif choice == 'LAST':
                while True:
                    choice = input('Are you sure you want to remove the last value in the list?(Y/N): ').upper()
                    if choice in ('YES', 'Y'):
                        numbers.pop()
                        break
                    elif choice in ('NO', 'N'):
                        print('Removal cancelled.')
                        break
                    else:
                        print(f'"{choice}" is not a valid input!')
                break
            else:
                print(f'"{choice}" is not a valid input!')
    elif choice == 'CHECK':
        while True:
            choice = input('What would you like to check?(val.pos, val.count): ').upper()

            if choice == 'VAL.POS':
                while True:
                    choice = input('Find what value?: ')
                    try:
                        choice = int(choice)
                    except ValueError:
                        print(f'"{choice}" is not a valid input!')
                    if choice not in numbers:
                        print(f'Value "{choice}" not found in the list.')
                    else:
                        print(f'Value "{choice}" found at position [{numbers.index(choice)}]')
                        break
                break
            elif choice == 'VAL.COUNT':
                while True:
                    choice = input('What value you wish to count?: ')
                    try:
                        choice = int(choice)
                    except ValueError:
                        print(f'"{choice}" is not a valid input!')
                    if choice not in numbers:
                        print(f'Value "{choice}" not found in the list.')
                    else:
                        print(f'Value "{choice}" found {numbers.count(choice)} time(s).')
            else:
                print(f'"{choice}" is not a valid input!')
    elif choice == 'SORT':
        while True:
            choice = input('(A)scending or (D)escending sort?: ').upper()
        
            if choice == 'A':
                numbers.sort()
                print('Values sorted.')
                break
            elif choice == 'D':
                numbers.reverse()
                print('Values sorted.')
                break
            else:
                print(f'"{choice}" is not a valid input!')
    elif choice == 'BACKUP':
        while True:
            choice = input('Would you like to make a (B)ackup or (R)estore the list from it?: ').upper()

            if choice == 'B':
                backup = numbers.copy()
                print(f'{backup} stored into backup.')
                break
            elif choice == 'R':
                if backup == []:
                    print('No backup available.')
                    break
                else:
                    numbers = backup.copy()
                    print(f'{backup} restored.')
                    break
            else:
                print(f'"{choice}" is not a valid input!')
    elif choice == 'QUIT':
        input('Bye! Press any key to exit.')
        exit()
    else:
        print(f'"{choice}" is not a valid input!')
