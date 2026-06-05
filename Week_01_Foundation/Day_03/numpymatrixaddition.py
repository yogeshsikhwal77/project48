import numpy as np
import time

class matrix:
    def __init__(self,data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows> 0 else 0

    @classmethod
    def from_file(cls, filename):
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                data = [[int(num) for num in line.split()] for line in lines]
                return cls(data)
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
            return None
        
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for row in self.data:
                str_row = " ".join([str(num) for num in row])
                f.write(str_row + "\n")
                
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Not the same dimension")
        new_data = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                new_row.append(self.data[i][j] + other.data[i][j])
            new_data.append(new_row)
        return matrix(new_data)
    

    
def numpy_matrix_workflow(file_a,file_b,file_c):
    try:
        mat1 = np.loadtxt(file_a.txt,dtype = int)
        mat2 = np.loadtxt(file_b.txt,dtype = int)
        if mat1.shape != mat2.shape:
            raise ValueError("not the same dimension")
        result = mat1 + mat2
        np.savetxt(file_c,result, fmt="%d")
        return result
    except OSError:
        print("file not found")
    



if __name__ == "__main__":
    size =1000
    data1 = np.random.randint(1,100,size=(size,size))
    data2 = np.random.randint(1,100,size=(size,size))
    
    py_mat1 = matrix(data1.tolist())
    py_mat2 = matrix(data2.tolist())

    start_time = time.time()
    py_result =py_mat1 + py_mat2
    py_duration = time.time() - start_time
    print(py_duration)

    start_time = time.time()
    np_result =data1 + data2
    np_duration = time.time() - start_time
    print(np_duration)

    if np_duration > 0:
        speedup = py_duration / np_duration
        print(f"NumPy is {speedup:.2f}x faster for a {size}x{size} matrix.")

  