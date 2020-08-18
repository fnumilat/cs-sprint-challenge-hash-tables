# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create a dictionary
    cache = dict()

    # Create an empry array to hold the end results
    result = []

    # Create a dictionary to hold the files
    files_cache = dict()

    # Loop through the queries
    # and set the item in dictionary to 0
    for item in queries:
        cache[item] = 0

    # Loop through the files array
    for file in files:
        # Create a var called index
        # that can find a find
        index = file.rfind('/')
        # and create a var called search
        # that increases the index by one starting from the right
        search = file[index+1: ]

        # See if the search is in the files cache
        # then add it to file
        # otherwise set the search to the file
        if search in files_cache:
            files_cache[search].append(file)
        else: 
            files_cache[search] = [file]
    
    # Loop through the keys in the cache
    for key in cache.keys():
        # See if the key is in the files cache
        if key in files_cache:
            # the loop the key in the files cache
            # and add the item in the result array
            for item in files_cache[key]:
                result.append(item)


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
