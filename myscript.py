# file: myscript.py

def square(x):
    """Square number"""
    return x ** 2


for N in range(2, 6):
    print(N, "squared is", square(N))
