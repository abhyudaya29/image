def last_digit_of_fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        next_fib = (previous + current) % 10
        previous, current = current, next_fib

    return current


n = 200
print(last_digit_of_fibonacci(n))  
