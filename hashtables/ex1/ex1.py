def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create a dictionary
    storage = dict()

    # Loop through the range of length
    for i in range(length):
        current_weight = weights[i]
        total = (limit - current_weight)

        # See if the total is in the dictionary
        # then return a tuple of the current index and the total index
        # otherwise set the current weight key to the current index
        if total in storage:
            total_index = storage[total]

            return (i , total_index)
        else:
            storage[current_weight] = i

    # return none if the pair doesn't exist for the 
    # given inputs
    return None

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))