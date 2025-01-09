#https://www.geeksforgeeks.org/multiprocessing-python-set-1/
import multiprocessing
import os

def calculate_area_square(a):
    print(f"Calculated Area is {a*a}")

def calulate_perimeter_square(a):
    print(f"Calculated Permimeter is {4*a}")


if __name__ == "__main__":
    print(f"Process id of main program: {os.getpid()}")
    p1 = multiprocessing.Process(target=calculate_area_square, args=(5,))
    p2 = multiprocessing.Process(target=calulate_perimeter_square, args=(5,))

    p1.start()
    p2.start()
    print(f"Process id of p1 sub-program: {p1.pid}")
    print(f"Process id of p2 sub-program: {p2.pid}")
    print(f"Is p1 sub-program alive?: {p1.is_alive()}")
    print(f"Is p2 sub-program alive?: {p2.is_alive()}")
    p1.join()
    p2.join()
    print(f"Is p1 sub-program alive?: {p1.is_alive()}")
    print(f"Is p2 sub-program alive?: {p2.is_alive()}")
    print("Multiprocessing completed!!!")