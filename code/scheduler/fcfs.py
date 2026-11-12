"""
Ordonnancement FCFS (premier arrivé, premier servi), non préemptif.
Renvoie un Gantt : liste de (pid, debut, fin), avec ("IDLE", d, f) si le CPU attend.
"""


def fcfs(procs):
    """Ordonnance procs dans l'ordre d'arrivée. Renvoie le Gantt."""
    # TODO (Adam) :
    # 1. trier les processus par date d'arrivée (puis pid en cas d'égalité)
    # 2. temps = 0 ; pour chaque processus :
    #    - si temps < arrival : ajouter ("IDLE", temps, arrival) et avancer temps
    #    - ajouter (pid, temps, temps + burst) puis temps += burst
    # 3. renvoyer la liste
    raise NotImplementedError
