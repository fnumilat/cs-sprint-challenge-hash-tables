def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create dictionaries for positives and negatives
    positives_dict = dict()
    negatives_dict = dict()

    # Create an array to store the results at the end
    result = []

    # Loop through list a
    # and see if item is bigger or equal to 1
    # then set the item in the positives dict
    # to 0 other wise do the same to the 
    # negatives dict
    for item in a:
        if item >= 1:
            positives_dict[item] = 0
        else:
            negatives_dict[item] = 0
    
    # Loop through the keys in the postives dict
    # and see if the key times negative 1 in the negatives dict
    # then add the key into the result array
    for key in positives_dict.keys():
        if key * -1 in negatives_dict:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
