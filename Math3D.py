import math


class Vec3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return str(self.x) + '\n' + str(self.y) + '\n' + str(self.z) + '\n'

class Vec4:

    def __init__(self, x, y, z, w=1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self) -> str:
        return str(self.x) + '\n' + str(self.y) + '\n' + str(self.z) + '\n' + str(self.w) + '\n'


class Mat4:
    def __init__(self):
        # identity matrix
        self.matrix = [[0 for x in range(4)] for y in range(4)]
        for i in range(4):
            self.matrix[i][i] = 1

    def __str__(self) -> str:
        string = ""
        for i in range(4):
            for j in range(4):
                string += str(self.matrix[i][j]) + " "
            string += '\n'
        return string

    def __mul__(self, other):
        if type(other) is Vec4:
            x = self.matrix[0][0] * other.x + self.matrix[0][1] * other.y + self.matrix[0][2] * other.z + self.matrix[0][3] * other.w
            y = self.matrix[1][0] * other.x + self.matrix[1][1] * other.y + self.matrix[1][2] * other.z + self.matrix[1][3] * other.w
            z = self.matrix[2][0] * other.x + self.matrix[2][1] * other.y + self.matrix[2][2] * other.z + self.matrix[2][3] * other.w
            w = self.matrix[3][0] * other.x + self.matrix[3][1] * other.y + self.matrix[3][2] * other.z + self.matrix[3][3] * other.w
            return Vec4(x, y, z, w)

        if type(other) is Mat4:
            new_mat = Mat4()
            new_mat.matrix = [[0 for x in range(4)] for y in range(4)]
            a = self.matrix
            b = other.matrix
            new_mat.matrix[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0] + a[0][2] * b[2][0] + a[0][3] * b[3][0]
            new_mat.matrix[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1] + a[0][2] * b[2][1] + a[0][3] * b[3][1]
            new_mat.matrix[0][2] = a[0][0] * b[0][2] + a[0][1] * b[1][2] + a[0][2] * b[2][2] + a[0][3] * b[3][2]
            new_mat.matrix[0][3] = a[0][0] * b[0][3] + a[0][1] * b[1][3] + a[0][2] * b[2][3] + a[0][3] * b[3][3]

            new_mat.matrix[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0] + a[1][2] * b[2][0] + a[1][3] * b[3][0]
            new_mat.matrix[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1] + a[1][2] * b[2][1] + a[1][3] * b[3][1]
            new_mat.matrix[1][2] = a[1][0] * b[0][2] + a[1][1] * b[1][2] + a[1][2] * b[2][2] + a[1][3] * b[3][2]
            new_mat.matrix[1][3] = a[1][0] * b[0][3] + a[1][1] * b[1][3] + a[1][2] * b[2][3] + a[1][3] * b[3][3]

            new_mat.matrix[2][0] = a[2][0] * b[0][0] + a[2][1] * b[1][0] + a[2][2] * b[2][0] + a[2][3] * b[3][0]
            new_mat.matrix[2][1] = a[2][0] * b[0][1] + a[2][1] * b[1][1] + a[2][2] * b[2][1] + a[2][3] * b[3][1]
            new_mat.matrix[2][2] = a[2][0] * b[0][2] + a[2][1] * b[1][2] + a[2][2] * b[2][2] + a[2][3] * b[3][2]
            new_mat.matrix[2][3] = a[2][0] * b[0][3] + a[2][1] * b[1][3] + a[2][2] * b[2][3] + a[2][3] * b[3][3]

            new_mat.matrix[3][0] = a[3][0] * b[0][0] + a[3][1] * b[1][0] + a[3][2] * b[2][0] + a[3][3] * b[3][0]
            new_mat.matrix[3][1] = a[3][0] * b[0][1] + a[3][1] * b[1][1] + a[3][2] * b[2][1] + a[3][3] * b[3][1]
            new_mat.matrix[3][2] = a[3][0] * b[0][2] + a[3][1] * b[1][2] + a[3][2] * b[2][2] + a[3][3] * b[3][2]
            new_mat.matrix[3][3] = a[3][0] * b[0][3] + a[3][1] * b[1][3] + a[3][2] * b[2][3] + a[3][3] * b[3][3]
            return new_mat

    def __rmul__(self, other):
        if type(other) is Vec4:
            x = self.matrix[0][0] * other.x + self.matrix[0][1] * other.y + self.matrix[0][2] * other.z + self.matrix[0][3] * other.w
            y = self.matrix[1][0] * other.x + self.matrix[1][1] * other.y + self.matrix[1][2] * other.z + self.matrix[1][3] * other.w
            z = self.matrix[2][0] * other.x + self.matrix[2][1] * other.y + self.matrix[2][2] * other.z + self.matrix[2][3] * other.w
            w = self.matrix[3][0] * other.x + self.matrix[3][1] * other.y + self.matrix[3][2] * other.z + self.matrix[3][3] * other.w
            return Vec4(x, y, z, w)

        if type(other) is Mat4:
            new_mat = Mat4()
            new_mat.matrix = [[0 for x in range(4)] for y in range(4)]
            a = self.matrix
            b = other.matrix
            new_mat.matrix[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0] + a[0][2] * b[2][0] + a[0][3] * b[3][0]
            new_mat.matrix[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1] + a[0][2] * b[2][1] + a[0][3] * b[3][1]
            new_mat.matrix[0][2] = a[0][0] * b[0][2] + a[0][1] * b[1][2] + a[0][2] * b[2][2] + a[0][3] * b[3][2]
            new_mat.matrix[0][3] = a[0][0] * b[0][3] + a[0][1] * b[1][3] + a[0][2] * b[2][3] + a[0][3] * b[3][3]

            new_mat.matrix[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0] + a[1][2] * b[2][0] + a[1][3] * b[3][0]
            new_mat.matrix[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1] + a[1][2] * b[2][1] + a[1][3] * b[3][1]
            new_mat.matrix[1][2] = a[1][0] * b[0][2] + a[1][1] * b[1][2] + a[1][2] * b[2][2] + a[1][3] * b[3][2]
            new_mat.matrix[1][3] = a[1][0] * b[0][3] + a[1][1] * b[1][3] + a[1][2] * b[2][3] + a[1][3] * b[3][3]

            new_mat.matrix[2][0] = a[2][0] * b[0][0] + a[2][1] * b[1][0] + a[2][2] * b[2][0] + a[2][3] * b[3][0]
            new_mat.matrix[2][1] = a[2][0] * b[0][1] + a[2][1] * b[1][1] + a[2][2] * b[2][1] + a[2][3] * b[3][1]
            new_mat.matrix[2][2] = a[2][0] * b[0][2] + a[2][1] * b[1][2] + a[2][2] * b[2][2] + a[2][3] * b[3][2]
            new_mat.matrix[2][3] = a[2][0] * b[0][3] + a[2][1] * b[1][3] + a[2][2] * b[2][3] + a[2][3] * b[3][3]

            new_mat.matrix[3][0] = a[3][0] * b[0][0] + a[3][1] * b[1][0] + a[3][2] * b[2][0] + a[3][3] * b[3][0]
            new_mat.matrix[3][1] = a[3][0] * b[0][1] + a[3][1] * b[1][1] + a[3][2] * b[2][1] + a[3][3] * b[3][1]
            new_mat.matrix[3][2] = a[3][0] * b[0][2] + a[3][1] * b[1][2] + a[3][2] * b[2][2] + a[3][3] * b[3][2]
            new_mat.matrix[3][3] = a[3][0] * b[0][3] + a[3][1] * b[1][3] + a[3][2] * b[2][3] + a[3][3] * b[3][3]
            return new_mat


