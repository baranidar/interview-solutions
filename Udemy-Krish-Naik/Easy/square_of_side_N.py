
def square_of_side_N():
    N = int(input("Enter a value for N: "))
    square_list = []
    for i in range(N):
        square_list.append("*" * N)
    return square_list


print(square_of_side_N())