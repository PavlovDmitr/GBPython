


from copy import deepcopy


class Matrix:
    '''
    Matrix Has you:)
    '''
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matrix)

    def size(self):
        sizepair = (len(self.matrix), len(self.matrix[0]))
        return sizepair

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)
    

    def __sum__(self, other):
        if (not isinstance(other, Matrix)):
            return 'Второй объект не Матрица'
        if self.size() != other.size():
            return 'Размеры Матриц не совпадают'
        
        
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    def __eq__(self, other: object) -> bool:
        if (not isinstance(other, Matrix)):
            return False
        if self.size() != other.size():
            return False
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if other[i][j] != self.matrix[i][j]:
                    return False
        return True
           

    def __mul__(self, other):
        if (not isinstance(other, Matrix)):
            return 'Второй объект не Матрица'
        if len(self.matrix) != len(other.matrix[0]) or len(self.matrix[0]) != len(other.matrix):
            return 'Нельзя перемножить матрицы таких размерностей'
        
        result = Matrix([[0 for x in range(len(other.matrix))] for y in range(len(self.matrix[0]))])
        
        for i in range(len(self.matrix[0])):
            for j in range(len(other.matrix)):
                for k in range(len(other.matrix[0])):
                    result.matrix[i][j] += self.matrix[k][i] * other.matrix[j][k]
                
        return result



    def __rmul__(self, other):
        return self.__mul__(other)
    
def test():
    matr = Matrix([[10, 15, 20], [20, 40, 50]])

    print(matr.__doc__)
    print(matr.size())
    print(matr.__sum__(Matrix([[1, 2, 3], [3,2,1]])))
    print(matr.__eq__(Matrix([[10, 15, 20], [20, 40, 50]])))
    print(matr.__eq__(Matrix([[10, 14, 20], [20, 40, 50]])))
    print(matr.__mul__(Matrix([[1, 2], [4, 5], [4, 1]])))



if __name__ == '__main__':
    test()