from input import from_txt
from laplace import LT
from graph import graph,branch
from matrix import matrices,reorder
from final_calc import calculate
import numpy as np
np.set_printoptions(linewidth=np.inf)
from sympy.matrices import Matrix

R_list,C_list,L_list,V_list,I_list,branch_src_list,branch_dest_list=from_txt('test_data_2.txt')
# print(V_list,branch_src_list,branch_dest_list)
g=graph()
g.generate(branch_src_list,branch_dest_list)
g.generate_matrix()
t=g.generate_tree()
print(t)
l=g.get_links()
print(l)
loops=g.get_loops()
print(loops)
R_list,L_list,C_list,V_list,I_list=reorder(g,R_list,C_list,L_list,V_list,I_list,branch_src_list,branch_dest_list)
# print(V_list)
R_LT,C_LT,L_LT,V_LT,I_LT=LT(R_list,C_list,L_list,V_list,I_list,branch_src_list,branch_dest_list)
print(V_LT)
B_f,Q_f,Z,Y=matrices(t,loops,R_LT,C_LT,L_LT)
# print(I_LT)
# V,I=calculate(B_f,Q_f,Z,Y,V_LT,I_LT,len(g.tree))
# print(V)
# print(Y_f)
# print(B_f)
# print(Q_f)
# b=branch(1,3)
# print(b.get_dir(l[0]))
# print(b.get_dir(l[1]))
