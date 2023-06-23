# Function to perform the search in the metro tree
def search_subsegment(metro, u, v, k):
    weight_sum = 0
    for station in range(u, v+1):
        weight_sum += metro[station]
        if weight_sum == k:
            return True
    return False

# Read the number of test cases
t = int(input())

# Iterate over the test cases
for _ in range(t):
    # Read the number of events n
    n = int(input())

    # Create a data structure to represent the metro tree
    metro = {1: 1}  # Initialize the tree with a single station with number 1 and weight x=1

    # Iterate over the events
    for _ in range(n):
        event = input().split()
        event_type = event[0]

        if event_type == "+":
            # Add a new station with weight xi to the station with number vi+1
            vi = int(event[1])
            xi = int(event[2])
            metro[vi + 1] = xi

        elif event_type == "?":
            # Perform a search in the tree from station 1 to station vi
            vi = int(event[1])
            ki = int(event[2])

            # Perform the search for the subsegment
            subsegment_exists = search_subsegment(metro, 1, vi, ki)

            # Print the result
            if subsegment_exists:
                print("YES")
            else:
                print("NO")

