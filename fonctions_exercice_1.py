
def calcul_erreur(solution_exacte,solution_rectangle):
    erreur_pourcentage = (solution_exacte-solution_rectangle)/solution_exacte
    return erreur_pourcentage
def calcul_solution_exacte(a,b,p1,p2,p3,p4):

    F_b = p1*b + (p2*(b**2))/2 + (p3*(b**3))/3 + (p4*(b**4))/4
    F_a = p1*a + (p2*(a**2))/2 + (p3*(a**3))/3 + (p4*(a**4))/4

    solution_exact = F_b - F_a

    return solution_exact

def calculer_aire(x,y):
    return x*y

def calcul_solution_rectangle(a,b,n,p1,p2,p3,p4):

    solution_rectangle = 0
    nombre_segments = (b-a)/n
    valeurs = []

    num_iteration = int(n+1)

    for i in range(num_iteration):
        yo = a + (i *nombre_segments)
        valeurs.append(yo)

    x = []
    for i in range(0,len(valeurs)-1):
        x.append(((valeurs[i]+valeurs[i+1])/2))

    y = []
    for i in x:
        y.append(p1 + (p2 * i) + (p3 * (i ** 2)) + (p4 * (i ** 3)))

    aire = []
    for i in range(0,len(y)):
        aire.append(calculer_aire(nombre_segments,y[i]))
        solution_rectangle += aire[i]

    return solution_rectangle

def erreur_segment_argument(n):

    solution_exacte = calcul_solution_exacte(0, 10, 1, 5, 10, 15)
    solution_rectangle = calcul_solution_rectangle(0, 10, n, 1, 5, 10, 15)

    erreurs = calcul_erreur(solution_exacte, solution_rectangle)

    return erreurs