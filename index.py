from graphics import *
import numpy as np
import math as m

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

    # return the scaling transformation matrix
    return Sx*Sy*Sz

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
