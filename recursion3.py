def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
print(count_digits(45678))