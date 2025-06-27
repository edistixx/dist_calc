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
from flux_py import *

# %%
x,y,i= gen(Ti=298.2,P=1.013,c1="air",c2="H2O",DC=1,corr=0,state=1,Case=0,z1_in=0,z2_in=2.5*10**-3,Pa1_in=0.00114*101325,Pa2_in=0,a_in=2,areatype = 0,geo=1,sigma=0.004,Rs_in=0.943*10**-2,Rsf_in=0.594*10**-2,yi_in=1,yf_in=1)
i

# %% [markdown]
# # computations imports

# %%
from mult_dist_comp import *
import mult_dist_comp

# %%
# P = 4
# F = 1000
# Fv = np.array([0.2,0.3,0.5])
# Lk_rec = 0.99
# Hk_rec = 0.99
# Lk_ind = 1
# Hk_ind = 2
# user_comps = np.array(["ethane","propane","butane"])
# q = 1
# R_int = 4
# mult_dist_comp.results(P,F,Fv,Lk_rec,Hk_rec,Lk_ind,Hk_ind,user_comps,q,R_int)

# %%
from D_AB_comp import *
from D_AB_comp import data_d


# %%

# multi
T = 300
P = 4
unit = "(m^2/s)"
comp = np.array(["benzene","bromine","air","oxygen"])
frac = np.array([0.1,0.3,0.2,0.4])
corr = 0
diff_spec = 0
c1 = "argon"
c2 = "benzene"
mult_dab(T,P,corr,diff_spec,comp,frac)
Dab(T,P,c1,c2,corr)

# %%

# %% [markdown]
# # UI design

# %%
from dash import Dash,html, dash_table,dcc,callback,Output,Input,State
import dash_bootstrap_components as dbc
import dash

# %%
app = dash.Dash(external_stylesheets = [dbc.themes.UNITED,dbc.icons.BOOTSTRAP],assets_folder='assets', assets_url_path='/assets/')

# %%
img_tag = html.Img(src = "assets/logo.png",width = 40)
brand_link = dcc.Link([img_tag],href = "#",className = "navbar-brand")

navbar = dbc.Navbar(
                dbc.Container([
                    dbc.Row([
                        dbc.Col([
                            html.Div([brand_link,
                            dbc.NavbarBrand("Sep-calc",className = "ms-2")]),
                        ])
                        
                    ]),
                    dbc.Row([ 
                        dbc.Col([
                    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                        dbc.Nav([
                            dbc.Button(dbc.NavItem(dbc.NavLink("🏠 Home",href = "/")),color = "dodgerblue"),
                            dbc.Button(dbc.NavItem(dbc.NavLink("🗓️ Ref",href = "/d_base")),color = "dodgerblue"),
                            dbc.Button(dbc.NavItem(dbc.NavLink("ℹ️ About")),id = "About",n_clicks = 0,color = "dodgerblue"),
                            
                            
                            
                            
                            ],
                                   navbar = True,pills = True),
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            )
                        ])
                    ]),
                    
                   
          
                
                
                ])



    
,color="#1A242D",
dark=True
)

