'''
Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
'''

def transpose(matrix: [[],[]]):
    result = []
    for n in range(len(matrix[0])):
        result.append([])
        for m in range(len(matrix)):
            result[n].append(matrix[m][n])
    return result
    
def main():
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(transpose(matrix=matrix))

if __name__ == "__main__":
    main()
