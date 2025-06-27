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


# %%
data_d = pd.read_excel("comp_data2.xlsx")
data_d
def Dab(T,P,c1,c2,corr):
    
    M = data_d.MM.values
    em3 = data_d[["GAS","Symbol"]].values
    Tc_data = data_d["Tc K"].values
    Pc_data = data_d["Pc Mpa"].values
    Vc_data = data_d["Vc m3/kmol"].values
    Vel_data = data_d["atomic_volume"].values
    A = np.where(em3[:,0] == c1.lower())[0][0] # Parameter-index extraction
    B = np.where(em3[:,0] == c2.lower())[0][0] # user selects these two from a drop down or must type it

    compA = em3[A,1];
    compB = em3[B,1];
    M_A = M[A]; #mol formula of selected compound
    M_B = M[B];
    
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
  # wilke-lee
    MAB = 2*((1/M_A) + (1/M_B))**(-1);
    DAB_w = (((3.03 - ((0.98)/(MAB**0.5)))*(10**-3)*T**(3/2))/(P*1.013*(MAB**0.5)*(sigmaAB**2)*ohm_D))*10**(-4);
    #fuller
    sig_VA = Vel_data[A];
    sig_VB = Vel_data[B];
    DAB_F = ( (1.0133*10**(-7))*T**(1.75)*((1/M_A) + (1/M_B))**(0.5))/(P*(sig_VA**(1/3) + sig_VB**(1/3))**(2));
    res = np.array([DAB_ch,DAB_w,DAB_F])
    
    
    return res[[corr]],res


# %%

# %%

def mult_dab(T,P,corr,diff_spec,comp,frac):
    
    
    diff_free_comp = np.delete(comp,diff_spec)
    diff_free_frac = np.delete(frac,diff_spec)
    
    c1 = comp[diff_spec]
    
    D1_s = []
    # finding binary diffusivities
    for i in range(0,len(diff_free_comp)):
        c2 = diff_free_comp[i]
        D1_i,summary = Dab(T,P,c1,c2,corr)
        D1_s.append(D1_i)
    #finding y primes
    yps = []
    for i in range(0,len(diff_free_frac)):
        yn = diff_free_frac[i]
        ynp = yn/(1 - frac[diff_spec])
        yps.append(ynp)
    
    # finding D1mix
    den_ar = []
    for i in range(0,len(diff_free_frac)):
        denom = yps[i]/D1_s[i]
        den_ar.append(denom)
    
    Di_mix = 1/(np.sum(den_ar))
    dij = [comp[diff_spec] + "-" +i  for i in diff_free_comp ]
    D1_sl = np.array([D1_s[i][0] for i in range(0,len(D1_s))])
    
    
    return Di_mix,D1_sl,dij


# 

# %%

# %%

# %%
