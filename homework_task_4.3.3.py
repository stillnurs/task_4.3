with open ('homework_task_4.3.3.txt', 'a') as guest_book:

    while True:
        guest = input('Please enter your full name: ')
        guest_book.write('Welcome, ')
        guest_book.write(guest + '\n')
        if guest != 'end':
            guest
        else:
            print('All guests were added to guest book.')

            break

with open ('homework_task_4.3.3.txt') as guest_book:
    line = guest_book.read()
print(line)