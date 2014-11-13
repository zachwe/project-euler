import time

def LoadData(filename):
    """
    f:
        Filename of input.
    Returns:
        2-dimensional array containing the contents of the file.

    """
    with open(filename, "rb") as f:
        out = []
        for row in f:
            out.append([int(i) for i in row.split(' ')])
    return out


def GetMaxProduct(ar):
    """
    ar:
        List of integers.
    Returns:
        Maximum 4-product.
    """
    i, maxvalue, maxcombo = 0, 0, [0] * 4
    # The reduce function
    rf = lambda x, y: x * y
    while i + 3 < len(ar):
        selection = ar[i:i + 4]
        product = reduce(rf, selection, 1)
        if product > maxvalue:
            maxvalue = product
            maxcombo = selection
        i += 1
    return (maxvalue, maxcombo)

def GetDiagAr(i, j, dim, matrix, direction=1):
    out = []
    if (j == 0 or i == 0) and direction == 1:
        # We're on the left side or the top of the matrix, looking down
        while i <= dim - 4 and j <= dim - 4:
            out.append(matrix[i][j])
            i += 1
            j += 1
    elif (j == 0 or i == dim - 1) and direction == -1:
        # left side or bottom looking up
        while i >= 3 and j <= dim - 4:
            out.append(matrix[i][j])
            i -= 1
            j += 1
    return out

def Run():
    """
    Runs everything
    """
    matrix = LoadData("data.txt")
    init = time.time()
    # Assuming square matrix
    dim = len(matrix)
    # Linear maximums are straightforward
    rowmax = max(map(GetMaxProduct, matrix))
    transpose = [[matrix[i][j] for i in range(dim)] for j in range(dim)]
    colmax = max(map(GetMaxProduct, transpose))
    
    # Now the diagonal maximums
    diagsLD = [GetDiagAr(i, 0, dim, matrix, 1) for i in range(dim)]
    diagsTD = [GetDiagAr(0, i, dim, matrix, 1) for i in range(dim)]
    diagsLU = [GetDiagAr(i, 0, dim, matrix, -1) for i in range(dim)]
    diagsBU = [GetDiagAr(dim - 1, i, dim, matrix, -1) for i in range(dim)]
    diags = diagsLD + diagsTD + diagsLU + diagsBU
    diagmax = max(map(GetMaxProduct, diags))
    end = time.time() 
    return (max(rowmax, colmax, diagmax, lambda x, y: x[0] > y[0]), end - init)
    

if __name__ == "__main__":
    print Run()
