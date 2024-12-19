
def smallest_letter(letters, target):
    target_ascii = ord(target)
    max_ascii = [ord(x) for x in letters]
    print(target_ascii, max_ascii, letters)
    character = letters[0]
    # does not exist
    if max(max_ascii) <= target_ascii:
        character = letters[0]
        return character
    else: # find next highest character
        for index, i in enumerate(max_ascii):
            print(index, i)
            if i > target_ascii:
                character = letters[index]
                print(character)
                return character  
        
letters = ['c', 'f', 'j']
target = 'j'
output = smallest_letter(letters, target)
if output == 'c': 
    print(True)

# letters = ['c', 'f', 'j']
# target = 'c'
# output = smallest_letter(letters, target)
# if output == 'f': 
#     print(True)

# letters = ['c', 'f', 'j']
# target = 'a'
# output = smallest_letter(letters, target)
# if output == 'c': 
#     print(True)



#****************************************************
def smallest_letter(letters, target):
    for i in range(len(letters)):
        if ord(letters[i]) > ord(target):
            return letters[i]  
    return letters[0]
