# MAP
ROMAN_TO_DECIMAL = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

# Function to Validate the Roman numeral (Extracted from https://www.geeksforgeeks.org/validating-roman-numerals-using-regular-expression/)
def ValidationOfRomanNumerals(string):
    import re
    # returning the boolean value
    return bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",string))
    # By the way this validation is actually beautiful

# ACTUAL FUNCTION
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


if __name__ == '__main__':
    # I import this inside main because it is not needed outside
    import argparse
    parser = argparse.ArgumentParser(description = 'Insert the roman number you want to translate to Decimal Number.')
    parser.add_argument('roman_number', help='Inserte the roman number.')
    args = parser.parse_args()
    
    # Extra validation
    try: 
        roman_string = args.roman_number.upper()
    except Exception as e:
        print(f"This should not happen. ERROR: {e}")
        

    if ValidationOfRomanNumerals(roman_string):
        print(f"The roman number {roman_string} decodes to {decode(roman_string)}")
    else:
        print("The string is not a valid Roman Number")