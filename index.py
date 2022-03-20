# from graphics import *
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
    p = ([0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0])
    p = np.dot(Ti, Rxi)
    p = np.dot(p, Ryi)
    p = np.dot(p, Rz)
    p = np.dot(p, Ry)
    p = np.dot(p, Rx)
    p = np.dot(p, T)
    return p


"""Function that returns the transformation matrix for a given translation in x, y, and z"""
def translationMatrix(x, y, z):
    """
    Returns the transformation matrix for a cube with a given translation in x, y, and z
    """
    # get the translation matrices
    Tx = np.array([[1, 0, 0, x],
                   [0, 1, 0, y],
                   [0, 0, 1, z],
                   [0, 0, 0, 1]])
    return Tx


"""Function that returns the transformation matrix for a given scaling in x, y, and z"""
def scalingMatrix(x, y, z):
    """
    Returns the transformation matrix for a cube with a given scaling in x, y, and z
    """
    # get the scaling matrices
    S = np.array([[x, 0, 0, 0],
                   [0, y, 0, 0],
                   [0, 0, z, 0],
                   [0, 0, 0, 1]])
    # return the scaling transformation matrix
    return S


"""Function that returns the transformation matrix for a given shearing in x, y, and z"""
def shearingMatrix(x, y, z):
    """
    Returns the transformation matrix for a cube with a given shearing in x, y, and z
    """
    # get the shearing matrices
    if(x==0):
        S = np.array([[1, 0, 0, 0],
                   [y, 1, 0, 0],
                   [z, 0, 1, 0],
                   [0, 0, 0, 1]])
    if(y==0):
        S = np.array([[1, x, 0, 0],
                   [0, 1, 0, 0],
                   [0, z, 1, 0],
                   [0, 0, 0, 1]])
    if(z==0):
        S = np.array([[1, 0, x, 0],
                   [0, 1, y, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

    # return the shearing transformation matrix
    return S


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
    print("this is final_coord ")
    print(final_coord)
    print("Pilih metode transformasi yang ingin dilakukan : \n1. Translasi \n2. Scaling \n3. Rotasi \n4. Rotasi dengan arbitrari axis \n5.Shear")
    methode = int(input("Pilih sesuai nomor \n"))
    if methode == 1:
        print("Anda memilih metode translasi.\n")
        x = int(input("Geser x sejauh : "))
        y = int(input("Geser y sejauh : "))
        z = int(input("Geser z sejauh : "))
        final_coord = np.dot(translationMatrix(x, y, z),final_coord)
    elif methode == 2:
        print("Anda memilih metode scaling.\n")
        x = int(input("scale x sebanyak : "))
        y = int(input("scale y sebanyak : "))
        z = int(input("scale z sebanyak : "))
        final_coord = np.dot(scalingMatrix(x, y, z),final_coord)
    elif methode == 3:
        print("Anda memilih metode rotasi.\n")
        print("Tentukan sumbu rotasi yang ingin dilakukan : \n1. x \n2. y \n3. z")
        axis = int(input("Pilih sesuai nomor \n"))
        t = int(input("Tentukan sudut putar (dalam satuan derajat): "))
        if axis == 1:
            final_coord = np.dot(rotationMatrix(t, 0,0), final_coord)
        elif axis == 2:
            final_coord = np.dot(rotationMatrix(0,t, 0), final_coord)
        elif axis == 3:
            final_coord = np.dot(rotationMatrix(0,0,t), final_coord)
    elif methode == 4:
        print("Anda memilih metode rotasi terhadap arbitrari axis.\n")
        print("Masukan dua koordinat untuk garis axis rotasi: ")
        print("Masukkan koordinat titik ke-1")
        xo=(int(input("X = ")))
        yo=(int(input("Y = ")))
        zo=(int(input("Z = ")))
        print("Masukkan koordinat titik ke-2")
        xp=(int(input("X = ")))
        yp=(int(input("Y = ")))
        zp=(int(input("Z = ")))
        degree = int(input("Tentukan sudut putar (dalam satuan derajat): "))
        final_coord = np.dot(rotationMatrixAboutAxis(xo, yo, zo, xp, yp, zp,degree), final_coord)
    elif methode == 5:
        print("Anda memilih metode shearing.\n")
        print("Tentukan sumbu shear yang ingin dilakukan : \n1. xy \n2. yz \n3. xz")
        shear = int(input("Pilih sesuai nomor \n"))
        if shear == 1 or shear == 3:
            x = int(input("Shear x sebesar : "))
        if shear == 1 or shear == 2:
            y = int(input("Shear y sebesar : "))
        if shear == 2 or shear == 3:
            z = int(input("Shear z sebesar : "))

        if shear == 1:
            final_coord= np.dot(shearingMatrix(x, y,0),final_coord)
        elif shear == 2:
            final_coord =  np.dot(shearingMatrix(0,y, z), final_coord)
        elif shear == 3:
            final_coord= np.dot(shearingMatrix(x,0, z),final_coord)

    print("Matrix hasil transformasi : \n", final_coord)

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
