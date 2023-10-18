# %%
import numpy as np

class SparseMatrix:
    """A sparse matrix that uses a dictionary to store the data"""
    def __init__(self, fill_value=np.nan):
        self.data = {}
        self.fill_value = fill_value
        
    def __setitem__(self, key, value):
        i, j = key
        key = (i, j)
        self.data[key] = value

    def __getitem__(self, index):
        i, j = index
        key = (i, j)
        return self.data.get(key, self.fill_value)
# %%
m = SparseMatrix()
# %%
m[0,0] = 1.0
# %%
m[0,0]