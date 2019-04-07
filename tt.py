start = input('Please enter the multiplicaton table you would like to generate the product(s) for: ')
stop = input('Please enter what number you want to stop generaton at: ')

for iterator in range(stop + 1):
    print (str(start) + ' * ' + str(iterator) + ' = ' + str(start * iterator))