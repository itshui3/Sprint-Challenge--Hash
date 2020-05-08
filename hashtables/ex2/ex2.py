#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    """
    YOUR CODE HERE
    """
    # Representing each ticket in response arr with the string value of it's destination
    route = []
    for i in tickets:
        cache[i.source] = i.destination
    pointer = cache['NONE']
    while len(route) < length:
        route.append(pointer)
        pointer = cache[pointer]
    return route
