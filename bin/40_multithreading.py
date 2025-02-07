"""
multithreading: One process split into multiple pieces -> each piece is called thread
    library: threading
    In python, It is NOT PARALLEL
    Interpreter will execute only one thread at a time

Then what is the use of multithreading?
- If some thread is waiting for some resource then
    during that waiting time, interpreter will execute another thread.

So, Finally, in multithreading we are making of waiting time.

multiprocessing: multiple processess
    library name: multiprocessing
    It is completely PARALLEL
"""

print("WITHOUT using multithreading")
print("-"*20)
# ---------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)

def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40]

my_square_function(L)
my_cube_function(L)

end_time = time.time()

print("Time taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
###########################

print("USING multithreading")
print("-"*20)
# ---------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)

def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40]

from threading import Thread

thread_1 = Thread(target=my_square_function, args=(L,))
thread_2 = Thread(target=my_cube_function, args=(L,))

# Start the thread
thread_1.start()
# start() will not wait for thread_1 to complete
# After calling start(), it will go to next line
thread_2.start()

# Manually making each thread to wait for its completion
thread_1.join()
thread_2.join()

end_time = time.time()

print("Time taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
###########################

print("WITH DELAY: WITHOUT using multithreading")
print("-"*20)
# ---------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)

def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40]

my_square_function(L)
my_cube_function(L)

end_time = time.time()

print("Time taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
###########################

print("WITH DELAY: USING multithreading")
print("-"*20)
# ---------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)

def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40]

from threading import Thread

thread_1 = Thread(target=my_square_function, args=(L,))
thread_2 = Thread(target=my_cube_function, args=(L,))

# Start the thread
thread_1.start()
# start() will not wait for thread_1 to complete
# After calling start(), it will go to next line
thread_2.start()

# Manually making each thread to wait for its completion
thread_1.join()
thread_2.join()

end_time = time.time()

print("Time taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
###########################