"""Python Program that converts a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters"""
def convert(word):
    count_capital = 0
    for char in range(len(word)):
        if word[char].isupper():
            count_capital += 1
        if char == 3 and count_capital == 2:
            print(word.upper())
            break     
    print(f"Found {count_capital} capital letter not within the range of the first four characters")
        
if __name__=='__main__':
    string = 'SolomOn'
    convert(string)