#https://leetcode.com/problems/robot-bounded-in-circle/description/
def isRobotBounded(self, instructions: str) -> bool:
    x = 0
    y = 0
    current_direction = (0,1)
    for item in instructions:
        if item == 'G':
            x = x + current_direction[0]
            y = y + current_direction[1]
        elif item  == 'L':
            current_direction = (-current_direction[1],current_direction[0])  
        else:
            current_direction = (current_direction[1],-current_direction[0])
    print(x,y, current_direction)
    return (x == 0 and y == 0) or current_direction != (0,1)
