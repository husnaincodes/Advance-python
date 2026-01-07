def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
print(double(5))
