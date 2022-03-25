# Copyright 2022 Manuel 


#----------------HandyManny-----------------------

from distutils.core import run_setup
from typing import Sequence, Any, Union
from unittest import result
import numpy as np
import json
import pdb

from .query_toolkit import query
from .refactoring_toolkit import refactors, refactors_dict



class HandyManny():
    """What can HandyManny do for you? Apply some data alchemy!"""
    
    def __init__(self, data: Any) -> "HandyManny":
        """Summon an instance of HandyManny!

        data (Any): The data to be transformed. 
        """
        self.data = data


    def refactors_dict(self, replace_missing: Union[str, int, float]=None, 
                       inplace=True) -> dict:
        '''HandyManny refactors leaf values of dictionary of dictionaries.

        This function is optimized to take a dictionary of dictionaries as input 
        and refactor its leaf values. Leaf values are defined as the values that
        are at the final nodes of the tree representation of a dictionary of
        dictionaries. When we access a dictionary by key, the accessed value is 
        a leaf values if it is not a dictionary itself.
        See ``self.refactors`` for the documentation
    
        Returns: 
            dict: A (nested) dictionary

        '''
        refactored_data = refactors_dict(self.data, replace_missing)
        if inplace:
            self.data = refactored_data
        return refactored_data


    def refactors(self, replace_missing: Union[str, int, float]=None,
                  inplace=True):
        """Polymorphic refactoring function
        
        If ``self.data`` is a dictionary, ``self.refactors_dict`` is applied. This function 
        'normalizes' the input, such that no value of the input dictionary can
        be a list of dictionaris, or other data structure whose elemenets are 
        dictionary (such as a tuple).

        replace_missing (Union[int, str, float]): Value with which to fill 
            missing values. Missing data are indicated by the following 
            'sentinel' values:
                 - the ``None`` python object, often used for missing data.
                 - the ``NaN`` special floating-point value.    
        inplace (bool): If ``True``, overwrite the data held by HandyManny

        """
        if isinstance(self.data, dict):
            refactored_data = self.refactors_dict(self.data, replace_missing)
        if inplace:
            self.data = refactored_data
        return refactored_data


    def map_refactors(self, replace_missing: Union[str, int, float]=None,
                      inplace=True):
        """Apply ``self.refactors`` to each element of a list.
        
        See the documentation of ``self.refactors``. 

        Returns:
            list: The list of the results of the query, applied once for each 
            element of the input list. 
        """
        if not isinstance(self.data, (list, tuple)):
                    raise TypeError("Cannot map-apply on non-iterable input")
        refactored_data = [refactors(d, replace_missing) for d in self.data]
        if inplace:
            self.data = refactored_data
        return refactored_data

 
    def query(self, key_tree, identifier=None, inplace=True):
        """A quite creative way to query a (nested) dictionary
    
        Args:
            key_tree (dict): A (nested) dictionary representing the keys of ``data`` that will 
            be kept in the final result. 
            identifier (str): The label of the identifier. This will be included in 
            the final query result, independently of the query. Defaults to ``None``.
            inplace (bool): If ``True``, overwrite the data held by HandyManny
        
        Returns:
            dict: A (nested) dictionary.
        """
        if not isinstance(self.data, dict):
            raise TypeError("""``self.data`` is not a dictionary. It cannot be queried upon""")
        query_data = [query(d, key_tree, identifier) for d in self.data]
        if inplace:
            self.data = query_data
        return query_data
        

    def map_query(self, key_tree, identifier=None, inplace=True):
        """Apply ``self.query`` to each element of a list or tuple.
        
        See the documentation of ``self.query``. 

        Returns:
            list: The list of the results of the query, applied once for each 
            element of the input list. 

        """
        if not isinstance(self.data, (list, tuple)):
            raise TypeError("Cannot map-apply on non-iterable input")
        query_data = [query(d, key_tree, identifier) \
                      for d in self.data]
        if inplace:
            self.data = query_data
        return query_data


    def apply(self, fun, inplace: bool=True):
        """Apply function ``fun`` to ``self.data`` and return its result"""
        output =  fun(self.data)
        if inplace:
            self.data = output
        return output
    

    def map_apply(self, fun, inplace: bool=True):
        """Map-apply function ``fun`` to ``self.data`` iterable and return the 
        list of results 
        """
        if not isinstance(self.data, (list, tuple)):
            raise TypeError("Cannot map-apply on non-iterable input")
        map_outputs = [fun(x) for x in self.data]
        if inplace:
            self.data = map_outputs
        return map_outputs



        