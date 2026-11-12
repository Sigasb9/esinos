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
    # 1. pour chaque processus, fin = plus grande date de fin de ses tranches dans le Gantt
    #    (ignorer les "IDLE")
    # 2. sejour = fin - arrival ; attente = sejour - burst
    # 3. construire le dict de chaque processus dans resultats
    # 4. moyennes = somme / nombre de processus
    # 5. renvoyer (resultats, attente_moyenne, sejour_moyen)
    raise NotImplementedError
