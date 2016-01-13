
def quicksort(l):
    if not l:
        return l
    else:
        pivot = l[0]
        lower = quicksort([i for i in l[1:] if i < pivot])
        upper = quicksort([i for i in l[1:] if i >= pivot])
        return lower + [pivot] + upper

print quicksort("321")
