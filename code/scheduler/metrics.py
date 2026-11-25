"""
Calcul des métriques d'ordonnancement à partir d'un Gantt.
séjour = fin − arrivée ; attente = séjour − burst.
"""


def calculer(procs, gantt):
    """
    Renvoie (resultats, attente_moyenne, sejour_moyen).
    resultats : liste de dicts {"pid", "arrivee", "burst", "fin", "sejour", "attente"}, dans l'ordre de procs.
    """
    # TODO (Adam) :

    # 1. retrouver l'instant de fin de chaque processus dans le Gantt
    fin = {}                                       # {pid: instant de fin}
    for pid, debut, f in gantt:
        if pid != "IDLE":                          # on ignore les trous du CPU
            fin[pid] = max(fin.get(pid, 0), f)     # la plus grande fin = vraie fin (utile en Round Robin)
    # 2. calculer séjour et attente pour chaque processus
    resultats = []
    for p in procs:
        sejour = fin[p.pid] - p.arrival            # temps total passé dans le système
        attente = sejour - p.burst                 # temps passé à attendre (séjour - temps CPU utile)
        resultats.append({"pid": p.pid, "arrivee": p.arrival, "burst": p.burst,
                          "fin": fin[p.pid], "sejour": sejour, "attente": attente})
    # 3. moyennes sur tous les processus
    n = len(procs)
    attente_moyenne = sum(r["attente"] for r in resultats) / n
    sejour_moyen = sum(r["sejour"] for r in resultats) / n
    return resultats, attente_moyenne, sejour_moyen