def translate(mat, vec3):
    mat.matrix[0][3] = vec3.x
    mat.matrix[1][3] = vec3.y
    mat.matrix[2][3] = vec3.z

def rotate(mat, angle, vec3):
    angle_x = vec3.x * angle
    angle_y = vec3.y * angle
    angle_z = vec3.z * angle

    matB = Mat4()
    matA = mat

    #x rotation
    matB.matrix[1][1] = math.cos(angle_x)
    matB.matrix[1][2] = -math.sin(angle_x)
    matB.matrix[2][1] = math.sin(angle_x)
    matB.matrix[2][2] = math.cos(angle_x)

    matA *= matB

    #y rotation
    matB = Mat4()
    matB.matrix[0][0] = math.cos(angle_y)
    matB.matrix[0][2] = math.sin(angle_y)
    matB.matrix[2][0] = -math.sin(angle_y)
    matB.matrix[2][2] = math.cos(angle_y)

    matA *= matB

    #z rotation
    matB = Mat4()
    matB.matrix[0][0] = math.cos(angle_z)
    matB.matrix[0][1] = -math.sin(angle_z)
    matB.matrix[1][0] = math.sin(angle_z)
    matB.matrix[1][1] = math.cos(angle_z)

    matA *= matB
    mat.matrix = matA.matrix

