import itertools
cube_permutations = {}

for i in itertools.count(1):
    cube = i**3
    cube_digits = str(sorted(str(cube)))
    if cube_digits in cube_permutations:
        cube_permutations[cube_digits][1] += 1
        if cube_permutations[cube_digits][1] == 5:
            print cube_permutations[cube_digits][0]
            break
    else:
        cube_permutations[cube_digits] = [cube, 1]

