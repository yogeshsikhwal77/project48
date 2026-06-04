class matrix:
    def __init__(self,data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows >0 else 0
        
    @classmethod
    def from_file(cls, filename):
        try:
            with open(filename,"r") as f:
                lines = f.readlines()
                data = [[int(num) for num in line.split()] for line in lines]
                return cls(data)
        except FileNotFoundError:
            print(f"error the file {filename} was not found")
            return None
        
    def save_to_file(self,filename):
        with open(filename,"w") as f :
            for row in self.data:
                str_row = " ".join([str(num) for num in row])
                f.write(str_row +"\n")
    def __add__(self,other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("not same dimension")
        new_data = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                new_row.append(self.data[i][j]+other.data[i][j])
            new_data.append(new_row)
        return matrix(new_data)
    
    def __str__(self):
      return "\n".join([str(row) for row in self.data])

if __name__ == "__main__":

   mat1 = matrix.from_file("matrix_A.txt")
   mat2 = matrix.from_file("matrix_B.txt")
   
   try:
       print("\nAdding matrices:")
       result = mat1+mat2
       print(result)
   
       result.save_to_file("matrix_C.txt")
       print("Result saved to 'matrix_add_result.txt'")
   except ValueError as e:
       print(f"Math Error: {e}")
   