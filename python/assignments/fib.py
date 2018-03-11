import sys

# method to print fibonacci series until N
def fib(n=0):
    if (n==0 or n==1):
        return n
    a, b = 0, 1
    while (b < n):
        print(b)
        a, b = b, b+a

if __name__ == "__main__":
    n = int(sys.argv[1])
    print("Fibonacci series until", n)
    fib(n)
