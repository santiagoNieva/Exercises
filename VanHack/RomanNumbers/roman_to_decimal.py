ROMAN_TO_DECIMAL = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def decode(roman):
    total = 0
    previous = 1001
    for character in roman:
        arabic = ROMAN_TO_DECIMAL[character.upper()]
        if previous < arabic:
            total += arabic - (2*previous)
        else:
            total += arabic
        previous = arabic
    return total