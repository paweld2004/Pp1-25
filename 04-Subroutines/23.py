def count_letter(text, letter):
    return text.count(letter)

import text_processing

letter = 'e'
count = text_processing.count_letter(text, letter)

print(text)
print(f"The number of letter '{letter}': {count}")
