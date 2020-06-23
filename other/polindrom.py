def polindrom(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return polindrom(word[1:-1])

print(polindrom("шалаш"))

