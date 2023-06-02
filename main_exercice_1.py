
import fonctions as fc
import matplotlib.pyplot as plt
from timeit import timeit

def convergence():

    erreurs = []
    x = range(1, 10000, 1)
    for i in x:
        erreurs.append(fc.erreur_segment_argument(i))

    return erreurs,x

timeit('convergence()',globals=globals(),number=1)

y,x = convergence()

plt.plot(x, y)
plt.yscale('log')
plt.xlabel("Nombre de segments")
plt.ylabel("Erreur relative (%)")

plt.show()



