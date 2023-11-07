credit_card_number = input('Enter credit card number: ')

formatted_credit_card_number = ' '.join([credit_card_number[i:i+4] for i in range(0, len(credit_card_number), 4)])

print(f'Card number: {formatted_credit_card_number}')
