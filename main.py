from input import from_txt
from laplace import LT
from graph import graph,branch
from matrix import matrices,reorder
from final_calc import calculate
import numpy as np
np.set_printoptions(linewidth=np.inf)
import sympy as sp

t=sp.Symbol('t')
s=sp.Symbol('s')

R_list,C_list,L_list,V_list,I_list,branch_src_list,branch_dest_list=from_txt('test_data.txt')
g=graph()
g.generate(branch_src_list,branch_dest_list)
g.generate_matrix()
t=g.generate_tree()
l=g.get_links()
loops=g.get_loops()
print(loops)
R_list,L_list,C_list,V_list,I_list=reorder(g,R_list,C_list,L_list,V_list,I_list,branch_src_list,branch_dest_list)
R_LT,C_LT,L_LT,V_LT,I_LT=LT(R_list,C_list,L_list,V_list,I_list,branch_src_list,branch_dest_list)
B_f,Q_f,Z,Y=matrices(t,loops,R_LT,C_LT,L_LT)
V,I=calculate(B_f,Q_f,Z,Y,V_LT,I_LT,len(g.tree))
