interested_in_computer_science = input('Are you interested in computer science? (Y/N): ')
like_playing_computer_games = input('Do you like playing computer games? (Y/N): ')
has_instagram_account = input('Do you have an Instagram account? (Y/N): ')

print(f'Interested in computer science: {interested_in_computer_science == "Y" and "Yes" or "No"}')
print(f'Playing computer games: {like_playing_computer_games == "Y" and "Yes" or "No"}')
print(f'Has an Instagram account: {has_instagram_account == "Y" and "Yes" or "No"}')
