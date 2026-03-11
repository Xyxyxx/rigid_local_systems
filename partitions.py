def make_partitions(n):
    if n == 0:
        return [[0]]
    if n == 1:
        return [[1]]

    partitions_of_n = [[n]]
    for i in range(1, n):
        if i <= n - i:
            temp2 = make_partitions(n - i)
            for a in temp2:
                partitions_of_n.append([i] + a)

    return partitions_of_n

def test():
    for i in range(10):
        part = make_partitions(i)
        for p in part:
            if sum(p) != i:
                return False

    return True

if __name__ == "__main__":
    if test():
        print("All tests passed")

