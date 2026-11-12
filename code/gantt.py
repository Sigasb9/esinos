"""
Affichage console : diagramme de Gantt et tableau des résultats d'ordonnancement.
Un Gantt est une liste de tuples (pid, debut, fin) ; ("IDLE", d, f) = processeur libre.
"""


def afficher(gantt):
    """Affiche le diagramme de Gantt en ASCII, avec les instants sous les barres."""
    if not gantt:
        print("(Gantt vide)")
        return
    barres = "|"
    temps = str(gantt[0][1])
    for pid, debut, fin in gantt:
        largeur = max(len(pid) + 2, 2 * (fin - debut))
        barres += pid.center(largeur) + "|"
        temps += str(fin).rjust(largeur + 1)
    print(barres)
    print(temps)


def afficher_tableau(resultats, attente_moy, sejour_moy):
    """Affiche le tableau par processus puis les moyennes."""
    print(f"{'PID':<6}{'Arrivée':>9}{'Burst':>7}{'Fin':>6}{'Séjour':>8}{'Attente':>9}")
    for r in resultats:
        print(f"{r['pid']:<6}{r['arrivee']:>9}{r['burst']:>7}{r['fin']:>6}"
              f"{r['sejour']:>8}{r['attente']:>9}")
    print(f"Attente moyenne : {attente_moy:.2f}   Séjour moyen : {sejour_moy:.2f}")
