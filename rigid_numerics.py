'''
Some code to figure out what numerical combinations are possible
for rank 3 rigid local systems
'''
# z_i = dim Z(A_i)
# need sum(z_i for i from 1 to s) = (s-2)n^2 + 2

from itertools import product
import partitions


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

def list_possible_dims(n):
    parts = partitions.make_partitions(n)
    possible = []
    for a in parts:
        sum_of_squares = 0
        for x in a:
            sum_of_squares += x * x
        possible.append(sum_of_squares)
    return possible

def rigid_dims_tester(n):
    print("Rank", n)
    possibles = list_possible_dims(n)
    print("Possible dimensions:", possibles)
    for s in range(3, 10):
        print(list_rigid_dims(s, n, possibles))


def main():

    print("Enter desired rank:")
    n = eval(input())
    rigid_dims_tester(n)


    #rigid_dims_tester(3)


    '''print("Rank 2:")

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
    '''

    # Rank 6 is very nonperformant.
    # Needs some optimizations that I'm too lazy to think about right now
    '''
    # now we restrict to semisimple systems 
    # which should be ok because these are dense
    # and we can have flat families go to the non-s.s. cases
    possible_rank6 = [6,8,10,12,14,18,20,26,36]
    print_acceptable_tuples(10, 6, possible_rank6)'''

if __name__ == "__main__":
    main()
