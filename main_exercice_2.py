import numpy as np

import fonctions as fc

p = fc.get_params()
grid = fc.create_grid(p)
print(np.shape(grid['X']))
T = fc.calcul_temperature(grid,p)

fc.visualisation(grid,p,T)

RHS = np.ndarray()

RHS = fc.calcul_RHS(p,T,grid)
