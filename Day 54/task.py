import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper():
        before = time.time()
        function()
        return time.time() - before

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


print("fast_function run speed: " + str(fast_function()))

print("slow_function run speed: " + str(slow_function()))