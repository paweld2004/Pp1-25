def is_palindrome(palindrome):
    cleaned_palindrome = ''.join(filter(str.isalnum, palindrome)).lower()
    return cleaned_palindrome == cleaned_palindrome[::-1]
