from graphics import *
import numpy as np
import math as m
import matplotlib.pyplot as plt
from numpy.core.shape_base import block


"""function that returns the transformation cube matrix for a given rotation in x, y, and z"""

def rotationMatrix(x, y, z):
    """
    Returns the transformation matrix for a cube with a given rotation in x, y, and z
    """
    # get the rotation matrices

    Rx = np.array([[1, 0, 0, 0],
                   [0, m.cos(x), -m.sin(x), 0],
                   [0, m.sin(x), m.cos(x), 0],
                   [0, 0, 0, 1]])

    Ry = np.array([[m.cos(y), 0, m.sin(y), 0],
                   [0, 1, 0, 0],
                   [-m.sin(y), 0, m.cos(y), 0],
                   [0, 0, 0, 1]])

    Rz = np.array([[m.cos(z), -m.sin(z), 0, 0],
                   [m.sin(z), m.cos(z), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

    # return the rotation transformation matrix
    return Rx*Ry*Rz


"""function that returns the transformation cube matrix for a given rotation in x, y, and z about an arbitrary axis"""


def rotationMatrixAboutAxis(x, y, z, xp, yp, zp, t):
    """
    Returns the transformation matrix for a cube with a given rotation in x, y, and z about an arbitrary axis
    """
    A, B, C = xp - x, yp - y, zp - z
    L = m.sqrt(A**2 + B**2 + C**2)
    V = m.sqrt(B**2 + C**2)
    # get the rotation matrices
    Rx = np.array([[m.cos(t), 0, m.sin(t), 0],
                   [0, 1, 0, 0],
                   [-m.sin(t), 0, m.cos(t), 0],
                   [0, 0, 0, 1]])
    Rxi = np.array([[m.cos(-t), 0, m.sin(-t), 0],
                    [0, 1, 0, 0],
                    [-m.sin(-t), 0, m.cos(-t), 0],
                    [0, 0, 0, 1]])
    Ry = np.array([[V/L, 0, -A/L, 0],
                   [0, 1, 0, 0],
                   [A/L, 0, V/L, 0],
                   [0, 0, 0, 1]])
    Ryi = np.array([[V/L, 0, A/L, 0],
                    [0, 1, 0, 0],
                    [-A/L, 0, V/L, 0],
                    [0, 0, 0, 1]])
    Rz = np.array([[m.cos(t), -m.sin(t), 0, 0],
                   [m.sin(t), m.cos(t), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

    # get the translation matrices
    T = np.array([[1, 0, 0, -x],
                  [0, 1, 0, -y],
                  [0, 0, 1, -z],
                  [0, 0, 0, 1]])
    Ti = np.array([[1, 0, 0, x],
                   [0, 1, 0, y],
                   [0, 0, 1, z],
                   [0, 0, 0, 1]])

    # return the rotation transformation matrix
    return Ti*Rxi*Ryi*Rz*Ry*Rx*T


"""Function that returns the transformation matrix for a given translation in x, y, and z"""


def translationMatrix(coord, x, y, z):
    """
    Returns the transformation matrix for a cube with a given translation in x, y, and z
    """
    # get the translation matrices
    Tx = np.array([[1, 0, 0, x],
                   [0, 1, 0, y],
                   [0, 0, 1, z],
                   [0, 0, 0, 1]])
    final_coord = np.dot(Tx, coord)
    return final_coord


"""Function that returns the transformation matrix for a given scaling in x, y, and z"""


def scalingMatrix(coord, x, y, z):
    """
    Returns the transformation matrix for a cube with a given scaling in x, y, and z
    """
    # get the scaling matrices
    Sx = np.array([[x, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    Sy = np.array([[1, 0, 0, 0],
                   [0, y, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    Sz = np.array([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, z, 0],
                   [0, 0, 0, 1]])
    
    scaling =  Sx*Sy*Sz
    final_coord = np.dot(scaling, coord)
    return final_coord
    # return the scaling transformation matrix
    


"""Function that returns the transformation matrix for a given shearing in x, y, and z"""


def shearingMatrix(x, y, z):
    """
    Returns the transformation matrix for a cube with a given shearing in x, y, and z
    """
    # get the shearing matrices
    Sx = np.array([[1, 0, 0, 0],
                   [y, 1, 0, 0],
                   [z, 0, 1, 0],
                   [0, 0, 0, 1]])
    Sy = np.array([[1, x, 0, 0],
                   [0, 1, 0, 0],
                   [0, z, 1, 0],
                   [0, 0, 0, 1]])
    Sz = np.array([[1, 0, x, 0],
                   [0, 1, y, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

    # return the shearing transformation matrix
    return Sx*Sy*Sz


"""Function that returns the transformation matrix for a given reflection in x, y, and z"""


def reflectionMatrix(x, y, z):
    """
    Returns the transformation matrix for a cube with a given reflection in x, y, and z
    """
    # get the reflection matrices
    Rx = np.array([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    Ry = np.array([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    Rz = np.array([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

    # get the reflection matrices
    if x == 1:
        Rx = np.array([[-1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    if y == 1:
        Ry = np.array([[1, 0, 0, 0],
                       [0, -1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    if z == 1:
        Rz = np.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, -1, 0],
                       [0, 0, 0, 1]])

    # return the reflection transformation matrix
    return Rx*Ry*Rz

x_list = []
y_list = []
z_list = []
w_list = []

n = int(input("Masukkan jumlah titik yang akan ditransformasi: "))
for i in range(n):
    print("Masukkan koordinat titik ke-", i+1)
    x_list.append(int(input("X = ")))
    y_list.append(int(input("Y = ")))
    z_list.append(int(input("Z = ")))
    w_list.append(1)

    
coord = []
coord.append(x_list)
coord.append(y_list)
coord.append(z_list)
coord.append(w_list)

final_coord = coord
lanjut = True
while lanjut == True:
    print("Pilih metode transformasi yang ingin dilakukan : \n1. Translasi \n2. Scaling \n3. Rotasi \n4. Shear")
    methode = int(input("pilih sesuai nomor \n"))
    if methode == 1:
        x = int(input("geser x sejauh : "))
        y = int(input("geser y sejauh : "))
        z = int(input("geser z sejauh : "))
        final_coord = translationMatrix(final_coord, x, y, z)
    elif methode == 2:
        x = int(input("scale x sebanyak : "))
        y = int(input("scale y sebanyak : "))
        z = int(input("geser z sebanyak : "))
        final_coord = scalingMatrix(final_coord, x, y, z)
    elif methode == 3:
        print("pilih sumbu rotasi yang ingin dilakukan : \n1. x \n2. y \n3. z")
        axis = int(input("pilih sesuai nomor \n"))
        degree = int(input("putar sebanyak (derajat): "))
        x = int(input("titik pusat x : "))
        y = int(input("titik pusat y : "))
        z = int(input("titik pusat z : "))
        if axis == 1:
            rotationMatrix(x, y)
        elif axis == 2:
            rotationMatrix(y, z)
        elif axis == 3:
            rotationMatrix(y, z)
    elif methode == 4:
        print("pilih sumbu shear yang ingin dilakukan : \n1. xy \n2. yz \n3. xz")
        shear = int(input("pilih sesuai nomor \n"))
        if shear == 1 or shear == 3:
            x = int(input("shear x sebesar : "))
        if shear == 1 or shear == 2:
            y = int(input("shear y sebesar : "))
        if shear == 2 or shear == 3:
            z = int(input("shear z sebesar : "))

        if axis == 1:
            shearingMatrix(x, y)
        elif axis == 2:
            shearingMatrix(y, z)
        elif axis == 3:
            shearingMatrix(x, z)

    print("matrix hasil transformasi : \n", final_coord)

    # Creating figure
    fig = plt.figure(figsize=(10, 7))
    ax = plt.axes(projection="3d")

    # Creating plot
    ax.scatter3D(final_coord[0], final_coord[1],
                final_coord[2], color="green")
    plt.title("simple 3D scatter plot")

    # show plot
    plt.show(block=True)

    state = input("Ulangi transformasi? (y/n)")
    if state == "y":
        lanjut = True
    elif state == "n":
        lanjut = False
