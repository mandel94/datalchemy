import sys

def query(data, key_tree, identifier=None):
    """A quite creative way to query a (nested) dictionary
    
    Args:
        data (dict): A (nested) dictionary.
        key_tree (dict): A (nested) dictionary representing the keys of `data `that will 
        be kept in the final result. 
        identifier (str): The label of the identifier. This will be included in 
        the final query result, independently of the query. Defaults to `None`.
    
    Returns:
        dict: A (nested) dictionary.
    """

    if isinstance(data, (int, str)): # data is a leaf value
        # Leaf values cannot be queried
        return data

    if key_tree == "all": # No specific nodes are queried 
        return data # Return eveything

    if isinstance(key_tree, list): 
        # Apply directly key_tree as a filter
        return {k:data[k] for k in data if k in key_tree}
    
    if isinstance(key_tree, str): 
        # Apply directly key_tree as a filter 
        return {k:data[k] for k in data if k in key_tree}

    # Else --> key_tree is dict
     # Dictionary that results from query (to update at each run of the loop)
    grand_q = {}
    if identifier:
        grand_q[identifier] = data[identifier]
    for key in key_tree.keys():
        # Inclusive filter
        filter_ = key_tree[key] 
        sub_data = data[key]
        if isinstance(sub_data, (int, str)): # sub_data is a leaf value
        # Leaf values cannot be queried
            return sub_data
        if key not in data.keys():
            continue # Go on if key not found in data
        # Test the type of filter
        if filter_ == "all": 
            try:
                # q is the loop result of the query
                if isinstance(sub_data, dict):
                    q = {k:v for k, v in sub_data.items()}
                else:
                    q = sub_data
                # Add loop result to grand dict
                grand_q[key] = q
            except:  
                print(
                    """Some error occurred at {} key for 
                       filter {}""".format(key, filter_))
        elif isinstance(filter_, list): # A list of categories to keep
            matching_keys = [k for k in sub_data if k in filter_]
            try:
                q = {m: sub_data[m] for m in matching_keys}
                grand_q[key] = q
            except:
                print(
                    """Some error occurred at {} key for 
                       filter {}""".format(key, filter_))
        elif isinstance(filter_, dict): 
            try:
                if not isinstance(sub_data, dict): # Dictionary reached leaf value
                    q = sub_data
                else: # Recurrence case (leaf value not reached)
                    sub_data = {k:v for k,v in sub_data.items() if k in filter_}
                    q = {m: query(sub_data[m], filter_[m]) for m in sub_data}
                grand_q[key] = q
            except:
                print(
                    """Some error occurred at {} key for 
                       filter {}""".format(key, filter_))
        else:
            sys.exit(
                """key_tree[{}] is not a list, 
                nor a dict,
                nor equal to 'all'""".format(key))
    return grand_q


def map_query(data, key_tree, identifier=None, inplace=True):
    """Apply ``query`` function to each element of a list or tuple.
    
    See the documentation of ``query``. 

    Returns:
        list: The list of the results of the query, applied once for each 
        element of the input list. 

    """
    if not isinstance(data, (list, tuple)):
        raise TypeError("Cannot map-apply on non-iterable input")
    query_data = [query(d ,key_tree, identifier) for d in data]
    return query_data




    
        
   





