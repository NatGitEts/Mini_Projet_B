
import numpy as np
import matplotlib.pyplot as plt
def get_params():

    p = {}
    p['L'] = 10
    p['H'] = 10
    p['x_c'] = 5
    p['y_c'] = 5
    p['n_segment'] = 100
    p['T0'] = 200 #°C
    p['k'] = 98.8*(10**-6) #m^2/S
    p['delta_x'] = p['L']/p['n_segment']
    p['delta_y'] = p['H']/p['n_segment']
    p['sigma'] = 0.2
    p['A'] = 10

    return p
def create_grid(params):

    x = np.linspace(0,params['L'],params['n_segment']+1)
    y = np.linspace(0,params['H'],params['n_segment']+1)

    X,Y = np.meshgrid(x,y)

    grid = {}
    grid['X'] = X
    grid['Y'] = Y

    return grid

def visualisation(grid,p,T):

    plt.contourf(grid['X'], grid['Y'], T)

    plt.show()

    return 0

def calcul_temperature(grid,p):

    temperature = p['A'] * np.exp(-((grid['X'] - p['x_c']) ** 2 / (2 * p['sigma'] ** 2) + (grid['Y'] - p['y_c']) ** 2 / (2 * p['sigma'] ** 2))) + p['T0']

    return temperature

def calcul_RHS(p,T,grid):

    RHS = p['k']*(((T(grid['X']+p['delta_x'],grid['Y']) - 2*T(grid['X'],grid['Y']) + T(grid['X']-p['delta_x'],grid['Y']))/(p['delta_x']**2))+
                 (((T(grid['X'],grid['Y']+p['delta_y']) - 2*T(grid['X'],grid['Y']) + T(grid['X'],grid['Y']-p['delta_y'])))/(p['delta_y']**2)))

    return RHS