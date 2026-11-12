"""
Ordonnancement SJF (plus court job d'abord), non préemptif.
Renvoie un Gantt : liste de (pid, debut, fin).
"""


def sjf(procs):
    """Choisit à chaque fin de processus le plus court parmi ceux arrivés. Renvoie le Gantt."""
    # TODO (Adam) :
    # 1. restants = copie de procs ; temps = 0 ; gantt = []
    # 2. tant qu'il reste des processus :
    #    - prets = ceux avec arrival <= temps
    #    - si aucun : ajouter ("IDLE", temps, prochaine arrivée) et sauter à cette date
    #    - sinon : prendre le plus petit burst (égalité -> arrivée la plus tôt),
    #      ajouter (pid, temps, temps + burst), avancer temps, le retirer
    # 3. renvoyer gantt
    raise NotImplementedError
