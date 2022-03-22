# Tugas Teknik Visualisasi Grafis Transformasi 3D Kelompok 13
# Anggota:
# 1. Iskan Mustamir             (20/456367/TK/50497)
# 2. M. Fatin Abimanyu          (20/456844/TK/50668)
# 3. M. Iqbal Reza Riandani     (20/460549/TK/51138)
# 4. Vira Ayu Oktaviani         (20/460570/TK/51159)
# 5. Mufidus Sani               (20/463608/TK/51600)

import math as m
import numpy as np
from graphics import *
from time import sleep

class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def rotationX(self, degree):
        # get rotation about x axis
        a = m.radians(degree)
        Rx = np.array([[1, 0, 0, 0],
                       [0, m.cos(a), -m.sin(a), 0],
                       [0, m.sin(a), m.cos(a), 0],
                       [0, 0, 0, 1]])
        hasil = np.dot(Rx, [self.x, self.y, self.z, 1])
        return Point3D(hasil[0], hasil[1], hasil[2])

    def rotationY(self, degree):
        # get rotation about y axis
        a = m.radians(degree)
        Ry = np.array([[m.cos(a), 0, m.sin(a), 0],
                       [0, 1, 0, 0],
                       [-m.sin(a), 0, m.cos(a), 0],
                       [0, 0, 0, 1]])
        hasil = np.dot(Ry, [self.x, self.y, self.z, 1])
        return Point3D(hasil[0], hasil[1], hasil[2])

    def rotationZ(self, degree):
        # get rotation about z axis
        a = m.radians(degree)
        Rz = np.array([[m.cos(a), -m.sin(a), 0, 0],
                       [m.sin(a), m.cos(a), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
        hasil = np.dot(Rz, [self.x, self.y, self.z, 1])
        return Point3D(hasil[0], hasil[1], hasil[2])

    def rotationMatrixAboutAxis(self, x, y, z, xp, yp, zp, degree):
        # get rotation about axis matrices
        hasil = np.array([self.x, self.y, self.z, 1])
        if x != 0 or y != 0 or z != 0 or xp != 0 or yp != 0 or zp != 0:
            A, B, C = xp - x, yp - y, zp - z
            a = A/m.sqrt(A**2+B**2+C**2)
            b = B/m.sqrt(A**2+B**2+C**2)
            c = C/m.sqrt(A**2+B**2+C**2)
            v = m.sqrt(b**2+c**2)
            r = m.radians(degree)

            T = np.array([[1, 0, 0, -x],
                          [0, 1, 0, -y],
                          [0, 0, 1, -z],
                          [0, 0, 0, 1]])
            Ti = np.array([[1, 0, 0, x],
                           [0, 1, 0, y],
                           [0, 0, 1, z],
                           [0, 0, 0, 1]])
            Rx = np.array([[1, 0, 0, 0],
                           [0, m.cos(r), -m.sin(r), 0],
                           [0, m.sin(r), m.cos(r), 0],
                           [0, 0, 0, 1]])
            Rxi = np.array([[1, 0, 0, 0],
                            [0, m.cos(r), -m.sin(r), 0],
                            [0, m.sin(r), m.cos(r), 0],
                            [0, 0, 0, 1]])
            Ry = np.array([[v, 0, -a, 0],
                           [0, 1, 0, 0],
                           [a, 0, v, 0],
                           [0, 0, 0, 1]])
            Ryi = np.array([[v, 0, a, 0],
                            [0, 1, 0, 0],
                            [-a, 0, v, 0],
                            [0, 0, 0, 1]])
            Rz = np.array([[m.cos(r), -m.sin(r), 0, 0],
                           [m.sin(r), m.cos(r), 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])

            p = Ti * Rxi * Ryi * Rz * Ry * Rx * T

            hasil = np.dot(p, [self.x, self.y, self.z, 1])
        return Point3D(hasil[0], hasil[1], hasil[2])

    def translationMatrix(self, x, y, z):
        # get the translation matrices
        Tx = np.array([[1, 0, 0, x],
                       [0, 1, 0, y],
                       [0, 0, 1, z],
                       [0, 0, 0, 1]])
        hasil = np.dot(Tx, [self.x, self.y, self.z, 1])
        return Point3D(hasil[0], hasil[1], hasil[2])

    def scalingMatrix(self, x, y, z):
        # get the scaling matrices
        Sc = np.array([[x, 0, 0, 0],
                       [0, y, 0, 0],
                       [0, 0, z, 0],
                       [0, 0, 0, 1]])
        # return the scaling transformation matrix
        hasil = np.dot(Sc, [self.x, self.y, self.z, 1])
        return Point3D(hasil[0], hasil[1], hasil[2])

    def shearingMatrix(self, x, y, z):
        # get sharing matrices
        Sh = [[0]*4]*4
        if(x == 0):
            Sh = np.array([[1, 0, 0, 0],
                           [0, y, 0, 0],
                           [0, z, 1, 0],
                           [0, 0, 0, 1]])
        elif(y == 0):
            Sh = np.array([[x, 0, 0, 0],
                           [0, 1, 0, 0],
                           [z, 0, 1, 0],
                           [0, 0, 0, 1]])
        elif(z == 0):
            Sh = np.array([[1, 0, x, 0],
                           [0, 1, y, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
        else:
            Sh = np.array([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])

        hasil = np.dot(Sh, [self.x, self.y, self.z, 1])
        return Point3D(hasil[0], hasil[1], hasil[2])

    def project(self, win_width, win_height, fov, viewer_distance):
        # visualize 3d to 2d
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, 1)

class Program:
    def __init__(self):
        self.faces = [(0, 1, 2, 3), (1, 5, 6, 2), (5, 4, 7, 6),
                      (4, 0, 3, 7), (0, 4, 5, 1), (3, 2, 6, 7)]

        self.vertices = [
            Point3D(-5,3,-2), 
            Point3D(5,3,-2),
            Point3D(5,-3,-2),
            Point3D(-5,-3,-2),
            Point3D(-5,3,2),
            Point3D(5,3,2),
            Point3D(5,-3,2),
            Point3D(-5,-3,2)
        ]

        self.line1 = [[], [], [], [], [], []]
        self.line2 = [[], [], [], [], [], []]
        self.line3 = [[], [], [], [], [], []]
        self.line4 = [[], [], [], [], [], []]

        self.degreeX, self.degreeY, self.degreeZ = 0, 0, 0
        self.transX, self.transY, self.transZ = 0, 0, 0
        self.scaleX, self.scaleY, self.scaleZ = 1, 1, 1
        self.shearX, self.shearY, self.shearZ = 1, 1, 1
        self.arbX, self.arbY, self.arbZ = 0, 0, 0
        self.arbXP, self.arbYP, self.arbZP = 0, 0, 0
        self.degreeArb = 0
        self.cond = 0

    def transformation(self, w, degree, mode, changeX=0, changeY=0, changeZ=0, xp=0, yp=0, zp=0):
        x, y, z = 0, 0, 0
        if mode == 'rotationX':
            x = 1
            if degree < 0:
                x = -1
        elif mode == 'rotationY':
            y = 1
            if degree < 0:
                y = -1
        elif mode == 'rotationZ':
            z = 1
            if degree < 0:
                z = -1
        elif mode == 'scaling':
            self.scaleX *= changeX
            self.scaleY *= changeY
            self.scaleZ *= changeZ
        elif mode == 'shearing':
            self.shearX = changeX
            self.shearY = changeY
            self.shearZ = changeZ
        elif mode == 'rotationArbitrary':
            self.arbX = changeX
            self.arbY = changeY
            self.arbZ = changeZ
            self.arbXP = xp
            self.arbYP = yp
            self.arbZP = zp

            arb = 1
            if degree < 0:
                arb = -1

        for i in range(abs(degree)):
            sleep(0.01)

            if mode == 'rotationX' or mode == 'rotationY' or mode == 'rotationZ':
                self.degreeX += x
                self.degreeY += y
                self.degreeZ += z
            elif mode == 'translation':
                self.transX += changeX/degree
                self.transY += changeY/degree
                self.transZ += changeZ/degree
            elif mode == 'rotationArbitrary':
                self.degreeArb += arb

            t = []
            gx = 0

            for v in self.vertices:
                r = v.rotationX(self.degreeX).rotationY(self.degreeY).rotationZ(self.degreeZ).translationMatrix(self.transX, self.transY, self.transZ).scalingMatrix(
                    self.scaleX, self.scaleY, self.scaleZ).shearingMatrix(self.shearX, self.shearY, self.shearZ).rotationMatrixAboutAxis(self.arbX, self.arbY, self.arbZ, self.arbXP, self.arbYP, self.arbZP, self.degreeArb)
                p = r.project(1280, 720, 500, 15)
                t.append(p)

            if(self.cond == 1):
                for i in range(6):
                    self.line1[i].undraw()
                    self.line2[i].undraw()
                    self.line3[i].undraw()
                    self.line4[i].undraw()
            else:
                self.cond = 1

            for f in self.faces:
                self.line1[gx] = Line(Point(t[f[0]].x, t[f[0]].y), Point(t[f[1]].x, t[f[1]].y))
                self.line2[gx] = Line(Point(t[f[1]].x, t[f[1]].y), Point(t[f[2]].x, t[f[2]].y))
                self.line3[gx] = Line(Point(t[f[2]].x, t[f[2]].y), Point(t[f[3]].x, t[f[3]].y))
                self.line4[gx] = Line(Point(t[f[3]].x, t[f[3]].y), Point(t[f[0]].x, t[f[0]].y))
                self.line1[gx].setFill('black')
                self.line2[gx].setFill('black')
                self.line3[gx].setFill('black')
                self.line4[gx].setFill('black')
                self.line1[gx].draw(w)
                self.line2[gx].draw(w)
                self.line3[gx].draw(w)
                self.line4[gx].draw(w)
                gx += 1

    def run(self):
        w = GraphWin("Plot 3D Balok", 1280, 720)
        w.setBackground('white')
        i = 0
        x_input = []
        y_input = []
        z_input = []

        Program.transformation(self, w, 1, '')

        print("Program Transformasi 3D pada Balok")
        print("Ukuran awal: Balok 4x2x2 dengan Pusat 0, 0, 0")
        print("Titik balok pada kondisi awal:\nA(-5, 3, -2)\nB(5, 3, -2)\nC(5, -3, -2)\nD(-5, -3, -2)\nE(-5, 3, 2)\nF(5, 3, 2)\nG(5, -3, 2)\nH(-5, -3, 2)")

        initial = input("Gunakan koordinat titik balok pada kondisi awal? (y/n) : ")
        if initial == 'n':
            for i in range(2):
                print("Masukkan koordinat titik ujung balok ke-", i+1)
                x_input.append(float(input("X = ")))
                y_input.append(float(input("Y = ")))
                z_input.append(float(input("Z = ")))
            self.vertices = [
                Point3D(x_input[0], y_input[0], z_input[0]),
                Point3D(x_input[0], y_input[1], z_input[0]),
                Point3D(x_input[1], y_input[1], z_input[0]),
                Point3D(x_input[1], y_input[0], z_input[0]),
                Point3D(x_input[0], y_input[0], z_input[1]),
                Point3D(x_input[0], y_input[1], z_input[1]),
                Point3D(x_input[1], y_input[1], z_input[1]),
                Point3D(x_input[1], y_input[0], z_input[1])
            ]
            Program.transformation(self, w, 1, '')

        lanjut = True
        while lanjut == True:
            print("Pilih metode transformasi yang ingin dilakukan : \n1. Translasi \n2. Scaling \n3. Rotasi \n4. Rotasi dengan arbitrari axis \n5. Shear")
            methode = int(input("Pilih sesuai nomor : "))
            if methode == 1:
                print("Anda memilih metode translasi.")
                x = float(input("Geser x sejauh : "))
                y = float(input("Geser y sejauh : "))
                z = float(input("Geser z sejauh : "))
                Program.transformation(self, w, 10, 'translation', x, y, z)

            elif methode == 2:
                print("Anda memilih metode scaling.")
                x = float(input("Scale x sebanyak : "))
                y = float(input("Scale y sebanyak : "))
                z = float(input("Scale z sebanyak : "))
                Program.transformation(self, w, 1, 'scaling', x, y, z)

            elif methode == 3:
                print("Anda memilih metode rotasi.")
                print(
                    "Tentukan sumbu rotasi yang ingin dilakukan : \n1. x \n2. y \n3. z")
                axis = input("Pilih sesuai nomor atau sumbu : ")
                degree = int(
                    input("Tentukan sudut putar (dalam satuan derajat dan gunakan nilai negatif apabila sudut putar rotasi searah jarum jam): "))
                if axis == '1' or axis == 'x':
                    Program.transformation(self, w, degree, 'rotationX')
                elif axis == '2' or axis == 'y':
                    Program.transformation(self, w, degree, 'rotationY')
                elif axis == '3' or axis == 'z':
                    Program.transformation(self, w, degree, 'rotationZ')

            elif methode == 4:
                print("Anda memilih metode rotasi terhadap arbitrari axis.\n")
                print("Masukan dua koordinat untuk garis axis rotasi : ")
                print("Masukkan koordinat titik ke-1")
                xo = (int(input("X = ")))
                yo = (int(input("Y = ")))
                zo = (int(input("Z = ")))
                print("Masukkan koordinat titik ke-2")
                xp = (int(input("X = ")))
                yp = (int(input("Y = ")))
                zp = (int(input("Z = ")))
                degree = int(input("Tentukan sudut putar (dalam satuan derajat dan gunakan nilai negatif apabila sudut putar rotasi searah jarum jam) : "))
                Program.transformation(self, w, degree, 'rotationArbitrary', xo, yo, zo, xp, yp, zp)

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
                    Program.transformation(self, w, 1, 'shearing', x, y, 0)
                elif shear == 2:
                    Program.transformation(self, w, 1, 'shearing', 0, y, z)
                elif shear == 3:
                    Program.transformation(self, w, 1, 'shearing', x, 0, z)

            state = input("Input Transformasi lain? (y/n) : ")
            if state == "y":
                lanjut = True
            elif state == "n":
                print("Terima kasih telah menggunakan program ini.")
                lanjut = False

Program().run()