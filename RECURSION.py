def print_rev(n):
    if n == 0:
        return
    print(n)
    print_rev(n - 1)
print_rev(9)