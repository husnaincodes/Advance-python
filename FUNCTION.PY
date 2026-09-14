numbers = list(map(int,input("Enter numbers separated by space: ").split(   )))

def even_odd_count(numbers,index=0,even_count=0,odd_count=0):
    if index == len(numbers):
        return even_count, odd_count
    if numbers[index] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    return even_odd_count(numbers, index + 1, even_count, odd_count)


even_count, odd_count = even_odd_count(numbers)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)