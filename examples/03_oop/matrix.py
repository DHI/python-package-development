class SparseMatrix:
    "A rudimentary sparse matrix class"
    def __init__(self, shape, fill_value=0.0, data=None):
        self.shape = shape
        self._data = data if data is not None else {}
        self.fill_value = fill_value
        
    def __setitem__(self, key, value):
        i,j = key
        self._data[i,j] = float(value) 

    def __getitem__(self, key) -> float:
        i,j = key
        return self._data.get((i,j), self.fill_value)
    
    def transpose(self) -> "SparseMatrix":
        data = {(j,i) : v for (i,j),v in self._data.items()}
        return SparseMatrix(data=data,
                            shape=self.shape,
                            fill_value=self.fill_value)
    
    def __repr__(self):
        matrix_str = ""
        for j in range(self.shape[1]):
            for i in range(self.shape[0]):
                value = self[i, j]
                matrix_str += f"{value:<4}"
            matrix_str += "\n"
        return matrix_str
    
if __name__ == "__main__":
    a = SparseMatrix(shape=(3,3), fill_value=0.0)
    a[0,0] = 1.0
    a[1,1] = 2.0
    a[2,2] = 3.0
    a[0,2] = 4.0
    print(a)
    print(a.transpose())