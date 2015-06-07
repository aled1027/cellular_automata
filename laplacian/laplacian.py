"""
This requires python3 because of super()
"""
class Matrix(object):
    """
    A simple matrix with read and write
    m = Matrix(size=3)
    m[i,j] := ith row and jth column
    m[i] = ith row
    We start with 0th row and column.
    """
    def __init__(self, xs=None, size=3):
        if xs:
            self.matrix = xs
        else:
            self.matrix = [[0]*size for _ in range(size)]

    def __setitem__(self, pos, item):
        if isinstance(pos, tuple):
            if pos[0] is None:
                for i,row in enumerate(self.matrix):
                    row[pos[1]] = item[i]
            elif pos[1] is None:
                self.matrix[pos] = item
            else:
                self.matrix[pos[0]][pos[1]] = item
        elif isinstance(pos, int):
            self.matrix[pos] = item
        else:
            raise("pos is not of a valid type")

    def __getitem__(self, pos):
        if isinstance(pos, tuple):
            return self.matrix[pos[0]][pos[1]]
        elif isinstance(pos, int):
            return self.matrix[pos]
        else:
            raise("pos is not of a valid type")

    def __repr__(self):
        s = ""
        for l in self.matrix:
            s = s + repr(l) + "\n"
        return s

    def __str__(self):
        return str(self.matrix)

    def __len__(self):
        return len(self.matrix)

    def row(self, r):
        return self.matrix[r]

class Laplacian(Matrix):
    def __init__(self, xs=None, size=3):
        super().__init__(xs=xs, size=size)

    @property
    def num_edges(self):
        counter = 0
        for row in self:
            for entry in row:
                if entry > 0:
                    counter+=1
        return counter

    def get_neighbor_indices(self, row=0):
        ret_list = []
        for i, entry in enumerate(self.row(row)):
            if entry > 0:
                ret_list.append((entry, i))
        return ret_list

    def symmetrize(self):
        """
        given the top right of the matrix is filled out, fill in the bottom left
        with the appropriate symmetric entries
        [a,b,c]    [a,b,c]
        [0,e,f] -> [b,e,f]
        [0,0,g]    [c,f,g]
        """
        size = len(self.matrix)
        for i, row in enumerate(self.matrix):
            for j in range(i,size):
                self[j,i] = self[i,j]

    def update_diagonals(self):
        for idx, row in enumerate(self.matrix):
            counter = 0
            for i, entry in enumerate(row):
                if idx != i and entry > 0:
                    # if we are at the diagonal entry, don't count it.
                    # if the entry is non-positive, don't count i
                    counter += entry
            row[idx] = -1 * counter


