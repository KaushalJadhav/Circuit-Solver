import sympy as sp
import numpy as np
from sympy.matrices import Matrix
from input import correct_VI

def combine(l1,l2):
    return list(map(lambda x, y:(min(x,y),max(x,y)), l1, l2))

def B_t(tree,loop):
    b=len(tree)+len(loop)
    n=len(tree)
    mat=np.zeros((b-n,n),dtype=int)
    for i in range(len(loop)):
        for j in range(len(tree)):
            mat[i][j]=tree[j].get_dir(loop[i])
    return mat

def B_f(mat):
    return np.concatenate((mat,np.eye(mat.shape[0],dtype=int)),axis=1)

def Q_f(B_t):
    Q_l=-B_t.transpose()
    Q_l=Q_l.astype(int)
    return np.concatenate((np.eye(Q_l.shape[0],dtype=int),Q_l),axis=1)

def create_list(src,g,list):
    src=src.copy()
    l=[]
    for b in g.tree:
        for c in range(len(src)):
            if b[0]==src[c][0] and b[1]==src[c][1]:
                l.append(list[c])
                del src[c]
                del list[c]
                break
    for b in g.links:
        for c in range(len(src)):
            if b[0]==src[c][0] and b[1]==src[c][1]:
                l.append(list[c])
                del src[c]
                del list[c]
                # print(R_list)
                break
    return l


def RLCVI(src,g,R_list,L_list,C_list,V_list,I_list):
    # RLC lists modified according to dest
    # R_list=R_list.tolist()
    # C_list=C_list.tolist()
    # L_list=L_list.tolist()
    # V_list=V_list.tolist()
    # I_list=I_list.tolist()
    # print(R_list)
    # print(C_list)
    # print(L_list)
    R=create_list(src,g,R_list)
    L=create_list(src,g,L_list)
    C=create_list(src,g,C_list)
    V=create_list(src,g,V_list)
    I=create_list(src,g,I_list)
    # R=Matrix(R)
    # L=Matrix(L)
    # C=Matrix(C)
    # V=Matrix(V)
    # I=Matrix(I)
    return R,L,C,V,I

def reorder(g,R_list,C_list,L_list,V_list,I_list,branch_src_list,branch_dest_list):
    V_list,I_list=correct_VI(V_list,I_list,branch_src_list,branch_dest_list)
    temp=combine(branch_src_list,branch_dest_list)
    return RLCVI(temp,g,R_list,L_list,C_list,V_list,I_list)

def reciprocal(a):
    if a==0:
        return a
    return 1/a

def generate_Z(R_list,C_list,L_list):
    Z=Matrix(len(R_list),len(R_list),lambda i,j: R_list[i]+C_list[i]+L_list[i] if i==j else 0)
    return Z

def generate_Y(R_list,C_list,L_list):
    Y=Matrix(len(R_list),len(R_list),lambda i,j: reciprocal(R_list[i])+reciprocal(C_list[i])+reciprocal(L_list[i]) if i==j else 0)
    return Y 

def matrices(tree,loop,R_list,C_list,L_list):
    '''
    Returns (B_f,Q_f,Z_f,Y_f)
    '''
    Bt=B_t(tree,loop)
    B_mat=B_f(Bt)
    Z=generate_Z(R_list,C_list,L_list)
    Y=generate_Y(R_list,C_list,L_list)
    return (B_mat,Q_f(Bt),Z,Y)


