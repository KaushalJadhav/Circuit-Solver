import sympy as sp
import numpy as np
from sympy.matrices import Matrix

def calculate(B,Q,Z,Y,Vg,Ig,n):
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
    Il=(Zf**-1)*E
    I=Bf.T*Il
    Yf=Qf*Y*Qf.T
    J=Qf*(Ig+Y*Qf.T*Vgt-Y*Vg)
    Vt=(Yf**-1)*J
    V=Qf.T*Vt
    return V,I

def calculate_partial_fractions(exp):
    return sp.apart(exp)