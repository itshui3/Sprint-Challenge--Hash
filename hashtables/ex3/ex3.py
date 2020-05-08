def intersection(arrays):
    cache = {}
    """
    YOUR CODE HERE
    """
    shortest = None
    result = []
    for arr in arrays: # might need index access

        if shortest == None or len(arr) < len(shortest):
            shortest = arr

        for i in arr:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1

            if cache[i] == len(arrays):
                result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
