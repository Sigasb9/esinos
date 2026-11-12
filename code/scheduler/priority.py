"""
Ordonnancement par priorité, non préemptif (plus petit nombre = plus prioritaire).
Renvoie un Gantt : liste de (pid, debut, fin).
"""


def priority(procs):
    """Choisit à chaque fin de processus le plus prioritaire parmi ceux arrivés. Renvoie le Gantt."""
    # TODO (Ilias) :
    # 1. même squelette que SJF : restants, temps = 0, gantt = []
    # 2. tant qu'il reste des processus :
    #    - prets = ceux avec arrival <= temps (sinon "IDLE" jusqu'à la prochaine arrivée)
    #    - prendre le plus petit `priority` (égalité -> arrivée la plus tôt)
    #    - ajouter (pid, temps, temps + burst), avancer temps, le retirer
    # 3. renvoyer gantt
    raise NotImplementedError
