def possible_permutations(array):
    if len(array) == 1:
        return [array]
    permutations = []
    for i in range(len(array)):
        perms = possible_permutations(array[:i] + array[i + 1:])
        for p in perms:
            permutations.append([array[i], *p])
    return (el for el in permutations)
