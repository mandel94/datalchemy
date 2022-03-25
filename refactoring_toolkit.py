import numpy as np
from typing import Union

def refactors_dict(d, replace_missing: Union[str, int, float]=None) -> dict:
    '''Refactor leaf values of dictionary of dictionaries.

    This function is optimized to take a dictionary of dictionaries as input 
    and refactor its leaf values. Leaf values are defined as the values that
    are at the final nodes of the tree representation of a dictionary of
    dictionaries. When we access a dictionary by key, the accessed value is 
    a leaf values if it is not a dictionary itself.

    Returns: 
        dict: A (nested) dictionary

    '''
    if isinstance(d, dict):
        # Get dictionary of values for all keys
        return {k: refactors_dict(sub_d, replace_missing) \
                for k, sub_d in d.items()}
    elif isinstance(d, (list, tuple)):
        if d: # If list is not void
            # Check first list item
            if isinstance(d[0], dict): 
                # Recursive call
                return {k: refactors_dict(sub_d, replace_missing) \
                        for k, sub_d in d[0].items()}
            else: # d is a list of categories
                return {cat: 1 for cat in d}  # Creare dictionary from categories
        else: # List is void
            return d
    else:  # d is not dict nor list
        if d in [None, np.nan]:
            return replace_missing if replace_missing else None
        else:
            return d  


def refactors(data, replace_missing: Union[str, int, float]=None):
    """Polymorphic refactoring function
    
    If ``data`` is a dictionary, ``refactors_dict`` is applied. This function 
    'normalizes' the input, such that no value of the input dictionary can
    be a list of dictionaris, or other data structure whose elemenets are 
    dictionary (such as a tuple).

    replace_missing (Union[int, str, float]): Value with which to fill 
        missing values. Missing data are indicated by the following 
        'sentinel' values:
                - the ``None`` python object, often used for missing data.
                - the ``NaN`` special floating-point value.    

    """
    if isinstance(data, dict):
        refactored_data = refactors_dict(data, replace_missing)
    return refactored_data


def map_refactors(data, replace_missing: Union[str, int, float]=None):
    """Apply ``refactors`` to each element of a list.
    
    See the documentation of ``refactors``. 

    Returns:
        list: The list of the results of the query, applied once for each 
        element of the input list. 
    """
    if not isinstance(data, (list, tuple)):
                raise TypeError("Cannot map-apply on non-iterable input")
    refactored_data = [refactors(d, replace_missing) for d in data]
    return refactored_data


