import json
from typing import Sequence


def read_jsnl(file: str, keys: Sequence[str], 
                identifier: str, remove_void: bool=False) -> dict:
    """Read data from a JSON Line file.
    
    Args:
        file: The file from which to import the data.
        keys: For each line read from `file`, import just the root-level 
            keys that are included in this list. Root-level keys are the 
            keys at the top of the hierarchical-tree representation of a 
            json file.
        identifier: If `remove_void` is set to `True`, this key won't be 
            considered when filtering for void observations.   
        remove_void: Should HandyManny remove observations with void values 
            on `keys`?        
    Returns:
        dict: A (nested) dictionary.

        """
    data = []
    with open(file, "r") as f:
        for line in f:
            # Select only non-null data. Non-null data has been defined as json with 
            # value at the highest root-level different from an empty list.
            d = json.loads(line)
            if remove_void:
                if keys == "all":
                    # Check for non-empty v's. Identifier is not considered. 
                    not_void = sum(len(v)>0 for k, v in d.items() if k != identifier)         
                else:
                    # Check the presence of non-null data at root-level keys. This
                    # time we don't need to check for the identifier, as it is not 
                    # included in keys
                    not_void = sum(len(v)>0 for k, v in d.items() if k in keys)
                if not_void > 0: 
                    data.append(d)  
            else:
                data.append(d)
    return data