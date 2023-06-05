
import numpy as np
import matplotlib.pyplot as plt
def get_params():

    p = {}
    p['L'] = 5
    p['H'] = 5
    p['x_c'] = 2.5
    p['y_c'] = 2.5
    p['n_segment'] = 20
    p['T0'] = 10 #°C
    p['k'] = 98.8*(10**-6) #m^2/S
    p['delta_x'] = p['L']/p['n_segment']
    p['delta_y'] = p['H']/p['n_segment']
    p['sigma'] = 0.6
    p['A'] = 10

    return p

def create_grid(p):

    x = np.linspace(0,p['L'],p['n_segment']+1)
    y = np.linspace(0,p['H'],p['n_segment']+1)

    X,Y = np.meshgrid(x,y)

    grid = {}
    grid['X'] = X
    grid['Y'] = Y
    return grid

def visualisation(grid,T,T_n_plus_1,T_n_plus_2,T_n_plus_3):


    return 0

def calcul_temperature_point_chaud(grid,p):

    temperature = p['A'] * np.exp(-((grid['X'] - p['x_c']) ** 2 / (2 * p['sigma'] ** 2) + (grid['Y'] - p['y_c']) ** 2 / (2 * p['sigma'] ** 2))) + p['T0']

    temperature[:, 0] = p['T0']
    temperature[:, -1] = p['T0']
    temperature[0, :] = p['T0']
    temperature[-1, :] = p['T0']

    return temperature

def calcul_RHS(p,T):

    T_plus_delta_x = np.roll(T,1,axis=1)
    T_moins_delta_x = np.roll(T,-1,axis=1)
    T_plus_delta_y = np.roll(T,1,axis=0)
    T_moins_delta_y = np.roll(T,-1,axis=0)

    RHS = p['k']*(((T_plus_delta_x - 2*T + T_moins_delta_x)/(p['delta_x']**2))+
                  ((T_plus_delta_y - 2*T + T_moins_delta_y)/(p['delta_y']**2)))

    RHS[:, 0] = 0
    RHS[:, -1] = 0
    RHS[0, :] = 0
    RHS[-1, :] = 0

    return RHS