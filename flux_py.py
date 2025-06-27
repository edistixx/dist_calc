# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import pandas as pd
from sympy import * 
data_d = pd.read_excel("comp_data2.xlsx")
data_d.head(3)

# %%
M = data_d.MM.values
em3 = data_d[["GAS","Symbol"]].values
Tc_data = data_d["Tc K"].values
Pc_data = data_d["Pc Mpa"].values
Vc_data = data_d["Vc m3/kmol"].values
Vel_data = data_d["atomic_volume"].values
dens = data_d["density"].values


# %%
c1 = "water"
c2 = "air"
A = np.where(em3[:,0] == c1.lower())[0][0] # Parameter-index extraction
B = np.where(em3[:,0] == c2.lower())[0][0] # user selects these two from a drop down or must type it


# %%
def dab_find(Ti,Pi,c1,c2,corr):
  
    A = np.where((em3[:,0] == c1.lower()) | (em3[:,1] == c1))[0][0] # Parameter-index extraction
    B = np.where((em3[:,0] == c2.lower()) | (em3[:,1] == c2))[0][0] # user selects these two from a drop down or must type it
    T = Ti
    P = Pi
    compA = em3[A,1];
    compB = em3[B,1];
    M_A = M[A]; #mol formula of selected compound
    M_B = M[B];
    rho_A = dens[A]
    rho_B = dens[B]
        
    K = 5.670367*10e-8
        
    #Parameter evaluation for Chapman and wilke lee
        
    Tc_A = Tc_data[A];
    Tc_B = Tc_data[B];
    Pc_A = Pc_data[A];
    Pc_B = Pc_data[B];
    Vc_A = Vc_data[A];
    Vc_B = Vc_data[B];
        
    e_A = K*0.75*Tc_A;
    e_B = K*0.75*Tc_B;
    e_AB = np.sqrt(e_A*e_B);
        
    sigmaA = (5/6)*((Vc_A)**(1/3))*10;
    sigmaB = (5/6)*((Vc_B)**(1/3))*10;
    sigmaAB = (sigmaA+sigmaB)/2;
    T_star = (K*T)/e_AB;
    
    C = [1.06036,0.15610,0.19300,0.47635,1.03587,1.52996,1.76474,3.89411]; #a-h cosntants
    
    ohm_D = ((C[0])/(T_star)**C[1]) + ((C[2])/(np.exp(C[3]*T_star))) + ((C[4])/(np.exp(C[5]*T_star))) + ((C[6])/(np.exp(C[7]*T_star)));
    # chapman
    DAB_ch = ((1.858*10**-7)*(T**(1.5))*((1/M_A) + (1/M_B))**0.5)/(P*(sigmaAB**2)*ohm_D);
    #wilke-lee
    MAB = 2*((1/M_A) + (1/M_B))**(-1);
    DAB_w = (((3.03 - ((0.98)/(MAB**0.5)))*(10**-3)*T**(3/2))/(P*1.013*(MAB**0.5)*(sigmaAB**2)*ohm_D))*10**(-4);
    #fuller
    sig_VA = Vel_data[A];
    sig_VB = Vel_data[B];
    DAB_F = ( (1.0133*10**(-7))*T**(1.75)*((1/M_A) + (1/M_B))**(0.5))/(P*(sig_VA**(1/3) + sig_VB**(1/3))**(2));
    res = np.array([DAB_ch,DAB_w,DAB_F])
    return res[corr]   


# %%
DAB = dab_find( 298.2, 1.013,"air","H2O",0)
DAB


