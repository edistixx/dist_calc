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
data = pd.read_excel("mol_properties.xlsx")
data.head(10)


# %%

def results(P,F,Fv1,Lk_rec,Hk_rec,Lk_ind,Hk_ind,user_comps,q,R_int,min_ind):
                
        ant_const_arr = np.array([data.antoine_a.to_list(),data.antoine_b.to_list(),data.antoine_c.to_list()]).T
        molm = data.molar_weigth.to_list()
        em1 = data[["formula","compounds"]].values
        T_p = data["Tb(K)"]
        
        
        ind_comp = np.sort([np.where((em1[:,1] == i) | (em1[:,0] == i))[0][0] for i in user_comps])
        
        M_array = np.array(molm)[ind_comp]
        antoine_matrix = np.array(ant_const_arr)[ind_comp,:]
        T_p_arr = np.array(T_p)[ind_comp]
        
        components = em1[ind_comp,0]
        components_n = em1[ind_comp,1]
        components_n      
                
        ind_sort = [np.where((np.array(user_comps) == i)|(np.array(user_comps) == j))[0][0] for (i,j) in zip(components_n,components)]
        
        Fv = Fv1[ind_sort]      

                
        
        
        xD_arr1 = []
        xW_arr1 = []
        for i in range(0,len(Fv)):
            comp_i = Fv[i]
        
            if i < Lk_ind:
                xDi_D = 1*(comp_i*F)
                xWi_W = 0
            elif i == Lk_ind:
                xDi_D = Lk_rec*(comp_i*F)
                xWi_W = (1 - Lk_rec)*(comp_i*F)
            elif i == Hk_ind:
                xWi_W = Hk_rec*(comp_i*F)
                xDi_D = (1 - Hk_rec)*(comp_i*F)
            elif i > Hk_ind:
                xDi_D = 0
                xWi_W = 1*(comp_i*F)
            
            xD_arr1.append(xDi_D) 
            xW_arr1.append(xWi_W)
        
        xD_arr = np.array(xD_arr1)
        xW_arr = np.array(xW_arr1)
        
        D = np.sum(xD_arr);
        W = np.sum(xW_arr);
        xDi = (1/D)*xD_arr;
        xWi = (1/W)*xW_arr;
        
        
        data_init = pd.DataFrame({"components":components,"Fv":Fv,"xDi":xDi,"xD_arr":xD_arr,"xWi":xWi,"xW_arr":xW_arr})
        
          #index of reference component   ####an alternative input
        
   
        #find bubble point
        
        it = 0;
        Pref_sat = P
        Tbp_arr1 = []
        cr_arr1 = []
        while it <= 10:
            Ps_arr1 = []
            Ps_arr22 = []
            Tref_sat = ((antoine_matrix[min_ind,1])/(antoine_matrix[min_ind,0] - np.log10(Pref_sat))) - antoine_matrix[min_ind,2]; #as our initial T guess
            for i in range(0,len(antoine_matrix)):
                Psi = 10**(antoine_matrix[i,0]-((antoine_matrix[i,1])/(Tref_sat+antoine_matrix[i,2])));
                Ps_arr1.append(Psi)
                Ps_arr = np.array(Ps_arr1)
                
                
            alpha_bp = (Ps_arr/Pref_sat);
            kr = 1/np.sum(xWi*alpha_bp);
            Pref_sat = kr * P;
            Trefn_sat = ((antoine_matrix[min_ind,1])/(antoine_matrix[min_ind,0] - np.log10(Pref_sat))) - antoine_matrix[min_ind,2]
        
            for i in range(0,len(antoine_matrix)):
                Psi2 = 10**(antoine_matrix[i,0]-((antoine_matrix[i,1])/(Tref_sat+antoine_matrix[i,2])))
                Ps_arr22.append(Psi2)
                Ps_arr2 = np.array(Ps_arr22)
            
            ki = (Ps_arr2)/(P);
            cr = np.sum(ki*xWi);
            it = it + 1
            Tbp_arr1.append(Trefn_sat)
            cr_arr1.append(cr)
            Tbp_arr = np.array(Tbp_arr1)
            cr_arr = np.array(cr_arr1)
            if it == 8 :
                Tbp = round(Trefn_sat,2); ##########################useroutput
                break
            
        
        #find dewpoint
        
        it1 = 0;
        Pref_sat1 = P
        Tdp_arr1 = []
        cr_arr11 = []
        while it1 <= 10:
            Ps_arr11 = []
            Ps_arr221 = []
            Tref_sat1 = ((antoine_matrix[min_ind,1])/(antoine_matrix[min_ind,0] - np.log10(Pref_sat1))) - antoine_matrix[min_ind,2]; #as our initial T guess
            for ii in range(0,len(antoine_matrix)):
                Psi1 = 10**(antoine_matrix[ii,0]-((antoine_matrix[ii,1])/(Tref_sat1+antoine_matrix[ii,2])));
                Ps_arr11.append(Psi1)
                Ps_arr1 = np.array(Ps_arr11)
                
                
            alpha_dp1 = (Ps_arr1/Pref_sat1);
            kr1 = np.sum(xDi/alpha_dp1);
            Pref_sat1 = kr1 * P;
            Trefn_sat1 = ((antoine_matrix[min_ind,1])/(antoine_matrix[min_ind,0] - np.log10(Pref_sat1))) - antoine_matrix[min_ind,2]
        
            for i in range(0,len(antoine_matrix)):
                Psi21 = 10**(antoine_matrix[i,0]-((antoine_matrix[i,1])/(Tref_sat1+antoine_matrix[i,2])))
                Ps_arr221.append(Psi21)
                Ps_arr21 = np.array(Ps_arr221)
            
            ki1 = (Ps_arr21)/(P);
            cr1 = np.sum(xDi/ki)
            it1 = it1 + 1
            Tdp_arr1.append(Trefn_sat1)
            cr_arr1.append(cr1)
            Tdp_arr = np.array(Tdp_arr1)
            cr_arr11 = np.array(cr_arr11)
            if it1 == 8 :
                Tdp = round(Trefn_sat1,2); ##########################useroutput,Tdp,Nmin
                break
            
        
        alpha_lk_hk = (alpha_dp1[Lk_ind]*alpha_bp[Lk_ind])**0.5;
        
        
        Nmin = np.round((np.log10((xDi[Lk_ind]*xWi[Hk_ind])/(xDi[Hk_ind]*xWi[Lk_ind])))/(np.log10(alpha_lk_hk)))
        
        Nmin ##########################useroutput
        
        #distribution
        xWo_arr1 = [];
        xDo_arr1 = [];
        init_printing()
        XW,XD = symbols("XW XD")
        eq1,eq2 = symbols('eq eq2',cls = Function)
        
        for i in range(0,len(Fv)):
            comp = Fv[i];
            eq1 = Eq(comp*F,XD + XW)
            alpha = (alpha_dp1[i]*alpha_bp[i])**0.5;
            eq2 = Eq((XD/XW),((alpha**Nmin)*(xD_arr[Hk_ind]/xW_arr[Hk_ind])))
            XDi_XWi = solve([eq1,eq2],(XD,XW));
            xWo_arr1.append(float(XDi_XWi[XW]))
            xDo_arr1.append(float(XDi_XWi[XD]))
            
            xWo_arr = np.round(np.array(xWo_arr1),3);
            xDo_arr = np.round(np.array(xDo_arr1),3);
            
        
        Dn = np.round(np.sum(xDo_arr),2);
        Wn = np.round(np.sum(xWo_arr),2);
        xDin = (1/Dn)*xDo_arr;
        xWin = (1/Wn)*xWo_arr;
        
        # datan = table(components',Fv',round(xDin',5),xDo_arr',round(xWin',5),xWo_arr',VariableNames=["Components","Xfi","XD","Xd_D","Xw","Xw_W"])
        
        data_fin =pd.DataFrame({"Compound":components_n,"Formula":components,"Fv":Fv,"xDi":np.round(xDin,5),"xD_arr":xDo_arr,"xWi":np.round(xWin,5),"xW_arr":xWo_arr})
        
        
        # Underwood
        Tav = (Tbp + Tdp)/2; # arith average of the 2 temperatures
        Psat_un1 = [];
        for i in range(0,len(antoine_matrix)):
            Ps = 10**(antoine_matrix[i,0]-(antoine_matrix[i,1]/(Tav+antoine_matrix[i,2])));
            Psat_un1.append(Ps)
            Psat_un = np.array(Psat_un1)
        
        
        
        alpha_un = (1/Psat_un[min_ind])*Psat_un
        
        
        O = symbols('O')
        LHS = Eq((np.sum((1/(alpha_un - O))*(alpha_un*xWin))), (1-q))
        Oii = solve(LHS,O)
        Oi = float(round(Oii[0],5))
        
        #for Rmin
        Rmin = round(np.sum((1/(alpha_un - Oi))*(alpha_un*xDin)) - 1,3) ##########################useroutput
        
        #finding R
        
        R = round(R_int*Rmin,3) ##########################useroutput
        
        #Finding N using Gilliland's correlation
        g = (R-Rmin)/(R+1)
        
        N,Ns,Nr = symbols('N Ns Nr')
        fun = Eq(((N - Nmin)/(N + 1) ) ,(1 - exp(((1 + 54.4*g)/(11 + 117.2*g))*((g - 1)/(g**0.5)))))
        N_th = int(round(solve(fun,N)[0])) - 1 

          #finding feed tray location using Kirk-Bride correlation
        eq1_1 = Eq(log(Nr/Ns,10),(0.206*log((W/D)*((Fv[Hk_ind]/Fv[Lk_ind])*((xWin[Lk_ind])/(xDin[Hk_ind]))**(2)),10)))
        eq1_2 = Eq(Nr + Ns, N_th)

        q_ret = solve([eq1_1,eq1_2])
        N_r = int(round(q_ret[Nr]))
        N_s = int(round(q_ret[Ns]))
        
        
        
        return Dn,Wn,Tbp,Tdp,Nmin,data_fin,Rmin,R,N_th,N_r,N_s





# %%
def tab_res(Tbp = 0,Tdp=0,Nmin=0,N_th=0,N_r=0,N_s=0,Rmin=0,R=0):
        param_ = ["Bubble Point Temp (℃)","Dew Point Temp (℃)","N_min","N_actual","N_enrich","N_strip","R_min","R"]
        out_p = pd.DataFrame({"":param_," ":[Tbp,Tdp,Nmin,N_th,N_r,N_s,Rmin,R]})
        return out_p



# %%
tab_res()

# %%
compound_data = data[["formula","compounds","molar_weigth","Tb(K)","Tc(K)","Pc(bar)","Vc(cm3/mol)"]]
compound_data  ###################output

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
