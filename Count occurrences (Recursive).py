
def count_occ(lst, target, index=0):
    if index == len(lst):
        return 0
    return (1 if lst[index] == target else 0) + count_occ(lst, target, index + 1)

print(count_occ([1, 2, 1, 3, 1, 4], 1))
