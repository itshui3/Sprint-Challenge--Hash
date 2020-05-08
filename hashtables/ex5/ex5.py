def finder(files, queries):
    cache = {}
    """
    YOUR CODE HERE
    """
    for i in files:
        filename = i.split('/')[-1]
        if filename not in cache:
            cache[filename] = []
        
        cache[filename].append(i)

    result = []

    for i in queries:
        if i in cache:
            for l in cache[i]:
                result.append(l)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
