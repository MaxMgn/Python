n = input()
list = []
def fib (n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if (n > 1):
        return fib (n-2) + fib (n-1)
    if (n < 0):
        return fib (n+2) - fib (n+1)
print (fib (n))

for i in range (-n, n+1):
    list.append (fib (i))
print (list)