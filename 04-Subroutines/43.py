def acronym(name):
    words = name.split()
    return ''.join(word[0].upper() for word in words)
