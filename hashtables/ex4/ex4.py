def has_negatives(a):
    cache = {}
    """
    YOUR CODE HERE
    """
    result = []
    for i in a:
        if -i in cache:
            result.append(i if i >= 0 else -i)
        cache[i] = 1
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
