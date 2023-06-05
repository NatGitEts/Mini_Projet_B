import numpy as np
import matplotlib.pyplot as plt
import fonctions_exercice_2 as fc

p = fc.get_params()
grid = fc.create_grid(p)
T = fc.calcul_temperature_point_chaud(grid,p)

temperatures = []
temperatures.append(T)

F0 = 0.25
dt = (F0 * (p['delta_x']**2))/(p['k'])

nombre_subplots = int(input("Entrez le nombre d'itération : "))

for i in range (1,nombre_subplots):
    RHS = fc.calcul_RHS(p,temperatures[i-1])
    temperatures.append(temperatures[i-1] + (dt*RHS))

# Calculer le nombre de lignes et de colonnes nécessaires pour la grille de subplots
nombre_lignes = int(nombre_subplots ** 0.5)
nombre_colonnes = int((nombre_subplots + nombre_lignes - 1) / nombre_lignes)

# Créer la grille de subplots
fig, axes = plt.subplots(nombre_lignes, nombre_colonnes)

# Supprimer les subplots inutilisés
if nombre_subplots < len(axes.flat):
    for j in range(nombre_subplots, len(axes.flat)):
        fig.delaxes(axes.flatten()[j])

# Parcourir les subplots et les personnaliser (dans cet exemple, nous affichons simplement leur indice)
for i, ax in enumerate(axes.flat):
    if i < nombre_subplots:
        im = ax.contourf(grid['X'],grid['Y'],temperatures[i],origin='lower')
        fig.colorbar(im, ax=ax)

# Ajuster les espaces entre les subplots
fig.tight_layout()
# Afficher l'image avec les subplots
plt.show()