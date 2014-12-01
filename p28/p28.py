
def GetSumForLayer(n):
    if n == 1:
        return 1
    # dimension of square w this layer
    dim = n * 2 - 1
    # highest value in this layer
    endval = dim ** 2
    return endval * 4 - ((dim - 1) * 6)

def Run():
    return sum([GetSumForLayer(i) for i in range(1, 502)])
