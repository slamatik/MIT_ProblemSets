###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time


# ================================
# Part A: Transporting Space Cows
# ================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    with open(filename) as f:
        data = f.readlines()
        data = [i.strip().split(',') for i in data]
        return {key: int(val) for key, val in data}


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows = {key: val for key, val in sorted(cows.items(), key=lambda item: item[1], reverse=True)}
    data = cows.copy()
    solution = []
    while data:
        trip = []
        trip_value = 0
        for key, val in cows.items():
            if trip_value + val <= limit and key in data:
                trip.append(key)
                trip_value += val
                data.pop(key)
        solution.append(trip)
    return solution


# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    data = []
    for partition in get_partitions(cows):
        trip = []
        for cow_list in partition:
            trip_value = 0
            for cow_name in cow_list:
                trip_value += cows[cow_name]
            if trip_value <= limit:
                trip.append(1)
            else:
                trip.append(0)

        if sum(trip) == len(partition):
            data.append(partition)
    data = sorted(data, key=len)
    return data[0]


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows('ps1_cow_data.txt')
    t0 = time.time()
    print('Greedy')
    print('\tNumber of trips:', len(greedy_cow_transport(cows)))
    print('\tTime Taken:', time.time() - t0, 'seconds')

    t1 = time.time()
    print('Brute Force')
    print('\tNumber of trips:', len(brute_force_cow_transport(cows)))
    print('\tTime Taken:', time.time() - t1, 'seconds')


compare_cow_transport_algorithms()
