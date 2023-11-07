def mask_credit_card(card_number):
    visible_digits = card_number[:2] + '*' * 12 + card_number[-4:]
    return visible_digits

import credit_card

card_number = "5290312400019022"
masked_card = credit_card.mask_credit_card(card_number)

print(f'f("{card_number}") returns "{masked_card}"')