# %%
#Dc - diffusing comp 
def gen(Ti=298.2,P= 1.013,c1="air",c2="H2O",DC=1,corr=2,state=1,Case=1,z1_in=1,z2_in=1,Pa1_in=1,Pa2_in=1,a_in=2,areatype = 0,geo=0,sigma=1,Rs_in=1,Rsf_in=1,yi_in=1,yf_in=1):
    Dab_t = dab_find(Ti,P,c1,c2,corr)

    Ri = 8.314
    if Case == 0:
        
        z1i = z1_in
        z2i = z2_in
        Pa1i = Pa1_in
        Pa2i = Pa2_in
        
        z1,z2,z,Pa,Pt,Pa1,Pa2,R,T,Dab,Ct_avg,C_A1,C_A2 = symbols('z1,z2,z,Pa,Pt,Pa1,Pa2,R,T,Dab,Ct_avg,C_A1,C_A2')
        
        Na= symbols('Na',cls = Function)(z)
        ya = symbols('ya',cls = Function)(Pa)
        ya = Pa/Pt
        P_eq = simplify(Na-Mul(ya,Na))
        f_eq = Eq(Na*integrate(1,(z,z1,z2)),(-Dab/(R*T))*integrate(1/(P_eq.subs(Na,1)),(Pa,Pa1,Pa2))) ####################for gases
        feq2 = f_eq.subs({z1:z1i,z2:z2i,Pt:P*10**5,Pa1:Pa1i,Pa2:Pa2i,R:Ri,T:Ti,Dab:Dab_t}) ####################for gases
        NA_g = feq2.rhs/(feq2.lhs.subs({Na:1}))
        data = pd.DataFrame({"":["Flux","Diffusivity"]," ":[NA_g,Dab_t]})
        
    elif Case == 1:
        #case ii : equimolar counter 
        Pa1i = Pa1_in
        Pa2i = Pa2_in
        
        z1i = z1_in
        z2i = z2_in
        
        
        z1,z2,z,Pa,Pt,Pa1,Pa2,R,T,Dab = symbols('z1,z2,z,Pa,Pt,Pa1,Pa2,R,T,Dab')
        
        Na= symbols('Na',cls = Function)(z) ##it is a func of z because I'll integrate that with res to z
        ya = symbols('ya',cls = Function)(Pa)##it is a func of pa because I have to multiply it by Na in the subsequent equation, else I'll get an error
        # ya = Pa/Pt
        f_eq_e = Eq(Na*integrate(1,(z,z1,z2)),(-Dab/(R*T))*integrate(1,(Pa,Pa1,Pa2))) ####################for gases
        feq2_e = f_eq_e.subs({z1:z1i,z2:z2i,Pt:P*10**5,Pa1:Pa1i,Pa2:Pa2i,R:Ri,T:Ti,Dab:Dab_t})####################for gases
        NA_g = feq2_e.rhs/(feq2_e.lhs.subs({Na:1}))
        NA_g
        data = pd.DataFrame({"":["Flux","Diffusivity"]," ":[NA_g,Dab_t]})
    elif Case == 2:

        #case ii : non-equimolar counter 
      
        alpha = a_in
        
        Pa1i = Pa1_in
        Pa2i = Pa2_in
        
        z1i = z1_in
        z2i = z2_in
    
        
        
        a, z1,z2,z,Pa,Pt,Pa1,Pa2,R,T,Dab = symbols('a,z1,z2,z,Pa,Pt,Pa1,Pa2,R,T,Dab')
        
        Na= symbols('Na',cls = Function)(z) ##it is a func of z because I'll integrate that with res to z
        ya = symbols('ya',cls = Function)(Pa)##it is a func of pa because I have to multiply it by Na in the subsequent equation, else I'll get an error
        ya = Pa/Pt
        P_eq_ne = simplify(Na-Mul(ya,Na*(1-a)))
        f_eq_ne = Eq(Na*integrate(1,(z,z1,z2)),(-Dab/(R*T))*integrate(1/(P_eq_ne.subs(Na,1)),(Pa,Pa1,Pa2))) ####################for gases
        feq2_ne = f_eq_ne.subs({a:alpha,z1:z1i,z2:z2i,Pt:P*10**5,Pa1:Pa1i,Pa2:Pa2i,R:Ri,T:Ti,Dab:Dab_t}) ####################for gases
        NA_g = feq2_ne.rhs/(feq2_ne.lhs.subs({Na:1}))
        NA_g
        data = pd.DataFrame({"":["Flux","Diffusivity"]," ":[NA_g,Dab_t]})
        
    if areatype == 1 and Case == 0 and geo == 1: 
        
    # variable area
        # geometry = "Sphere"
        # Rs_in=1,Rsf_in=1
        Rsfi = Rsf_in
        P_infi = Pa2_in
        P_asi = Pa1_in
        Rsoi = Rs_in
        rh_A,Rs,R_inf,Pa,Pt,Pas,Pa_inf,t,Rso,Rsf,Dab,T,R,M_a,O = symbols('rh_A,Rs,R_inf,Pa,Pt,Pas,Pa_inf,t,Rso,Rsf,Dab,T,R,M_a,O')
        r,h = symbols('r,h')
        ya = symbols('ya',cls = Function)(Pa)
        # WL = symbols('WL',cls = Function)(t)
        WR = symbols('WR',cls = Function)(Rs)
        ya = Pa/Pt
        
        Na= symbols('Na',cls = Function)(r)
        W= symbols('W',cls = Function)(r)
        P_eq = simplify(Na-Mul(ya,Na))
        Area,V = symbols('Area,V',cls = Function)
        
        
        V = (4/3)*pi*r**3
        Area = diff(V,r)
        v_eq = Eq(W*integrate(1/r**2,(r,Rs,np.inf)),((Area/r**2)*-Dab/(R*T))*integrate(1/(P_eq.subs(Na,1)),(Pa,Pas,Pa_inf))) ####################for gases
        WL = v_eq.rhs/(simplify(v_eq.lhs.subs({W:1})))
        Area2 = Area.subs({r:Rs})
        t1 = Eq(((WL)/(4*pi*Rs)) * integrate(1,(t,0,t)),(-rh_A*1000/M_a)*integrate(((Area2)/(4*pi*Rs)),(Rs,Rso,Rsf)))
        t11 = t1.subs({Rsf:Rsfi,Rso:Rsoi,Pt:P*10**5,Pa_inf:P_infi,Pas:P_asi,Dab:Dab_t,rh_A:1140,M_a:128,R:Ri,T:Ti}) ###check
        t = (t11.rhs)/(t11.lhs.subs({t:1}))
        time = t/3600
        NA_g = 0
        data = pd.DataFrame({"":["Flux","Diffusivity","Time"]," ":[NA_g,Dab_t,time]})
    if areatype == 1 and Case == 0 and geo == 1: 
        
            Rsfi = Rsf_in
            P_infi = Pa2_in
            P_asi = Pa1_in
            Rsoi = Rs_in    

            rh_A,R_inf,Pa,Pt,Pas,Pa_inf,t,Rso,Rsf,Dab,T,R,M_a = symbols('rh_A,R_inf,Pa,Pt,Pas,Pa_inf,t,Rso,Rsf,Dab,T,R,M_a',positive=True)
            r,l = symbols('r,l',positive=True)
            Rs,O = symbols('Rs,O',positive=True)
            ya = symbols('ya',cls = Function)(Pa)
            # WL = symbols('WL',cls = Function)(t)
            WR = symbols('WR',cls = Function)(Rs)
            ya = Pa/Pt
            
            Na= symbols('Na',cls = Function)(r)
            W= symbols('W',cls = Function)(r)
            P_eq = simplify(Na-Mul(ya,Na))
            Area,V = symbols('Area,V',cls = Function)
            
            
            V = pi*r**2*l
            Area = diff(V,r)
            v_eq = Eq(W*logcombine(integrate((1/r),(r,Rs,(Rs + O)))),((Area/r)*-Dab/(R*T))*integrate(1/(P_eq.subs(Na,1)),(Pa,Pas,Pa_inf))) ####################for gases
            WL = v_eq.rhs/(simplify(v_eq.lhs.subs({W:1})))
            Area2 = Area.subs({r:Rs})
            t1 = Eq((WL*log((O + Rs)/(Rs)))/(2*pi*l*(-rh_A*1000/M_a)) * integrate(1,(t,0,t)),integrate(((Area2*log((O+Rs)/(Rs))))/(2*pi*l),(Rs,Rso,Rsf)))
            t11 = t1.subs({Rsf:Rsfi,Rso:Rsoi,Pt:P*10**5,Pa_inf:P_infi,Pas:P_asi,Dab:Dab_t,rh_A:1140,M_a:128,R:Ri,T:Ti,O:sigma})
            t = simplify((t11.rhs)/(t11.lhs.subs({t:1})))
           
            time =  t/3600
            data = pd.DataFrame({"":["Flux","Diffusivity","Time"]," ":[NA_g,Dab_t,time]})
# # integrate(v_eq,(r,Rs,0))
                
                
                

        

        
            
        
            
    return NA_g,Dab_t,data
        
        # # flux_eq1 = Eq(Na,((-Dab)/(R*T))*(diff(Pa,z)) + ya*(Na + N_s_comp))
        # # flux_eq1
                
            

# %%

x,y,i = gen(Ti=298.2,P=1.013,c1="air",c2="H2O",DC=1,corr=2,state=1,Case=0,z1_in=0,z2_in=2.5*10**-3,Pa1_in=0.00114*101325,Pa2_in=0,a_in=2,areatype = 1,geo=1,sigma=0.004,Rs_in=0.943*10**-2,Rsf_in=0.594*10**-2,yi_in=1,yf_in=1)


# %%


# %%

# %%

# %%

# %%

# %%

# %%

# %%
