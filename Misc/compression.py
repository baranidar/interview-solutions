def compression(s):
    result = ''
    if len(s) == 0:
        return ''
    prev = s[0]
    counter = 0

    for item in s:
        if prev == item:
            counter += 1
        else:
            result = result + prev + str(counter) 
            counter = 1
        prev = item

    result = result + prev + str(counter)
    return result

input = 'TTTTTGGTCCTTTTA'
output = compression(input)
print(output)

#T5G2T1C2T3A1