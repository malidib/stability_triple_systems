# Only two packages are needed
import pickle
import pandas as pd


# Main function, nothing to change here.
def estimate_boundary(X,location):
    X=pd.DataFrame([X],columns=['mass1', 'mass2', 'inclination', 'ecc1', 'ecc2'])
    e=float(X["ecc2"])
    
    if( (e<=0.8) & (location=="inner")):
        file_name = "xgb_e0p8_inner.pkl"
        model_inner = pickle.load(open(file_name, "rb"))
        y_pred = model_inner.predict(X)

    if((e<=0.8) & (location=="outer")):
        file_name = "xgb_e0p8_outer.pkl"
        model_inner = pickle.load(open(file_name, "rb"))
        y_pred = model_inner.predict(X)

    if((e>0.8) & (location=="inner")):
        file_name = "xgb_e0p9_inner.pkl"
        model_inner = pickle.load(open(file_name, "rb"))
        y_pred = model_inner.predict(X)

    if((e>0.8) & (location=="outer")):
        file_name = "xgb_e0p9_outer.pkl"
        model_inner = pickle.load(open(file_name, "rb"))
        y_pred = model_inner.predict(X)

    return 10.**y_pred


#############################################  START PARAMETERS ###############################################
mass_s1 = 1. # mass of star 1 in any unit
mass_s2 = 1.  # mass of star 2 in same unit as mass_s1
mass_planet = 1e-3 # mass of the planet in same unit as mass_s1 and mass_s2
ecc_b= 0.1 # binary stars eccentricity 
ecc_p = 0.1 # planetary eccentricity 
inclination = 10. # inclination between the orbital planes of the binary and the planet in degrees 
boundary = "inner" #"inner" vs "outer" boundary to estimate  
#############################################  END PARAMETERS  ###############################################

Mb = mass_s2/(mass_s1+mass_s2)  # Calculate the binary mass parameter
Mp = mass_planet/(mass_s1+mass_s2) # Calculate the planetary mass parameter

# Return the ratio a_c/a_b where a_c and a_b are respectively the critical and binary semimajor axis
estimate_boundary([Mb,Mp,inclination,ecc_b,ecc_p],boundary)