"""
Ordonnancement Round Robin (tourniquet) avec un quantum fixe.
Convention : les processus arrivés pendant une tranche entrent dans la file AVANT le processus interrompu.
"""


def rr(procs, quantum):
    """Exécute chaque processus au plus `quantum` unités à tour de rôle. Renvoie le Gantt."""
    # TODO (Ilias) :
    # 1. trier par arrivée ; reste = {pid: burst} ; file = deque() ; temps = 0
    # 2. ajouter à la file les processus arrivés à temps 0
    # 3. tant qu'il reste du travail :
    #    - file vide -> ("IDLE", temps, prochaine arrivée), puis ajouter les arrivés
    #    - p = file.popleft() ; duree = min(quantum, reste[p])
    #    - ajouter (pid, temps, temps + duree) ; temps += duree ; reste[p] -= duree
    #    - ajouter d'abord les processus arrivés pendant cette tranche (arrival <= temps)
    #    - PUIS remettre p en fin de file s'il n'a pas fini
    # 4. renvoyer gantt
    raise NotImplementedError
