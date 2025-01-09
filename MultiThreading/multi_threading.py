#https://www.geeksforgeeks.org/multithreading-python-set-1/
import threading
import os

def calculate_area_square(a):
    print(f"Calculated Area is {a*a}")
    print(f"Thread name: {threading.current_thread().name}")
    print(f"Thread id of calculate_area_square: {os.getpid()}")

def calulate_perimeter_square(a):
    print(f"Calculated Permimeter is {4*a}")
    print(f"Thread name: {threading.current_thread().name}")
    print(f"Thread id of calulate_perimeter_square: {os.getpid()}")


if __name__ == "__main__":
    print(f"Process id of main program: {os.getpid()}")
    t1 = threading.Thread(target=calculate_area_square, args=(5,))
    t2 = threading.Thread(target=calulate_perimeter_square, args=(5,))

    t1.start()
    t2.start()

    print(f"Is t1 sub-program alive?: {t1.is_alive()}")
    print(f"Is t2 sub-program alive?: {t2.is_alive()}")
    t1.join()
    t2.join()
    print(f"Is t1 sub-program alive?: {t1.is_alive()}")
    print(f"Is t2 sub-program alive?: {t2.is_alive()}")
    print("MultiThreading completed!!!")