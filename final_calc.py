import sympy as sp
import numpy as np
from sympy.matrices import Matrix
import warnings
from functools import reduce

from sympy.tensor.functions import shape
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def getMatrixMinor(m,i,j):
    return m.minor_submatrix(i,j)

def det(m):
    #base case for 2x2 matrix
    if m.shape[0] == 2:
        return m[0,0]*m[1,1]-m[0,1]*m[1,0]

    determinant = 0
    for c in range(m.shape[0]):
        determinant += ((-1)**c)*m[0,c]*det(getMatrixMinor(m,0,c))
        determinant =sp.expand(determinant)
    return determinant

def inv(m):
    d=det(m)
    mat=sp.zeros(m.shape[0],m.shape[1])
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            mat[i,j]=det(getMatrixMinor(m,i,j))*(-1**(i+j))
            mat[i,j]=sp.expand(mat[i,j])
    mat=mat.T
    mat=mat/d
    return mat

def calculate(B,Q,Z,Y,Vg,Ig,n):
    s=sp.Symbol('s')
    Vg=Matrix(Vg)
    Vgt=Matrix(Vg[0:n])
    Vgl=Matrix(Vg[n:])
    Ig=Matrix(Ig)
    Igt=Matrix(Ig[0:n])
    Igl=Matrix(Ig[n:])
    Bf=Matrix(B)
    Qf=Matrix(Q)
    Zf=Bf*Z*Bf.T
    E=Bf*(Vg+Z*Bf.T*Igl-Z*Ig)
    Il=(inv(Zf))*E
    I=Bf.T*Il
    Yf=Qf*Y*Qf.T
    J=Qf*(Ig+Y*Qf.T*Vgt-Y*Vg)
    Vt=(inv(Yf))*J
    V=Qf.T*Vt
    return V,I