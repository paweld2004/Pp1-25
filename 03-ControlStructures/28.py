ean_13 = input('Enter EAN-13 article number: ')

if len(ean_13) == 13 and ean_13.startswith('590'):
    print('Article number is correct')
    print('Article manufactured in Poland')
