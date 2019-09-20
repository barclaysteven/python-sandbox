# Example: abc
# result: [ 'abc', 'acb', 'bac', 'bca', 'cab', 'cba' ]


def permutation_recursive(my_string):
    permutations = []

    if my_string is None or len(my_string) == 0:
        return permutations

    for char in range(len(my_string)):
        prefix = my_string[char]
        remainder = my_string[:char] + my_string[char + 1:]
        subperms = permutation_recursive(remainder)

        if not subperms:
            permutations.append(prefix)

        else:
            for subperm in subperms:
                permutations.append(prefix + subperm)

    return permutations


print(permutation_recursive("abc"))