# %%
ab_cardf = html.Div([
    html.Br(),
    
  
    
    html.Div([
    
    html.Div(["_______________________________________________"],className = "text-center", style={'color': 'white','font-family':'Open Sans'}),
    html.Br(),
    html.Div(["Developed by the Technical and App Development team "],className = "text-center", style={'color': 'white','font-family':'Open Sans'}),
    html.Div(),
        html.Div([html.P("The Modelling Club - KNUST",className = "text-center", style={'color': 'white','font-family':'Open Sans'})
                 ]),
    html.Div(["Department Of Chemical Engineering"],className = "text-center", style={'color': 'white','font-family':'Open Sans'}),
    
    ]),
    
html.Div([
    html.Div([],className = "text-center",style = { "background":'#7f98d2',"background-image" : 'url("/assets/TMC_LOGO.png")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":100,"width":100}),
    # html.Div(["Providing local solutions through the use of computer aided engineering."],style={'color': 'white','font-family':'Open Sans'}),
]
      ,style = {
    "background":'#7f98d2',}  ),
    
],style = {

    "border-radius":0,
    "background":'#7f98d2',
    "height":170
    })



# %% [markdown]
# # Mult_widgets

# %%

P_unit= dcc.Dropdown(options = ["bar","atm","Pa","mmHg","psia"],value = "bar",id = "p_unit",style = { "width" : 117,"height":5})
flow_unit= dcc.Dropdown(id = "flow_unit",style = { "width" : 117,"height":5})
flow_unit1= dcc.Dropdown(options = ["kmol/hr","kmol/s","mol/hr","mol/s","Ibmol/hr","Ibmol/s","kg/hr","kg/s"],id = "flow_unit1",style = { "width" : 117,"height":5})
flow_unit2= dcc.Dropdown(options = ["kmol/hr","kmol/s","mol/hr","mol/s","Ibmol/hr","Ibmol/s","kg/hr","kg/s"],id = "flow_unit2",style = { "width" : 117,"height":5})
flowbasis= dcc.Dropdown(options = ["Mole","Mass"],value = "Mole",id = "flowbasis",style = { "width" : 70,"height":5})
fracbasis= dcc.Dropdown(options = ["Mole","Mass"],value = "Mole",id = "fracbasis",style = { "width" : 100,"height":5})



Lk_in= dcc.Dropdown(id = "Lk_in",style = { "width" : 90,"height":5})
Hk_in= dcc.Dropdown(id = "Hk_in",style = { "width" : 90,"height":5})

Lk_rec = dcc.Input(id = "Lk_rec",type = "number",placeholder = "@Distillate",style = { "width" : 100,"textAlign" : "right"})
Hk_rec = dcc.Input(id = "Hk_rec",type = "number",placeholder = "@Bottom",style = { "width" : 100,"textAlign" : "right"})



F_in = dcc.Input(id = "Feed_flow",type = "number",placeholder = "Feed flowrate",style = { "width" : 70,"textAlign" : "right"})
P_in = dcc.Input(id = "Pressure",type = "number",placeholder = "Pressure",style = { "width" : 70,"textAlign" : "right"})
# q_sl = dcc.RangeSlider(0, 1, 0.1, value=[1], id='q_range')
q_sl = dcc.Input(id = "quality",type = "number",placeholder = "Quality",style = { "width" : 70,"textAlign" : "right"},max = 1,min = 0)
R_Rmin = dcc.Input(id = "ratio",type = "number",placeholder = "R/Rmin",style = { "width" : 70,"textAlign" : "right"},min = 1)

R_out = dcc.Input(id = "R_out",type = "number",placeholder = "",style = { "width" : 85,"textAlign" : "right"},disabled = True)
N_out = dcc.Input(id = "N_out",type = "number",placeholder = "",style = { "width" : 85,"textAlign" : "right"},disabled = True)
D_out = dcc.Input(id = "D_out",type = "number",placeholder = "",style = { "width" : 85,"textAlign" : "right"},disabled = True)
W_out = dcc.Input(id = "W_out",type = "number",placeholder = "",style = { "width" : 85,"textAlign" : "right"},disabled = True)

ref_comp= dcc.Dropdown(id = "ref_comp",style = { "width" : 90,"height":5})


# %% [markdown]
# # DAB widgets

# %%
P_dab = dcc.Input(id = "P_dab",type = "number",placeholder = "Pressure",style = { "width" : 70,"textAlign" : "right"})
T_dab = dcc.Input(id = "T_dab",type = "number",placeholder = "Temperature",style = { "width" : 70,"textAlign" : "right"})
c1_in = dcc.Input(id = "c1_in",type = "text",placeholder = "specie1",style = { "width" : 70,"textAlign" : "right"})
c2_in = dcc.Input(id = "c2_in",type = "text",placeholder = "specie2",style = { "width" : 70,"textAlign" : "right"})
typ = dcc.RadioItems(id = "typ",options = ["Binary","Multi-component"],value = "Binary",inline = True)

P_unit_dab= dcc.Dropdown(options = ["bar","atm","Pa","mmHg","psia"],value = "bar",id = "P_unit_dab",style = { "width" : 117,"height":5})
T_unit_dab= dcc.Dropdown(options = ["K","℃","℉","°R"],value = "K",id = "T_unit_dab",style = { "width" : 117,"height":5})
diff_spec_in = dcc.Dropdown(id = "diff_spec_in",style = { "width" : 117,"height":5})

c1_l = dbc.Label("Compound1:",className = "mr-2")
c2_l = dbc.Label("Compound2:",className = "mr-2")
# corr_out = dbc.Label(className = "mr-2",id = "corr_out")
P_dab_l = dbc.Label("Pressure:",className = "mr-2")
T_dab_l = dbc.Label("Temperature:",className = "mr-2")
corr_l = dbc.Label("Correlation:",className = "mr-2")

fracbasis_dab= dcc.Dropdown(options = ["Mole","Mass"],value = "Mole",id = "fracbasis_dab",style = { "width" : 100,"height":5})
corr_dab= dcc.Dropdown(options = ["Chapman-Enskog","Wilke-Lee","Fuller et al"],value = "Chapman-Enskog ",id = "corr_dab",style = { "width" : 190,"height":5})
binary_dab= dcc.Dropdown(options = ["Chapman-Enskog","Wilke-Lee","Fuller et al"],value = "Chapman-Enskog ",id = "binary_dab",style = { "width" : 150,"height":5})

outp_dab = dcc.Input(id = "outp_dab",type = "text",placeholder = "",style = { "width" : 90,"textAlign" : "right"},disabled = True)
outp_dab2 = dcc.Input(id = "outp_dab2",type = "text",placeholder = "",style = { "width" : 90,"textAlign" : "right"},disabled = True)
out_unit = dcc.Dropdown(options = ["m^2/s","m^2/hr","cm^2/s","cm^2/hr"],value = "m^2/s",id = "out_unit",style = { "width" : 90,"height":5})

# %% [markdown]
# # Flux widgets

# %%
typ_fl = dcc.RadioItems(id = "typ_fl",options = ["Binary","Multi-component"],value = "Binary",inline = True)
P_fl = dcc.Input(id = "P_fl",type = "number",placeholder = "Pressure",style = { "width" : 70,"textAlign" : "right"})
T_fl = dcc.Input(id = "T_fl",type = "number",placeholder = "Temperature",style = { "width" : 70,"textAlign" : "right"})
z2_z1 = dcc.Input(id = "z2_z1",type = "number",placeholder = "thickness",style = { "width" : 75,"textAlign" : "right"})
Pa1_fl = dcc.Input(id = "Pa1_fl",type = "number",placeholder = "",style = { "width" : 70,"textAlign" : "right"})
Pa2_fl = dcc.Input(id = "Pa2_fl",type = "number",placeholder = "",style = { "width" : 70,"textAlign" : "right"})

c1_in_fl = dcc.Input(id = "c1_in",type = "text",placeholder = "specie1",style = { "width" : 70,"textAlign" : "right"})
c2_in_fl = dcc.Input(id = "c2_in",type = "text",placeholder = "specie2",style = { "width" : 70,"textAlign" : "right"})

P_dab_fl_1 = dbc.Label("Pressure:",className = "mr-2")
T_dab_fl_1 = dbc.Label("Temperature:",className = "mr-2")
corr_fl_1 = dbc.Label("Correlation:",className = "mr-2")
Driv_force_lab = dbc.Label("Driving force:",className = "mr-2")

c1_fl = dbc.Label("Compound1:",className = "mr-2")
c2_fl = dbc.Label("Compound2:",className = "mr-2")
corr_fl_list1= dcc.Dropdown(options = ["Chapman-Enskog","Wilke-Lee","Fuller et al"],value = "Chapman-Enskog ",id = "corr_fl_list1",style = { "width" : 190,"height":5})
P_unit_fl= dcc.Dropdown(options = ["bar","atm","Pa","mmHg","psia"],value = "bar",id = "P_unit_fl",style = { "width" : 117,"height":5})
z2_z1_un= dcc.Dropdown(options = ["m","cm","mm"],value = "m",id = "z2_z1_un",style = { "width" : 50,"height":5})

diff_type= dcc.Dropdown(options = ["Stagnant_film","Eq_counter_curr","Non-eq_counter_curr"],value = "Stagnant_film",id = "diff_type",style = { "width" : 140,"height":5})
Area_type = dcc.Dropdown(options = ["Constant ","Variable"],value = "Constant",id = "Area_type",style = { "width" : 140,"height":5})
state_fl = dcc.Dropdown(options = ["Gas","Liquid"],value = "Gas",id = "state_fl",style = { "width" : 140,"height":5})
Driv_force = dcc.Dropdown(id = "Driv_force",style = { "width" : 190,"height":5})

DrFr = dcc.Dropdown(id = "DrFr",style = { "width" : 190,"height":5})

outp_dab3 = dcc.Input(id = "outp_dab3",type = "text",placeholder = "",style = { "width" : 90,"textAlign" : "right"},disabled = True)
out_unit3 = dcc.Dropdown(options = ["m^2/s","m^2/hr","cm^2/s","cm^2/hr"],value = "m^2/s",id = "out_unit3",style = { "width" : 100,"height":5})
T_unit_fl= dcc.Dropdown(options = ["K","℃","℉","°R"],value = "K",id = "T_unit_fl",style = { "width" : 117,"height":5})
diff_spec_in_fl = dcc.Dropdown(id = "diff_spec_in_fl",style = { "width" : 125,"height":5})

# %%

# %%
#info
info_stat = html.Div([
    html.P("Welcome to Dist-calc v1",className = "text-center"),
    html.P("A mass transfer and separation process calculator designed by the App development team of the Modelling Club-KNUST"),
    html.Br(),
    html.P("Some simulation abilities of version 1.0 include:"),
    html.P("- Molecular diffusivity calculator"),
    html.P("The diffusivity constant is predicted based on the compounds provided, Temperature, Pressure and Correlation selected."),
    html.Br(),
    html.P("- Flux calculator"),
    html.P("The flux of the selected diffusing specie is predicted based on the compounds provided, Temperature, Pressure and Correlation selected, geometry etc."),
    html.Br(),
    html.P("- Distillation Calculator."),
    html.P("The number of stages, reflux ratio,distillate and Bottoms compositions and their corresponding flowrates etc, are predicted based on the compounds entered, input flowrate, pressure,temperature etc")
])


info_stat_dist = html.Div([
    html.P("Distillation",className = "text-center"),
    
    ])
info_stat_flux =  html.Div([
    html.P("Flux calculator is temporarily unvailable!",className = "text-center"),
    
    ])

info_stat_molD =  html.Div([
    html.P("Molecular diffusivity",className = "text-center"),
    
    ])


# %%
empty_content = html.Div([],id = "page-content") # for all the pages

# %% [markdown]
# # Home page

# %%
home_card = dbc.Card([
    dbc.CardBody([ html.Div([
        html.H4("Welcome to Sep-calc v1.0",className = "text-center"),
        
        html.P("A calculator for Separation process calculations ",className = "text-center"),
        html.Br(),

        dbc.Container([
            dbc.Row([

                dbc.Col([],xs = 2, sm = 2,md =2 ,lg = 2,xl = 2),

    dbc.Col([

                     html.Div([
              dbc.Button(dbc.NavItem(dbc.NavLink("Molecular Diffusivity",href = "/molD",className = "text-center")),style = {"background":"#7f98d2"})
        ])
                ])
                
            ]),
             html.Br(),
    
             dbc.Row([
                  dbc.Col([],xs = 2, sm = 2,md =2 ,lg = 2,xl = 2),
                    dbc.Col([

                     html.Div([
              dbc.Button(dbc.NavItem(dbc.NavLink("Flux calculation",href = "/fcalc",className = "text-center")),style = {"background":"#7f98d2"})
        ])
                ]),

             ]),
                     html.Br(),
             dbc.Row([
                dbc.Col([],xs = 2, sm = 2,md =2 ,lg = 2,xl = 2),
                dbc.Col([
                     
        html.Div([
            dbc.Button(dbc.NavItem(dbc.NavLink("Distillation",href = "/multi",className = "text-center")),style = {"background":"#7f98d2"})
        ])
            
                ],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3)
            ]),
                   html.Div([
                            dbc.Modal([
                     dbc.ModalHeader(dbc.ModalTitle("About")),
                     dbc.ModalBody([info_stat]),
                     dbc.ModalFooter(dbc.Button("close",id = "sub_close",className = "ms-auto",n_clicks = 0))
                 ],
                          id = "info",
                          is_open = False,)     
                                 
                                 
                                 
                                 
                                 
                                 ])
        ])
    ])
                          
       
    ])
],style = {
    "width":350,
    "height":380,
    "border-radius":5,
    "background":"lightyellow"
    })


# home html

home =  html.Div([
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Container([
            dbc.Row([dbc.Col()]),
            dbc.Row([
                dbc.Col([],xs = 1, sm = 1,md =4 ,lg = 4,xl = 4),
                dbc.Col([home_card],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4,style = {"padding-left":"2px","padding-right":"1px"}),
                dbc.Col([],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                
            ])

        
    ])

,
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
ab_cardf]




        
    ,style = {"background-image" : 'url("/assets/bg_home.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":780}
)


# %% [markdown]
# # Mult_dist_page design

# %%

# %%
# a form to accept molecule name
c_frame = pd.DataFrame({"Compound_ID":[""],"fraction":0})
mol_names = dbc.Container([
dbc.Row([
    dbc.Col([dbc.Label("Basis:",className = "mr-2")],xs = 2, sm = 2,md =2 ,lg = 2,xl = 2),
    dbc.Col([fracbasis],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
    
]),
    html.Br(),
    html.Br(),
    
    dbc.Row([
        dbc.Col([
    dash_table.DataTable(
        id = "comp_input",
         columns=[
            {"name": i, "id": i, "deletable": False} for i in c_frame.columns
        ],
        data = c_frame.to_dict('records'),
        editable = True,
       
        row_deletable = True,
        page_action="native",
       
        
        
        
        
    )
    ]) ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Button("Add row",id = "add-row-button",n_clicks = 0,style = {"background":"#7f98d2"})
        ],xs = 6, sm = 6,md =6 ,lg = 6,xl = 6),
         dbc.Col([
            html.Div([],id = "frac_total")
        ]),
    ]),
     # ref_comp
    html.Br(),
    dbc.Row([
             dbc.Col([dbc.Label("Ref_comp:",className = "mr-2")],xs = 3, sm = 3,md =2 ,lg = 2,xl = 2),
         dbc.Col([
                 ref_comp
            ],xs = 3, sm = 3,md =2 ,lg = 2,xl = 2),

    ]),
    
])



mult_card = dbc.Card([
dbc.CardHeader("Input Field",className = "text-center"),
 dbc.CardBody([
     html.Br(),
        dbc.Container([
                    
                    dbc.Row([
                        dbc.Col([dbc.Label("Pressure ",className = "mr-2")],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                        dbc.Col([P_in],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                        dbc.Col([P_unit],xs = 4, sm = 4,md =3 ,lg = 3,xl = 3)
                        
                        ]),
            html.Br(),
             dbc.Row([
                        dbc.Col([dbc.Label("Flow_basis",className = "mr-2")],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([flowbasis],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   
                        ]),
             html.Br(),
               dbc.Row([
                        dbc.Col([dbc.Label("Feed_flowrate",className = "mr-2")],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([F_in],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   dbc.Col([flow_unit],xs = 4, sm = 4,md =3 ,lg = 3,xl = 3)
                        ]),
            html.Br(),
               dbc.Row([
                        dbc.Col([dbc.Label("Feed_quality",className = "mr-2")],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([q_sl],xs = 4, sm = 4,md =3 ,lg = 3,xl = 3),
                   
                        ]),
            html.Br(),
               dbc.Row([
                        dbc.Col([dbc.Label("R/Rmin",className = "mr-2")],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([R_Rmin],xs = 4, sm = 4,md =3 ,lg = 3,xl = 3),
                   dbc.Col([])
                        ]),
                html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([],id = "status_display")
                ])
            ]),
            html.Br(),
              
        
                    dbc.Row([
                
                    dbc.Col([
                     dbc.Button("feed_comp",id = "feed",n_clicks = 0,style = {"background":"#D8773A"}),

                    dbc.Modal([
                     dbc.ModalHeader(dbc.ModalTitle("Composition specifications"),className = "text-center"),
                     dbc.ModalBody([
                         
                         html.Div([
                             
                         mol_names,
                             html.Br(),
                             html.Br(),
                            dbc.Container([
                                dbc.Row([
                                    dbc.Col([
                                        html.P("Key specifications",className = "text-center")
                                    ])
                                ]),

                                    dbc.Row([
                                         dbc.Col([
                                        
                                    ],xs = 2, sm = 2,md =2 ,lg = 2,xl =2),
                                        
                                    dbc.Col([
                                        html.P("Key")
                                    ],xs = 4, sm = 4,md =3 ,lg = 3,xl = 3),
                                       dbc.Col([
                                        
                                    ],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                                        
                                     dbc.Col([
                                        html.P("Recovery")
                                    ]),
                                        
                                        
                                ]),
                                    dbc.Row([
                                        dbc.Col([
                                        dbc.Label("Light_Key",className = "mr-2")
                                        ],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                                        dbc.Col([
                                            Lk_in
                                        ],xs = 4, sm = 4,md =5 ,lg = 5,xl = 5),
                                        dbc.Col([
                                            Lk_rec
                                        ],xs = 2, sm = 2,md =2 ,lg = 2,xl = 2),
                                    ]),
                                html.Br(),
                                    dbc.Row([
                                        dbc.Col([
                                        dbc.Label("Heavy_Key",className = "mr-2")
                                        ],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                                        dbc.Col([
                                            Hk_in
                                        ],xs = 4, sm = 4,md =5 ,lg = 5,xl = 5),
                                        dbc.Col([
                                            Hk_rec
                                        ],xs = 2, sm = 2,md =2 ,lg = 2,xl = 2),
                                    ])

                            ]),
                         ])
                     
                     ]),
                     dbc.ModalFooter(dbc.Button("Submit",id = "sub",className = "ms-auto",n_clicks = 0,style = {"background":"#D8773A"}))
                 ],
                          id = "mol_ent",
                          is_open = False,)
                ])
                ]),
        
            html.Br(),
                dbc.Col([]),
               
                    
                    ]),                      

 ])
 
   
]
,style = {
    "width":360,
    "height":460,
    "border-radius":5,
    "background":"#F1F4F5"
    }
                    )

#output for FUG
mult_card_out = dbc.Card([
    dbc.CardHeader("Output",className = "text-center"),
         dbc.CardBody([

dbc.Container([




            dbc.Row([
                        dbc.Col([dbc.Label("Distillate flowrate ",className = "mr-2")],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                        dbc.Col([D_out],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                        dbc.Col([flow_unit1],xs = 4, sm = 4,md =3 ,lg = 3,xl = 3)
                        
                        ]),
            html.Br(),
               dbc.Row([
                        dbc.Col([dbc.Label("Bottoms flowrate",className = "mr-2")],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   dbc.Col([W_out],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([flow_unit2],xs = 4, sm = 4,md =3 ,lg = 3,xl = 3)
                        ]),
            html.Br(),
               dbc.Row([
                        dbc.Col([dbc.Label("Stages",className = "mr-2")],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   dbc.Col([N_out],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   
                        ]),
            html.Br(),
               dbc.Row([
                        dbc.Col([dbc.Label("Reflux ratio",className = "mr-2")],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   dbc.Col([R_out],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   dbc.Col([])
                        ]),
            html.Br(),
              
            html.Br(),
                     dbc.Row([
                        dbc.Col([
                             dbc.Col([
                     dbc.Button("Summary",id = "res",n_clicks = 0,style = {"background":"#D8773A"}),
                             dbc.Modal([
                     dbc.ModalHeader(dbc.ModalTitle("Output"),className = "text-center"),
                     dbc.ModalBody([html.Div([
                          dbc.Row([
                                    dbc.Col([html.Div([],id = "table")])
                                    
                                    
                                    
                                        ]),
                                        html.Br(),
                                        html.Br(),
                                            dbc.Row([
                                    dbc.Col([html.Div([],id = "table_dist")])
                                    
                                    
                                    
                                        ])  ,
                     ])]),
                     dbc.ModalFooter(dbc.Button("Close",id = "s_close",className = "ms-auto",n_clicks = 0,style = {"background":"#D8773A"}))
                 ],
                          id = "results_m",
                          is_open = False)

                    
                ])
                        ]),
                   dbc.Col([]),
                        ]),

    
 

]
             )
         ])

]
         ,style = {
        "width":360,
        "height":460,
        "border-radius":5,
        "background":"#F1F4F5"
        }                   
                          
                        )


 




# %% [markdown]
# # Tab links design

# %%


# database 
comp_database_card =  html.Div([
       dash_table.DataTable(
     data = compound_data.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in compound_data.columns],
       virtualization = True,    
       filter_action='native',
    style_cell_conditional=[
        {'if': {'column_id': 'formula'},
         'width': '30%',"textAlign" : "right"},
        {'if': {'column_id': 'compounds'},
         'width': '30%',"textAlign" : "left"},
          {'if': {'column_id': 'molar_weigth'},
         'width': '30%',"textAlign" : "left"},
        {'if': {'column_id': 'Tb(K)'},
         'width': '30%',"textAlign" : "left"},
          {'if': {'column_id': 'Tc(K)'},
         'width': '30%',"textAlign" : "left"},
        {'if': {'column_id': 'Pc(bar)'},
         'width': '30%',"textAlign" : "left"},
         {'if': {'column_id': 'Vc(cm3/mol)'},
         'width': '30%',"textAlign" : "left"},
        
        
    ]

            


           
                                   )
        ])
                                

# %%
# Multicomponent page layout design
multi_comp = html.Div([
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),

    html.Div([]),
                    dbc.Container([
                        dbc.Row([
                             dbc.Col([],
                                    xs = 3, sm = 3,md =1 ,lg = 1,xl = 2,style = {'padding-left':"30px"}),
                              dbc.Col([mult_card],
                                    xs = 11, sm = 11,md = 3,lg =3,xl = 3,style = {'padding-left':"20px"}),
                            
                            dbc.Col([html.Br()],xs = 13, sm = 13,md =3,lg = 1,xl = 1),
                            # dbc.Col([],xs = 1, sm = 1,md =1,lg = 1,xl = 1),
                            
                            dbc.Col([
                                   mult_card_out 
                            ],
                                    xs = 7, sm = 7,md =4 ,lg = 4,xl = 4 ,style = {'padding-left':"20px"}),
                            
                            
                        ]),

                        html.Div([
                            dbc.Modal([
                     dbc.ModalHeader(dbc.ModalTitle("About")),
                     dbc.ModalBody([info_stat_dist]),
                     dbc.ModalFooter(dbc.Button("close",id = "sub_close_d",className = "ms-auto",n_clicks = 0))
                 ],
                          id = "info_stat_dist",
                          is_open = False,)     
                                 
                                 
                                 
                                 
                                 
                                 ])
                        

                        
                    ])



  , 
     html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
html.Div([ab_cardf])]
                     )

# %% [markdown]
# # Diffusivity Design

# %%
c_frame_dab = pd.DataFrame({"Compound_ID":[""],"fraction":0})
mol_names_dab = dbc.Container([
dbc.Row([
    dbc.Col([dbc.Label("Basis:",className = "mr-2")],xs = 2, sm = 2,md =2 ,lg = 2,xl = 2),
    dbc.Col([fracbasis_dab],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
    
]),


   
    html.Br(),
    html.Br(),
    
    dbc.Row([
        dbc.Col([
    dash_table.DataTable(
        id = "comp_input_dab",
         columns=[
            {"name": i, "id": i, "deletable": False} for i in c_frame_dab.columns
        ],
        data = c_frame_dab.to_dict('records'),
        editable = True,
       
        row_deletable = True,
        page_action="native",
       
        
        
        
        
    )
            
    ]) ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Button("Add row",id = "add-row-button_dab",n_clicks = 0,style = {"background":"#7f98d2"})
        ],xs = 6, sm = 6,md =6 ,lg = 6,xl = 6),
         dbc.Col([
            html.Div([],id = "frac_total_dab")
        ]),
    
    ]
            
           
           
           
           
           ),
    html.Br(),
        dbc.Row([
        
        dbc.Col([
            dbc.Label("Binary_corr:",className = "mr-2")
        ],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
         dbc.Col([
            binary_dab
        ],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
    ])
    
])

# %%
for_binary = html.Div([
      dbc.Row([
                        dbc.Col([c1_l],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([c1_in],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   
                        ],id = "binary1"),
    
               # dbc.Row([
               #  dbc.Col(c1_l],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
               #     dbc.Col([c1_in],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),

    
            html.Br(),
               dbc.Row([
                        dbc.Col([c2_l],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([c2_in],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   dbc.Col([])
                        ]),
                html.Br(),
              dbc.Row([
                        dbc.Col([corr_l],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([corr_dab],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   dbc.Col([])
    
              ]),

            html.Br(),

              dbc.Row([
                        dbc.Col([html.H4("Output",className = "text-center")]),
                        ]),
            html.Br(),
               dbc.Row([
                        dbc.Col([html.Div([],id = "corr_out")],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([outp_dab],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([out_unit],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3)
                        ]),
              
            html.Br(),
                     dbc.Row([
                        dbc.Col([
                             dbc.Col([
                     dbc.Button("Summary",id = "res_dab",n_clicks = 0,style = {"background":"#D8773A"}),
                             dbc.Modal([
                     dbc.ModalHeader(dbc.ModalTitle("Summary"),className = "text-center"),
                     dbc.ModalBody([html.Div([
                          dbc.Row([
                                    dbc.Col([html.Div([],id = "table_dab")])
                                    
                                    
                                    
                                        ]),
                                    
                     ])]),
                     dbc.ModalFooter(dbc.Button("Close",id = "s_close_dab",className = "ms-auto",n_clicks = 0,style = {"background":"#D8773A"}))
                 ],
                          id = "results_dab",
                          is_open = False)

                    
                ])
                        ]),
                   
                        ]),








    



    
]  ,id = "for_binary")

    
for_multi =  html.Div([
dbc.Row([
                
                    dbc.Col([
                     dbc.Button("Composition",id = "feed_dab",n_clicks = 0,style = {"background":"#D8773A"}),

                    dbc.Modal([
                     dbc.ModalHeader(dbc.ModalTitle("Composition specifications"),className = "text-center"),
                     dbc.ModalBody([
                         
                         html.Div([
                             
                         mol_names_dab,
                             html.Br(),
                             html.Br(),
                            dbc.Container([
                              
                     dbc.Row([
                                        dbc.Col([
                                        dbc.Label("Diffusing_specie",className = "mr-2")
                                        ],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                                        dbc.Col([
                                            diff_spec_in
                                        ],xs = 4, sm = 4,md =5 ,lg = 5,xl = 5),
                                       
                                    ]),
                                   
                               

                            ]),
                         ])
                     
                     ]),
                     dbc.ModalFooter(dbc.Button("Submit",id = "sub_dab",className = "ms-auto",n_clicks = 0,style = {"background":"#D8773A"}))
                 ],
                          id = "mol_ent_dab",
                          is_open = False,)
                ])
]),




html.Br(),

              dbc.Row([
                        dbc.Col([html.H4("Output",className = "text-center")]),
                        ]),
            html.Br(),
               dbc.Row([
                        dbc.Col([html.Div([],id = "corr_out2")],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([outp_dab2],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([out_unit],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3)
                        ]),
              
            html.Br(),
                     dbc.Row([
                        dbc.Col([
                             dbc.Col([
                     dbc.Button("Summary",id = "res_dab2",n_clicks = 0,style = {"background":"#D8773A"}),
                             dbc.Modal([
                     dbc.ModalHeader(dbc.ModalTitle("Summary"),className = "text-center"),
                     dbc.ModalBody([html.Div([
                          dbc.Row([
                                    dbc.Col([html.Div([],id = "table_dab2")])
                                    
                                    
                                    
                                        ]),
                                    
                     ])]),
                     dbc.ModalFooter(dbc.Button("Close",id = "s_close_dab2",className = "ms-auto",n_clicks = 0,style = {"background":"#D8773A"}))
                 ],
                          id = "results_dab2",
                          is_open = False)

                    
                ])
                        ]),
                   
                        ]),  

      ],id = "for_multi") 


# %%

# %%

# %%
Dab_card_out = dbc.Card([
    
         dbc.CardBody([

dbc.Container([
     html.Br(),
                
              dbc.Row([dbc.Col([typ],xs = 9, sm = 9,md =9 ,lg = 9,xl = 9),
                        dbc.Col([],xs = 1, sm = 1,md =1 ,lg = 1,xl = 1),
                        
                        dbc.Col([],xs = 1, sm = 1,md =1 ,lg = 1,xl = 1)
                        
                        ]),
    html.Br(),

            dbc.Row([
                        dbc.Col([P_dab_l],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                        dbc.Col([P_dab],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                        dbc.Col([P_unit_dab],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3)
                        
                        ]),
            html.Br(),
               dbc.Row([
                        dbc.Col([T_dab_l],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([T_dab],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   dbc.Col([T_unit_dab],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3)
                        ]),
            html.Br(),
                
                    html.Div([],id = "display_choice"),
                
    

              html.Br(),
              
       
    
 

]
             )
         ])

]
         ,style = {
        "width":360,
        "height":590,
        "border-radius":5,
        "background":"#F1F4F5"
        }                   
                          
                        )


 




# %%

# %%
molD = html.Div([
    html.Br(),
    html.Br(),
    
    dbc.Container([
        dbc.Row([
            dbc.Col([],xs = 1, sm = 1,md =4 ,lg = 4,xl = 4),
            dbc.Col([Dab_card_out],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3,style = {'padding-left':"1px",'padding-right':"5px"}),
            dbc.Col([],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3,style = {'padding-right':"50px"})
        ]),
       
        
    ]),
       html.Div([
                            dbc.Modal([
                     dbc.ModalHeader(dbc.ModalTitle("About")),
                     dbc.ModalBody([info_stat_molD]),
                     dbc.ModalFooter(dbc.Button("close",id = "sub_close_D",className = "ms-auto",n_clicks = 0))
                 ],
                          id = "info_stat_molD",
                          is_open = False,)     
                                 
                                 
                                 
                                 
                                 
                                 ]),
      html.Br(),
    html.Br(),
        html.Br(),
    html.Br(),
    
    html.Div([ab_cardf])
])

# %% [markdown]
# # Flux design

# %%
sys_spec = dbc.Container([
dbc.Row([
    dbc.Col([dbc.Label("Diff_type:",className = "mr-2")],xs = 4, sm = 4,md =4 ,lg = 3,xl = 3),
    dbc.Col([diff_type],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
    
]),
    html.Br(),
    dbc.Row([
    dbc.Col([dbc.Label("Area_type:",className = "mr-2")],xs = 4, sm = 4,md =4 ,lg = 3,xl = 3),
    dbc.Col([Area_type],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
    
]),
        html.Br(),
    dbc.Row([
    dbc.Col([dbc.Label("State:",className = "mr-2")],xs = 4, sm = 4,md =4 ,lg = 3,xl = 3),
    dbc.Col([state_fl],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
    
]),
            html.Br(),
    dbc.Row([
    dbc.Col([dbc.Label("△Z:",className = "mr-2")],xs = 4, sm = 4,md =4 ,lg = 3,xl = 3),
    dbc.Col([z2_z1],xs = 3, sm = 3,md =2 ,lg = 2,xl = 2),
    dbc.Col([z2_z1_un],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4)
]),
        html.Br(),

    #     dbc.Row([
        
    #     dbc.Col([
    #         dbc.Label("Binary_corr:",className = "mr-2")
    #     ],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
    #      dbc.Col([
    #         corr_fl_list1
    #     ],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
    # ]),
      # html.Br(),
                      
                     dbc.Row([
                                        dbc.Col([
                                        dbc.Label("Diffusing_specie",className = "mr-2")
                                        ],xs = 4, sm = 4,md =4 ,lg = 3,xl = 3),
                                        dbc.Col([
                                            diff_spec_in_fl
                                        ],xs = 4, sm = 4,md =5 ,lg = 5,xl = 5),
                                       
                                    ]),
    
])

# %%
for_binary_fl = html.Div([
      dbc.Row([
                        dbc.Col([c1_fl],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([c1_in_fl],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   
                        ]),
    
               # dbc.Row([
               #  dbc.Col(c1_l],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
               #     dbc.Col([c1_in],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),

    
            html.Br(),
               dbc.Row([
                        dbc.Col([c2_fl],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([c2_in_fl],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   dbc.Col([])
                        ]),
                html.Br(),
              dbc.Row([
                        dbc.Col([corr_fl_1],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([corr_fl_list1],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   dbc.Col([])
    
              ]),
     html.Br(),
             dbc.Row([
                        dbc.Col([Driv_force_lab],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([DrFr],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   dbc.Col([])
    
              ]),


     dbc.Row([
            dbc.Col([dbc.Button("System",id = "system_spec",n_clicks = 0,style = {"background":"#D8773A"})],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                    dbc.Modal([
                     dbc.ModalHeader(dbc.ModalTitle("System Specification"),className = "text-center"),
                     dbc.ModalBody([
                         
                         html.Div([
                             
                         sys_spec,
                             html.Br(),
                             html.Br(),
                          
                         ])
                     
                     ]),
                     dbc.ModalFooter(dbc.Button("Submit",id = "sub_fl",className = "ms-auto",n_clicks = 0,style = {"background":"#D8773A"}))
                 ],
                          id = "sys_fl",
                          is_open = False)
         
                
              ]),

            html.Br(),

              dbc.Row([
                        dbc.Col([html.H4("Output",className = "text-center")]),
                        ]),
            html.Br(),
               dbc.Row([
                        dbc.Col([html.Div([],id = "corr_out")],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([outp_dab3],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([out_unit3],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3)
                        ]),
              
            html.Br(),
                     dbc.Row([
                        dbc.Col([
                             dbc.Col([
                     dbc.Button("Summary",id = "res_fl",n_clicks = 0,style = {"background":"#D8773A"}),
                             dbc.Modal([
                     dbc.ModalHeader(dbc.ModalTitle("Summary"),className = "text-center"),
                     dbc.ModalBody([html.Div([
                          dbc.Row([
                                    dbc.Col([html.Div([],id = "table_fl")])
                                    
                                    
                                    
                                        ]),
                                    
                     ])]),
                     dbc.ModalFooter(dbc.Button("Close",id = "s_close_fl",className = "ms-auto",n_clicks = 0,style = {"background":"#D8773A"}))
                 ],
                          id = "results_fl",
                          is_open = False)

                    
                ])
                        ]),
                   
                        ]),








    



    
]  ,id = "for_binary_fl")

# %%
fl_card_out =  dbc.Card([
    
         dbc.CardBody([

dbc.Container([
     html.Br(),
                
              dbc.Row([dbc.Col([typ_fl],xs = 9, sm = 9,md =9 ,lg = 9,xl = 9),
                        dbc.Col([],xs = 1, sm = 1,md =1 ,lg = 1,xl = 1),
                        
                        dbc.Col([],xs = 1, sm = 1,md =1 ,lg = 1,xl = 1)
                        
                        ]),
    html.Br(),

            dbc.Row([
                        dbc.Col([P_dab_fl_1],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                        dbc.Col([P_fl],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                        dbc.Col([P_unit_fl],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3)
                        
                        ]),
            html.Br(),
               dbc.Row([
                        dbc.Col([T_dab_fl_1],xs = 4, sm = 4,md =4 ,lg = 4,xl = 4),
                   dbc.Col([T_fl],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
                   dbc.Col([T_unit_fl],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3)
                        ]),
            html.Br(),
                
                    html.Div([],id = "display_choice_fl"),
                
    

              html.Br(),
              
       
    
 

]
             )
         ])

]
         ,style = {
        "width":360,
        "height":650,
        "border-radius":5,
        "background": "#F1F4F5"
        }                   
                          
                        )


 




# %%
molD_fl = html.Div([
    html.Br(),
    html.Br(),
    
    dbc.Container([
        dbc.Row([
            dbc.Col([],xs = 0, sm = 0,md =4 ,lg = 4,xl = 4),
            dbc.Col([fl_card_out],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3),
            dbc.Col([],xs = 3, sm = 3,md =3 ,lg = 3,xl = 3)
        ]),
       
        
    ]),
       html.Div([
                            dbc.Modal([
                     dbc.ModalHeader(dbc.ModalTitle("About")),
                     dbc.ModalBody([info_stat_flux]),
                     dbc.ModalFooter(dbc.Button("close",id = "sub_close_f",className = "ms-auto",n_clicks = 0))
                 ],
                          id = "info_stat_flux",
                          is_open = False,)     
                                 
                                 
                                 
                                 
                                 
                                 ]),
      html.Br(),
    html.Br(),
    
    html.Div([ab_cardf])
])


# %%
@callback([Output("outp_dab3","value"),Output("table_fl","children")],[Input("P_fl","value"),Input("T_fl","value"),Input("c1_in_fl","value"),Input("c2_in_fl","value"),Input("corr_fl_list1","value"),Input("diff_type","value"),Input("Area_type","value"),Input("state_fl","value"),Input("z2_z1","value")])

def flux_comp_(Pi,T,c1i,c2i,corri,case,areatype_i,state_i,z2_in):
    corrl = np.array(["Chapman-Enskog","Wilke-Lee","Fuller et al"])
    dift = np.array(["Stagnant_film","Eq_counter_curr","Non-eq_counter_curr"])
    atype = np.array(["Constant ","Variable"])
    stl = np.array(["Gas","Liquid"])
    
    corr_ind = np.where(corrl == corri)[0][0]
    dift_ind = np.where(dift == case)[0][0]
    atype_ind = np.where(atype == areatype_i)[0][0]
    stl_ind = np.where(stl == state_i)[0][0]








    
    NA_g,Dab_t,data = gen(Ti=T,P=Pi,c1=c1i,c2=c2i,DC=1,corr=corr_ind,state=stl_ind,Case=dift_ind,z1_in=0,z2_in=z2_in,Pa1_in=0.00114*101325,Pa2_in=0,a_in=2,areatype = atype_ind,geo=1,sigma=0.004,Rs_in=0.943*10**-2,Rsf_in=0.594*10**-2,yi_in=1,yf_in=1)
    re_data = dash_table.DataTable(
            data = data.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in data.columns],
           virtualization = False, 
            style_cell_conditional=[
            {'if': {'column_id': ''},
             'width': '30%',"textAlign" : "right"},
            {'if': {'column_id': ' '},
             'width': '30%',"textAlign" : "left"}])
          
    return Dab_t,data








# %%
# corrl = np.array(["Chapman-Enskog","Wilke-Lee","Fuller et al"])
# dift = np.array(["Stagnant_film","Eq_counter_curr","Non-eq_counter_curr"])
# atype = np.array(["Constant ","Variable"])
# stl = np.array(["Gas","Liquid"])

# corr_ind = np.where(corrl == corrl[0])[0][0]
# dift_ind = np.where(dift == dift[0])[0][0]
# atype_ind = np.where(atype == atype[0])[0][0]
# stl_ind = np.where(stl == stl[0])[0][0]
# @callback([Output("outp_dab3","value"),Output("table_fl","children")],[Input("P_fl","value"),Input("T_fl","value"),Input("c1_in_fl","value"),Input("c2_in_fl","value"),Input("corr_fl_list1","value"),Input("DrFr","value"),Input("diff_type","value"),Input("Area_type","value"),Input("state_fl","value"),Input("z2_z1","value")])

# %%

# %%

# %%

# app layout 
app.layout = html.Div([
    html.Div([ dcc.Location(id = "url"),navbar,empty_content])
                      ])



# %%

# %%
@callback(Output("page-content","children"),[Input("url","pathname")])
def render_p_content(pathname):
    if pathname == "/":
        return home
    elif pathname == "/multi":
        return multi_comp
    elif pathname == "/fcalc":
        return molD_fl
    elif pathname == "/d_base":
        return comp_database_card
    elif pathname == "/molD":
        return molD

@app.callback(Output("navbar-collapse", "is_open"),[Input("navbar-toggler", "n_clicks")],[State("navbar-collapse", "is_open")],)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open



@callback( Output("mol_ent", "is_open"),[Input("feed","n_clicks"),Input("sub","n_clicks")],[State("mol_ent", "is_open")])
def toggle_modal(n1,n2,is_open):
    if n1 or n2:
        return not is_open
   
    return is_open
  

@callback(Output("info_stat_dist", "is_open"),[Input("About","n_clicks"),Input("sub_close_d","n_clicks")],[State("info_stat_dist", "is_open")])
def toggle_info(n1,n2,is_open):
     if n1 or n2:
        return not is_open
   
     return is_open


@callback(Output("info_stat_molD", "is_open"),[Input("About","n_clicks"),Input("sub_close_D","n_clicks")],[State("info_stat_molD", "is_open")])
def toggle_info(n1,n2,is_open):
     if n1 or n2:
        return not is_open
   
     return is_open


@callback(Output("info_stat_flux", "is_open"),[Input("About","n_clicks"),Input("sub_close_f","n_clicks")],[State("info_stat_flux", "is_open")])
def toggle_info(n1,n2,is_open):
      if n1 or n2:
        return not is_open
   
      return is_open

@callback(Output("info", "is_open"),[Input("About","n_clicks"),Input("sub_close","n_clicks")],[State("info", "is_open")])
def toggle_info(n1,n2,is_open):
      if n1 or n2:
        return not is_open
   
      return is_open


@callback(Output("results_m", "is_open"),[Input("res","n_clicks"),Input("s_close","n_clicks")],[State("results_m", "is_open")])
def toggle_results(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open



@callback([Output("flow_unit","options")],[Input("flowbasis", 'value')])
def flowunit_sel(flowbasis):
    if flowbasis == "Mole":
        opt = [["kmol/hr","kmol/s","mol/hr","mol/s","Ibmol/hr","Ibmol/s"]]
    elif flowbasis == "Mass":
        opt = [["kg/hr","kg/s"]]

    return opt




@callback([Output("flow_unit1","value"),Output("flow_unit2","value")],[Input("flow_unit", 'value')])
def flowunit_sel2(flow_unit):
    out_unit = [flow_unit,flow_unit]
    return out_unit

@callback(
    Output('comp_input', 'data'),
    [Input('add-row-button', 'n_clicks')],
    [State('comp_input', 'data'),
    State('comp_input', 'columns')]
)
def add_row(n_clicks, rows, columns):
    
    rows.append({c['id']: '' for c in columns})
    return rows



@callback(
    [Output("sub","disabled"),Output("Lk_in","options"),Output("Hk_in","options"),Output("ref_comp","options"),Output("frac_total","children")],
    [Input('comp_input', 'data')],
 
)
def keyupdate(tc):
    
    # if n1 or n2:
    comp_ids = [i["Compound_ID"] for i in tc ] # a list of input compound
    em1 = data[["formula","compounds"]].values
    comp_frac1 = [i["fraction"] for i in tc ] # a list of input compound fraction
    comp_fraci = np.array([float(i) for i in comp_frac1])  
        
    ind_comp = np.sort([np.where((em1[:,1] == i) |(em1[:,0] == i) )[0][0] for i in comp_ids])
    components_n = em1[ind_comp,1]
    c_sum  = np.sum(comp_fraci)
    
    if c_sum != 1.0:
        tt_comp = f"Sum of fraction must add up to 1"
        return True,components_n,components_n,tt_comp
        
    elif c_sum == 1.0:
         tt_comp = f"Total: {np.round(c_sum,1)}"
         return False,components_n,components_n,components_n,tt_comp
        
    
      
        
      

@callback(
    [Output("table", "children"),Output("table_dist", "children"),Output("R_out","value"),Output("N_out","value"),Output("D_out","value"),Output("W_out","value"),Output("status_display","children")],
    [Input("Lk_in","value"),Input("Hk_in","value"),Input("p_unit","value"),Input("flowbasis", 'value'),Input("fracbasis", 'value'),Input("flow_unit", 'value'),Input("flow_unit1", 'value'),Input("flow_unit2", 'value'),Input("comp_input", 'data'),Input("Pressure","value"),Input("Feed_flow","value"), Input("quality","value"),Input("ratio","value"),Input("Lk_rec","value"),Input("Hk_rec","value"),Input("ref_comp","value")]
)

def rec_tab(lk_us,hk_us,u1,u2,u3,u4,u5,u6,tc,p1,p2,p3,p4,p5,p6,p7):
    # if n1 or n2:
        #unit conversion for pressure
        if u1 == "bar":
            P = 1*p1
        elif u1 == "atm":
            P = 1.01325*p1
        elif u1 == "Pa":
            P = (1e-5)*p1
        elif u1 == "mmHg":
            P = (1/760)*1.01325*p1
        elif u1 == "psia":
            P = (1/14.7)*1.01325*p1
        
        
       
        
        
        comp_ids = np.array([i["Compound_ID"] for i in tc ]) # a list of input compound
        comp_frac1 = [i["fraction"] for i in tc ] # a list of input compound fraction
        comp_fraci = np.array([float(i) for i in comp_frac1])  

         #---------keys
        Lk_ind = np.where(comp_ids == lk_us)[0][0] # index of light key 
        Hk_ind = np.where(comp_ids == hk_us)[0][0] # index of heavy key
        ref = np.where(comp_ids == p7)[0][0] # index of heavy key
            #getting the molar mass
        em1 = data[["formula","compounds"]].values
        molm1 = data.molar_weigth.to_list()
        M_array1 = []; 
        for i in range(0,len(comp_ids)):
            ind_comp = np.where((em1[:,1] == comp_ids[i])|(em1[:,0] == comp_ids[i]))[0][0]

            M_array1.append(molm1[ind_comp])

        M_array = np.array([M_array1])[0]
            
         

            #flow fraction confirm
        if u2 == "Mole" and u3 == "Mole":
            comp_frac = np.round(comp_fraci,3)
        elif u2 == "Mole" and u3 == "Mass":
            comp_fracii = (comp_fraci/M_array)/(sum((comp_fraci/M_array)))
            comp_frac = np.round(comp_fracii,3)
        elif u2 == "Mass" and u3 == "Mole":
            comp_fracii = (comp_fraci*M_array)/(sum((comp_fraci*M_array)))
            comp_frac = np.round(comp_fracii,3)
        elif u2 == "Mass" and u3 == "Mass":
            comp_frac = np.round(comp_fraci,3)
            
        Mavg = np.sum(comp_frac*M_array)  ## avg mol mass    
            
        Di,Wi,Tbp,Tdp,Nmin,distrib,Rmin,R,N_th,N_r,N_s = mult_dist_comp.results(P,p2,comp_frac,p5,p6,Lk_ind,Hk_ind,comp_ids,p3,p4,ref)

        

        
        res = tab_res(Tbp,Tdp,Nmin,N_th,N_r,N_s,Rmin,R)
             
        uarr = np.array(["kmol/hr","kmol/s","mol/hr","mol/s","Ibmol/hr","Ibmol/s","kg/hr","kg/s"])
        fl = np.where(uarr ==u4)[0][0]
        fl1 = np.where(uarr == u5)[0][0]
        fl2 = np.where(uarr == u6)[0][0]
        
        r1 = [1,(1/3600),1000,(1000/3600),(1000/453.59),(1000/(453.59*3600)),Mavg,(Mavg/3600)]
        r2 = [3600,1,1000*3600,1000,((1000*3600)/453.59),(1000/453.59),Mavg*3600,Mavg]
        r3 = [1/1000,(1/(3600*1000)),1,(1/3600),(1/453.59),(1/(453.59*3600)),(Mavg/1000),(Mavg/(1000*3600))]
        r4 = [((1/1000)*3600),(1/(1000)),(1*3600),1,((1*3600)/(453.59)),(1/(453.59)),((Mavg*3600)/1000),(Mavg/(1000))]
        r5 = [453.59/1000,(453.59/(1000*3600)),453.59,(453.59/3600),1,1/3600,0.45359,(0.45359*(1/3600))]
        r6 = [((453.59*3600)/1000),((453.59)/1000),453.59*3600,453.59,3600,1,0.45359*3600,0.45359]
        r7 = [(1/Mavg),(1/(Mavg*3600)),(1000/(Mavg)),(1000/(Mavg*3600)),(1/0.45359),(1/(0.45359*3600)),1,(1/3600)]
        r8 = [(1/Mavg)*3600,(1/(Mavg)),(1000/(Mavg))*3600,(1000/Mavg),(1/0.45359)*3600,(1/(0.45359)),3600,1]
        conv_array = np.array([r1,r2,r3,r4,r5,r6,r7,r8])
        D = Di*conv_array[fl,fl1]
        W = Wi*conv_array[fl,fl2]
        
    #unit conversion in a matrice instead of using if else condition
        re_data = dash_table.DataTable(
            data = res.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in res.columns],
           virtualization = True, 
            style_cell_conditional=[
            {'if': {'column_id': ''},
             'width': '30%',"textAlign" : "right"},
            {'if': {'column_id': ' '},
             'width': '30%',"textAlign" : "left"}]
                                      )
        dis_data = dash_table.DataTable(
            data = distrib.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in distrib.columns],
            virtualization = True,
            style_cell_conditional=[
            {'if': {'column_id': 'Compound'},
             'width': '30%',"textAlign" : "right"},
            {'if': {'column_id': 'Formula'},
             'width': '30%',"textAlign" : "left"},
            {'if': {'column_id': 'Fv'},
             'width': '30%',"textAlign" : "right"},
            {'if': {'column_id': 'xDi'},
             'width': '30%',"textAlign" : "left"},
            {'if': {'column_id': 'xD_arr'},
             'width': '30%',"textAlign" : "right"},
            {'if': {'column_id': 'xWi'},
             'width': '30%',"textAlign" : "left"},
            {'if': {'column_id': 'xW_arr'},
             'width': '30%',"textAlign" : "right"}]
                                   )
        check = [R,N_th,D,W]
        if len(check) != 0 :
            mes = ["Results available with no errors"]

        
    
        return re_data,dis_data,R,N_th,D,W,mes






# %%

# %%

# %%

# @callback(
#     [Output("sub_dab","disabled"),Output("diff_spec_in","options")],
#     [Input('comp_input_dab', 'data')]
 
# )
# def keyupdate(tc1):
    
#     comp_ids = [i["Compound_ID"] for i in tc1 ] # a list of input compound
        
#     em1 = data_d[["GAS","Symbol"]].values
#     comp_frac1 = [i["fraction"] for i in tc1 ] # a list of input compound fraction
#     comp_fraci = np.array([float(i) for i in comp_frac1])  
        

    
#     ind_comp = [np.where((em1[:,0] == i)|(em1[:,1] == i))[0][0] for i in comp_ids]
#     components_n = em1[ind_comp,0]
#     c_sum  = np.sum(comp_fraci)
    
#     if c_sum != 1.0:
#         tt_comp = f"Sum of fraction must add up to 1 not {np.round(c_sum,1)}"
#         return True,[components_n]
        
#     elif c_sum == 1.0:
#          tt_comp = f"Total: {np.round(c_sum,1)}"
#          return False,[components_n]
        
    



# %%
@callback(Output("display_choice", "children"),[Input("typ","value")])
def choice(t):
    if t == "Binary":
        return for_binary
    elif t == "Multi-component":
        return for_multi


@callback( Output("mol_ent_dab", "is_open"),[Input("feed_dab","n_clicks"),Input("sub_dab","n_clicks")],[State("mol_ent_dab", "is_open")])
def toggle_modal(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open
@callback(Output("results_dab", "is_open"),[Input("res_dab","n_clicks"),Input("s_close_dab","n_clicks")],[State("results_dab", "is_open")])
def toggle_results(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open


@callback(Output("results_dab2", "is_open"),[Input("res_dab2","n_clicks"),Input("s_close_dab2","n_clicks")],[State("results_dab2", "is_open")])
def toggle_results(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open



@callback(
    Output('comp_input_dab', 'data'),
    [Input('add-row-button_dab', 'n_clicks')],
    [State('comp_input_dab', 'data'),
    State('comp_input_dab', 'columns')]
)
def add_row(n_clicks, rows, columns):
    
    rows.append({c['id']: '' for c in columns})
    return rows


@callback(
    [Output("sub_dab","disabled"),Output("diff_spec_in","options"),Output("frac_total_dab","children")],
    [Input('comp_input_dab', 'data')],
 
)
def keyupdate(tc1):
    
    
    comp_ids = [i["Compound_ID"] for i in tc1 ] # a list of input compound
        
    em1 = data_d[["GAS","Symbol"]].values
    ind_comp = [np.where((em1[:,0] == i)|(em1[:,1] == i))[0][0] for i in comp_ids]
    components_n = em1[ind_comp,0]

    comp_frac1 = [i["fraction"] for i in tc1 ] # a list of input compound fraction
    comp_fraci = np.array([float(i) for i in comp_frac1]) 

    c_sum  = np.sum(comp_fraci)
    if c_sum != 1.0000000:
        tt_comp = f"Sum of fraction must add up to 1"
        return True,components_n,tt_comp
                     
    elif c_sum == 1.0000000:
        tt_comp = f"Total: {np.round(c_sum,1)}"
        return False,components_n,tt_comp
            
        
        




@callback(
    [Output("table_dab2", "children"),Output("outp_dab2","value"),Output("corr_out2","children")],
    [Input("feed_dab","n_clicks"),Input("sub_dab","n_clicks"),Input("P_unit_dab","value"),Input("T_unit_dab","value"),Input("P_dab","value"),Input("T_dab","value"),
    Input("comp_input_dab","data"),Input("out_unit", 'value'),Input("binary_dab", 'value'),Input("fracbasis_dab", 'value'),Input("diff_spec_in", 'value')
]
)


def mult(n1,n2,u1,u2,p1,t1,tc,unit,bd,fb,diff_spec):
    if n1 or n2:
        
        
        
        if u1 == "bar":
            P = 1*p1
        elif u1 == "atm":
            P = 1.01325*p1
        elif u1 == "Pa":
            P = (1e-5)*p1
        elif u1 == "mmHg":
            P = (1/760)*1.01325*p1
        elif u1 == "psia":
            P = (1/14.7)*1.01325*p1
                        
        t_un = ["K","℃","℉","°R"]
        if u2 == t_un[0]:
            T = 1*t1
        elif u2 == t_un[1]:
            T = t1 + 273.15
        elif u2 == t_un[2]:
            T = ((t1 - 32)*(5/9)) + 273.15
                
        elif u2 == t_un[3]:
            T = (((t1 - 460)  - 32)*(5/9)) + 273.15
            
            
                    
        comp_ids = np.array([i["Compound_ID"] for i in tc ]) # a list of input compound
        em1 = data_d[["GAS","Symbol"]].values
        ind_comp = [np.where((em1[:,0] == i)|(em1[:,1] == i))[0][0] for i in comp_ids]
        components_n = em1[ind_comp,0]
            
                    
                    #obtaining molar masses of selected compounds
        M = data_d.MM.values
        M_array1 = []; 
                    
                    
        for i in range(0,len(comp_ids)):
            ind_comp = np.where((em1[:,0] == comp_ids[i])|(em1[:,1] == comp_ids[i]))[0][0]
            M_array1.append(M[ind_comp])
                    
            M_array = np.array([M_array1])[0]
            
                            
        comp_frac1 = [i["fraction"] for i in tc ] 
        comp_fraci = np.array([float(i) for i in comp_frac1])  # a list of input compound fraction
                        #flow fraction confirm
        if fb == "Mole":
            comp_frac = np.round(comp_fraci,3)
        elif fb == "Mass":
            comp_fracii = (comp_fraci/M_array)/(sum((comp_fraci/M_array)))
            comp_frac = np.round(comp_fracii,3)
                    
        eq = ["Chapman-Enskog","Wilke-Lee","Fuller et al"]
        units_d = ["m^2/s","m^2/hr","cm^2/s","cm^2/hr"]
        cor_ind = np.where(np.array(eq) == bd)[0][0]  
            
        d_spec = np.where(np.array(components_n) == diff_spec)[0][0]
                    
        Di_mix,D1_sl,dij = mult_dab(T,P,cor_ind,d_spec,components_n,comp_frac)
                    
                    
        units_d = ["m^2/s","m^2/hr","cm^2/s","cm^2/hr"]
        u_ind = np.where(np.array(units_d) == unit)[0][0]
            
        c_d = np.array([1,3600,10**4,(10**4)*3600])
        conv_fac_res = Di_mix*c_d
            
        conv_arr = np.array([c_d]).T *D1_sl
            
        sum_data1 = pd.DataFrame({"Binary Diffusivities":dij,"Value"+"("+units_d[u_ind]+")":conv_arr[u_ind,:]})
            
        re_data = dash_table.DataTable(
            data = sum_data1.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in sum_data1.columns],
                        virtualization = True, 
                            style_cell_conditional=[
                            {'if': {'column_id': 'Correlation'},
                             'width': '30%',"textAlign" : "right"},
                            {'if': {'column_id': "Value"+"("+units_d[u_ind]+")"},
                             'width': '30%',"textAlign" : "left"}]
                        )
            
        return re_data,str(format(conv_fac_res[u_ind],".3g")),f"D_{components_n[d_spec]}-mix"




@callback(
    [Output("table_dab", "children"),Output("outp_dab","value"),Output("corr_out","children")],
    [Input("c1_in","value"),Input("c2_in", 'value'),Input("P_unit_dab","value"),Input("T_unit_dab","value"),Input("P_dab","value"),Input("T_dab","value"),
    Input("out_unit", 'value'),Input("corr_dab", 'value')
]
)

def binary_comp(c1,c2,u1,u2,p1,t1,unit,corr):
     if u1 == "bar":
        P = 1*p1
     elif u1 == "atm":
        P = 1.01325*p1
     elif u1 == "Pa":
        P = (1e-5)*p1
     elif u1 == "mmHg":
        P = (1/760)*1.01325*p1
     elif u1 == "psia":
        P = (1/14.7)*1.01325*p1
                    
     t_un = ["K","℃","℉","°R"]
     if u2 == t_un[0]:
        T = 1*t1
     elif u2 == t_un[1]:
        T = t1 + 273.15
     elif u2 == t_un[2]:
        T = ((t1 - 32)*(5/9)) + 273.15
            
     elif u2 == t_un[3]:
        T = (((t1 - 460)  - 32)*(5/9)) + 273.15
                
     eq = ["Chapman-Enskog","Wilke-Lee","Fuller et al"]
     units_d = ["m^2/s","m^2/hr","cm^2/s","cm^2/hr"]
     cor_ind = np.where(np.array(eq) == corr)[0][0]    
                
     res,sum_data= Dab(T,P,c1,c2,cor_ind)
                  
                
     units_d = ["m^2/s","m^2/hr","cm^2/s","cm^2/hr"]
     u_ind = np.where(np.array(units_d) == unit)[0][0]
     c_d = np.array([1,3600,10**4,(10**4)*3600])
     conv_fac_res = res[0]*c_d
     conv_arr = np.array([c_d]).T *sum_data
     summary = pd.DataFrame({"Correlation":["Chapman-Enskog ","Wilke-Lee ","Fuller et al"],"Value"+"("+units_d[u_ind]+")":conv_arr[u_ind,:]})    
                    
     re_data1 = dash_table.DataTable(
         data = summary.to_dict('records'),
         columns=[{'id': c, 'name': c} for c in summary.columns],
                    virtualization = True, 
                        style_cell_conditional=[
                        {'if': {'column_id': 'Correlation'},
                         'width': '30%',"textAlign" : "right"},
                        {'if': {'column_id': "Value"+"("+units_d[u_ind]+")"},
                         'width': '30%',"textAlign" : "left"}]
                    )
        
     return re_data1,str(format(conv_fac_res[u_ind],".3g")),f"Diffusivity of {c1} in {c2}"
            
            
                    
        
                    
        
        

               
            
                
                    
               

# %%
@callback(Output("display_choice_fl", "children"),[Input("typ_fl","value")])
def choice(t):
    if t == "Binary":
        return for_binary_fl
    # elif t == "Multi-component":
    #     return for_multi


@callback(Output("sys_fl", "is_open"),[Input("system_spec","n_clicks"),Input("sub_fl","n_clicks")],[State("sys_fl", "is_open")])
def toggle_modal(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    [Output("diff_spec_in_fl","options")],
    [Input("system_spec","n_clicks"),Input("sub_fl","n_clicks"),Input("c1_in","value"),Input("c2_in","value")],
 
)
def keyupdate(n1,n2,c1,c2):
    if n1 or n2:
        comp_ids = [c1,c2] # a list of input compound
        em1 = data_d[["Symbol","GAS"]].values
        ind_comp = np.sort([np.where((em1[:,1] == i)|(em1[:,0] == i))[0][0] for i in comp_ids])
        comp19 = em1[ind_comp,1]
        components_n = comp19.tolist()
        
        return [components_n]





      

# %%



               
        
@callback(
    [Output("DrFr","options")],
    [Input("state_fl","value")]
)

def dforce(st):
    if st == "Gas":
        force = ["Concentration (yi)","Partial pressure"]
        
    elif st == "Liquid":
        force = ["Concentration (xi)","Molar Concentration"]
        
    return [force]
        


@callback(Output("results_fl", "is_open"),[Input("res_fl","n_clicks"),Input("s_close_fl","n_clicks")],[State("results_fl", "is_open")])
def toggle_results(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open 






# %%

# %%
if __name__ == "__main__":

    try:
        app.run(jupyter_mode = "tab",port = "8001")
    except Exception:
        print("Startup problem")
    

# %%



# %%

# comp_ids = ["argon","oxygen"]# a list of input compound
        
# em1 = data_d[["GAS","Symbol"]].values
# ind_comp = [np.where(em1[:,0] == i)[0][0] for i in comp_ids]
# components_n = em1[ind_comp,0]
# list(components_n)

# %%
# comp_ids = ["ethane","propane"]# a list of input compound
# em1 = data[["formula","compounds"]].values
# ind_comp = np.sort([np.where(em1[:,1] == i)[0][0] for i in comp_ids])
# components_n = em1[ind_comp,1]
# components_n

# %%

# %%
# # !pip install plotly --upgrade

# %%

# %%
0.69478+0.29608+0.00871+0.00036+0.00002+0.00005+0.00001


        # %%
        # comp_ids = ["argon","bromine"] # a list of input compound
        # em1 = data_d[["Symbol","GAS"]].values
        # ind_comp = np.sort([np.where(em1[:,1] == i)[0][0] for i in comp_ids])
        # comp19 = em1[ind_comp,1]
        # components_n = [comp19.tolist()]

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
