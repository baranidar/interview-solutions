# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
    def reverse(self, x: int) -> int:
        x = str(x)[::-1] if x > 0 else "-"+str(x).strip("-")[::-1]
        x = x.lstrip("0") 
        print(x)
        return int(x) if int(x) > -2**31 and int(x) < 2**31 - 1 else 0
