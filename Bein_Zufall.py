import numpy as np
import matplotlib.pyplot as plt
import random

fig = plt.figure()
ax = plt.axes(projection="3d")

def init():
    ax.set_xlim([-2, 2])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, -1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    print("initiated")
def rotations_x(alpha):
    Matrix = np.array([[1, 0, 0, 0],
                       [0, np.cos(alpha), -np.sin(alpha), 0],
                       [0, np.sin(alpha), np.cos(alpha), 0],
                       [0, 0, 0, 1]])
    # print(Matrix)
    return Matrix
def rotations_y(alpha):
    Matrix = np.array([[np.cos(alpha), 0, np.sin(alpha), 0],
                       [0, 1, 0, 0],
                       [-np.sin(alpha), 0, np.cos(alpha), 0],
                       [0, 0, 0, 1]])
    # print(Matrix)
    return Matrix
def rotations_z(alpha):
    Matrix = np.array([[np.cos(alpha), -np.sin(alpha), 0, 0],
                       [np.sin(alpha), np.cos(alpha), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    # print(Matrix)
    return Matrix
def transmatrix(x_y_z):
    x = x_y_z[0]
    y = x_y_z[1]
    z = x_y_z[2]
    tmatrix = np.array([[1, 0, 0, x],
                        [0, 1, 0, y],
                        [0, 0, 1, z],
                        [0, 0, 0, 1]])
    return tmatrix

init()

def EndPoints(alpha,beta,gamma):

    rotationValue_1 = -np.deg2rad(0+alpha)
    rotationValue_2 = np.deg2rad(0+beta)
    rotationValue_3 = np.deg2rad(0+gamma)

    first_startpoint = np.array([0, 0, 0, 1])

    first_direction = np.array([0, 0, -1, 1])
    second_direction = np.array([0, 0, -1, 1])
    third_direction = np.array([0, 0, -1, 1])


    test1 = np.matmul(rotations_x(rotationValue_1), transmatrix(first_startpoint))
    test1_vector = np.matmul(test1, first_direction)

    test2 = np.matmul(np.matmul(rotations_x(rotationValue_1), rotations_y(rotationValue_2)), transmatrix([0, 0, 0]))
    test2_vector = np.matmul(test2, second_direction)

    test3 = np.matmul(np.matmul(np.matmul(rotations_x(rotationValue_1), rotations_y(rotationValue_3)), rotations_y(rotationValue_2)), transmatrix([0, 0, 0]))
    test3_vector = np.matmul(test3,third_direction)


    x_end = test1_vector[0] + test2_vector[0] + test3_vector[0] + first_startpoint[0]
    y_end = test1_vector[1] + test2_vector[1] + test3_vector[1] + first_startpoint[1]
    z_end = test1_vector[2] + test2_vector[2] + test3_vector[2] + first_startpoint[2]

    print( "x =", x_end, "y =", y_end, "z =", z_end,"\n")
    position = [x_end,y_end,z_end]
    return position

for i in range(0,100):
    random_alpha = random.randint(-10, 10)
    random_beta = random.randint(-90, 90)
    random_gamma = random.randint(-90, 90)
    position = EndPoints(random_alpha,random_beta,random_gamma)
    ax.scatter(position[0],position[1],position[2])
plt.show()