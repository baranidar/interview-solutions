def digit_accumulator(s):
    float_string = list(s)
    sum = 0
    for i in float_string:
        if i != '.':
            sum += int(i)
    print(sum)
    
digit_accumulator("789.4321")
