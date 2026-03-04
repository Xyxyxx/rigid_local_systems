'''
Some code to figure out what numerical combinations are possible
for rank 3 rigid local systems
'''
# z_i = dim Z(A_i)
# need sum(z_i for i from 1 to s) = (s-2)n^2 + 2

from itertools import product

def list_rigid_dims(s, n, possible):

    combinations = list(product(possible, repeat = s))

    for i in range(len(combinations)):
        combinations[i] = list(combinations[i])
        combinations[i].sort()
        combinations[i] = tuple(combinations[i])

    combinations = set(combinations)

    num_criterion = (s-2) * n * n + 2
    
    answers = []
    for c in combinations:
        if sum(c) == num_criterion:
            answers.append(c)

    #print(answers)
    return answers

def print_acceptable_tuples(above, n, possible):
    for s in range(3, above):
        dims = list_rigid_dims(s,n, possible)
        print(dims)
        print("s=", s, "len = ", len(dims))

    return

def main():
    print("Rank 3:")

    possible_rank3 = [3,5,9]
    for s in range(3, 10):
        print(list_rigid_dims(s, 3, possible_rank3))

    print("Rank 2:")

    possible_rank2 = [4,2]
    for s in range(3,10):
        print(list_rigid_dims(s,2, possible_rank2))

    print("Rank 4:")
    possible_rank4 = [4,6,8,10,16]
    for s in range(3,10):
        dims = list_rigid_dims(s,4,possible_rank4)
        print(dims)
        print("s =", s, "len =", len(dims))

    print('Rank 5:')

    possible_rank5 = [5,7,9,11,13,25]
    for s in range(3,10):
        dims = list_rigid_dims(s, 5, possible_rank5)
        print(dims)
        print("s=", s, "len = ", len(dims))

    # now we restrict to semisimple systems
    # which should be ok because these are dense
    # and we can have flat families go to the non-s.s. cases
    '''possible_rank6 = [6,8,10,12,14,18,20,26,36]
    print_acceptable_tuples(10, 6, possible_rank6)'''

if __name__ == "__main__":
    main()
