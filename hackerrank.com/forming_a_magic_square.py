
def formingMagicSquare(s):
    _min = 100
    def computeDifference(s,M):
        d = 0
        for row in range(3):
            for col in range(3):
                d += abs(s[row][col] - M[row][col])
        return d
    def flipRight(M):
        dummy = [[0 for i in range(3)]for i in range(3)]
        for ar in range(3):
            for ac in range(3):
                dummy[ac][2-ar] = M[ar][ac]
        M = dummy
    master = [
            [8, 3, 4],
            [1, 5, 9],
            [6, 7, 2],
    ]
    c_1 = [['x','2-y'], ['2-x','y'], ['y','x'], ['2-y','2-x']]
    for exp in c_1:
        for _ in range(3):
            dummy = [[0 for i in range(3)]for i in range(3)]
            for x in range(3):
                for y in range(3):
                    dummy[x,y] = Master[eval(exp[0])][eval(exp[1])]
            d = computeDifference(s,dummy)
            if d < _min:
                _min = d
        flipRight(dummy)

    return _min



   

