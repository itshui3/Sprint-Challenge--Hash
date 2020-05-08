def get_indices_of_item_weights(weights, length, limit):
    if length < 2:
        return None
    cache = {}
    """
    YOUR CODE HERE
    """
    for index, item in enumerate(weights):
        if limit - item in cache:
            #Found the pair
            if index > cache[limit - item]:
                return (index, cache[limit-item])
            else:
                return (cache[limit-item], index)
        else:
            #No pair
            cache[item] = index
