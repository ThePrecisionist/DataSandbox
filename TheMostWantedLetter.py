def checkio(input):
    #Declare some variables
    Char_Dict = {}
    max = 0
    this_one = ''

    #Sort out the given text
    text =  sorted(input.lower().strip('1234567890!?.,@#$%^&*()').replace(" ","").replace("-",""))

    #Populate the dictionary
    for ch in text:
        if Char_Dict:
            if ch in Char_Dict:
                Char_Dict[ch] += 1
            else:
                Char_Dict.update({ch:1})
        else:
            Char_Dict.update({ch: 1})

    #Find the most common Char
    for key, value in Char_Dict.items():
        if max < value:
            max = value
            this_one = key

    return (this_one)

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")