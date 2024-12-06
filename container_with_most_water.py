# brute-force
height = [1,8,6,2,5,4,8,3,7]
i = 0
j = 1
max_amt = 0
print(height[i], len(height) - 2)
while i <= len(height) - 2:
    print(height[j], len(height) - 1)
    while j <= len(height) - 1:
        wdth = j - i
        hgt = min(height[i], height[j])
        max_amt = wdth * hgt if wdth * hgt > max_amt else max_amt
        print(f"max_amt = {max_amt}")
        j += 1
        print(f"j = {j}")
    j = i + 1
    i += 1
print(max_amt)
