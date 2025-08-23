def spiral(matrix):
    n = len(matrix)
    m = len(matrix[0])
    sr = 0
    er = n - 1
    sc = 0
    ec = m - 1
    result = []

    while sr <= er and sc <= ec:
        # left to right
        for i in range(sc, ec + 1):
            result.append(matrix[sr][i])
        sr += 1

        # top to bottom
        for i in range(sr, er + 1):
            result.append(matrix[i][ec])
        ec -= 1

        if sr <= er:
            # right to left
            for i in range(ec, sc - 1, -1):
                result.append(matrix[er][i])
            er -= 1

        if sc <= ec:
            # bottom to top
            for i in range(er, sr - 1, -1):
                result.append(matrix[i][sc])
            sc += 1

    return result

# Sample input
rows = int(input("Enter number of rows: ")) #2
cols = int(input("Enter number of columns: "))#3
flat_list = list(map(int, input(f"Enter {rows*cols} elements: ").split())) #1 2 3 4 5 6

# Convert flat list to 2D matrix
matrix = [flat_list[i*cols:(i+1)*cols] for i in range(rows)]

print("Spiral order:", spiral(matrix))#[1,2,3,6,5,4]