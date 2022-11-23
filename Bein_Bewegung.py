import numpy as np
import matplotlib.pyplot as plt

def init():
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([0, 3])
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


fig = plt.figure()
ax = plt.axes(projection="3d")
init()

rotationValue_1 = -np.deg2rad(45)
rotationValue_2 = np.deg2rad(0)
rotationValue_3 = np.deg2rad(0)

first_startpoint = np.array([0, 0, 0, 1])

first_direction = np.array([0, 0, 1, 1])
second_direction = np.array([0, 0, 1, 1])
third_direction = np.array([0, 0, 1, 1])

#first_direction = np.matmul(rotations_x(rotationValue_1), first_direction)
#second_direction = np.matmul(rotations_y(rotationValue_2), second_direction)
#third_direction = np.matmul(rotations_y(rotationValue_2), third_direction)

#second_startpoint = np.array([first_startpoint[0] + first_direction[0], first_startpoint[1] + first_direction[1], first_startpoint[2] + first_direction[2], 1])
#third_startpoint = np.array([second_startpoint[0] + second_direction[0], second_startpoint[1] + second_direction[1], second_startpoint[2] + second_direction[2], 1])

test1 = np.matmul(rotations_x(rotationValue_1), transmatrix(first_startpoint))
test1_vector = np.matmul(test1, first_direction)

test2 = np.matmul(np.matmul(rotations_x(rotationValue_1), rotations_y(rotationValue_2)), transmatrix([0, 0, 0]))
test2_vector = np.matmul(test2, second_direction)

test3 = np.matmul(np.matmul(np.matmul(rotations_x(rotationValue_1), rotations_y(rotationValue_3)), rotations_y(rotationValue_2)), transmatrix([0, 0, 0]))
test3_vector = np.matmul(test3,third_direction)

ax.quiver(first_startpoint[0], first_startpoint[1], first_startpoint[2], test1_vector[0], test1_vector[1], test1_vector[2], color="r" )   #erster Abschnit
#ax.quiver(first_startpoint[0], first_startpoint[1], first_startpoint[2], test1[0], test1[1], test1[2], color="y", )

ax.quiver(first_startpoint[0]+test1_vector[0], first_startpoint[1]+test1_vector[1], first_startpoint[2]+test1_vector[2], test2_vector[0], test2_vector[1], test2_vector[2], color="r", )
#ax.quiver(first_startpoint[0]+test1_vector[0], first_startpoint[1]+test1_vector[1], first_startpoint[2]+test1_vector[2], test2[0], test2[1], test2[2], color="y", )

ax.quiver(first_startpoint[0]+test1_vector[0]+test2_vector[0], first_startpoint[1]+test1_vector[1]+test2_vector[1], first_startpoint[2]+test1_vector[2]+test2_vector[2], test3_vector[0], test3_vector[1], test3_vector[2], color="r", )
#zwischenErgebnis = np.matmul(rotations_y(rotationValue), transMatrix(newcords))
#zwischenVector = np.matmul(rotations_y(rotationValue), start_vector)
#ergebnis = np.matmul(zwischenErgebnis, start_vector)
#print( "",round(ergebnis[0]), "\n", round(ergebnis[1]), "\n", round(ergebnis[2]))
#ax.quiver(start[0], start[1], start[2], ergebnis[0], ergebnis[1], ergebnis[2])  # Ergebnis
#ax.quiver(start[0], start[1], start[2], zwischenVector[0], zwischenVector[1], zwischenVector[2],color="g")  # zwischenVector
#ax.quiver(start[0], start[1], start[2], newcords[0], newcords[1], newcords[2], color="y")  # NewCoords

"""
ax.quiver(first_startpoint[0], first_startpoint[1], first_startpoint[2], first_direction[0], first_direction[1], first_direction[2], color="b", )   #erster Abschnit
ax.quiver(second_startpoint[0], second_startpoint[1], second_startpoint[2], second_direction[0], second_direction[1], second_direction[2], color="y")   #zweiter Abschnitt
ax.quiver(third_startpoint[0], third_startpoint[1], third_startpoint[2], third_direction[0], third_direction[1], third_direction[2], color="r")   #dritter Abschnitt
"""

x_end = test1_vector[0] + test2_vector[0] + test3_vector[0] + first_startpoint[0]
y_end = test1_vector[1] + test2_vector[1] + test3_vector[1] + first_startpoint[1]
z_end = test1_vector[2] + test2_vector[2] + test3_vector[2] + first_startpoint[2]

print( "x =", x_end, "\ny =", y_end, "\nz =", z_end)

plt.show()




