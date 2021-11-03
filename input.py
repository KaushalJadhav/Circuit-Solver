import pandas as pd
import itertools
import re


def check_float(string):
    try:
        float(string)
        return True
    except: 
        return False 



conv_dict={
           'T':1e12,
           'G':1e9,
           'g':1e9,
           'M':1e6,
           'MEG':1e6,
           'meg':1e6,
           'k':1e3,
           'K':1e3,
           'h':1e2,
           'H':1e2,
           'D':10,
           'std':1,
           'd':1e-1,
           'c':1e-2,
           'C':1e-2,
           'm':1e-3,
           'u':1e-6,
           'mu':1e-6,
           'n':1e-9,
           'p':1e-12,
           'f':1e-15,
           'fm':1e-15,
           }
  
def conv(value,from_unit,to_unit):
  try:
    return float(value)*(conv_dict[from_unit]/conv_dict[to_unit])
  except :
    raise KeyError('Unknown unit abbrevation ')

def convert(data,list):
 for d in data:
     d=str(d)
     if check_float(d):
        value=float(d)
     else:
         res = [''.join(grp) for _, grp in itertools.groupby(d, str.isalpha)]
         if len(res)==1:
             value=0
         elif len(res)==2:
             value=conv(res[0],res[1],'std')
         else:
             raise Exception("Error occurred in parsing")
     list.append(value)
 return list

def print_list(l):
    for item in l:
        print("{:.3e}".format(item))

def print_VI(l):
    for item in l:
        if len(item)==2:
            print("{:.3e}".format(item[0]))
        else:
            print("{:.3e},".format(item[0]),"{:.3e}<".format(item[1]),"{:.3e}".format(item[2]))

def convert_VI(data,list):
    chk=False
    for d in data:
     d=str(d)
     d=re.split(",|<",d)
     value=[]
     if len(d)==1:
         chk=True
     else:
         chk=False
     for V_I in d:
         if check_float(V_I):
             val=float(V_I)
         else:
             res = re.findall('\d*\.?\d+',V_I)
             if res:
                 res.append(V_I.replace(str(res[0]),''))
             else:
                 res=['-']
             if len(res)==1:
                 val=0
             elif len(res)==2:
                 val=conv(res[0],res[1],'std')
             else:
                 raise Exception("Error occurred in parsing")
         value.append(val)  
     if chk:
        value.append('DC')
     else:
      if V_I.find("<")==-1:
         value.append(0)
         value.append('AC')
      else:
         value.append('AC')
     if len(value)==5:
         value.pop(3)
     list.append(value)


def from_txt(file):
    X=pd.read_csv(file,sep=' ')
    R_list=[]
    C_list=[]
    L_list=[]
    V_list=[]
    I_list=[]
    branch_src_list=X['Branch_origin'].to_numpy()
    branch_dest_list=X['Branch_dest'].to_numpy()
    convert(X['R'],R_list)
    convert(X['C'],C_list)
    convert(X['L'],L_list)
    convert_VI(X['V'],V_list)
    convert_VI(X['I'],I_list)
    return R_list,C_list,L_list,V_list,I_list,branch_src_list,branch_dest_list

def correct_VI(V_list,I_list,branch_src_list,branch_dest_list):
    for i in range(len(branch_src_list)):
        if branch_dest_list[i]<branch_src_list[i]:
            V_list[i][0]=-V_list[i][0]
            I_list[i][0]=-I_list[i][0]
    return V_list,I_list
