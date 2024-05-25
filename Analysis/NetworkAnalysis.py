import math 

def s_res(r1,r2):
    return r1 + r2

def p_res(r1,r2):
    return (r1 * r2)/(r1 + r2)

def s_cap(c1,c2):
    return (c1 * c2)/(c1 + c2)

def p_cap(c1,c2):
    return c1+c2

def s_ind(l1,l2):
    return l1 + l2

def p_ind(l1,l2):
    return (l1 * l2)/ (l1 + l2)

def vdr2(V,e1,e2):
    Ve1 = (e1/(e1+e2) ) * V
    Ve2 = (e2/(e1+e2) ) * V
    return Ve1 , Ve2

def vdr3(V,e1,e2,e3):
    Ve1 = (e1/(e1+e2+e3)) * V
    Ve2 = (e2/(e1+e2+e3)) * V
    Ve3 = (e3/(e1+e2+e3)) * V
    return Ve1 , Ve2 , Ve3

def cdr2(i,e1,e2):
    ie1 = (e2 / (e1+e2))*i
    ie2 = (e1 / (e1+e2))*i
    return ie1 , ie2

def cdr3(i,e1,e2,e3):
    e1_opp = p_res(e2,e3)
    e2_opp = p_res(e1,e3)
    e3_opp = p_res(e1,e3)
    
    ie1 = (e1_opp / ( e1_opp + e1)) * i
    ie2 = (e2_opp / ( e2_opp + e2)) * i
    ie3 = (e3_opp / ( e3_opp + e3)) * i
    return ie1 , ie2, ie3

def Vc(Vo,C,R,t):
    C = C/1000000 #Converting to micro
    tau = R * C
    return (Vo * math.pow(math.exp(1), -1 *( t / (tau)))) * 1000

def IL(io,L,R,t):
    L = L/1000  #Converting to mili
    tau = L / R
    print(tau)
    return (io * math.pow(math.exp(1), -1 *( t / (tau)))) * 1000000


