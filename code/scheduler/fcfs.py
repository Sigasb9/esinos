"""
Ordonnancement FCFS (premier arrivé, premier servi), non préemptif.
Renvoie un Gantt : liste de (pid, debut, fin), avec ("IDLE", d, f) si le CPU attend.
"""


def fcfs(procs):
    """Ordonnance procs dans l'ordre d'arrivée. Renvoie le Gantt."""  
    # TODO (Adam) :

    # 1. trier par arrivée (puis par pid en cas d'égalité)
    #    sorted() crée une nouvelle liste : la liste d'origine n'est pas modifiée.
    #    key=(arrival, pid) : on compare d'abord l'arrivée, le pid départage les égalités.
    gantt = []
    temps = 0                                      # l'horloge du CPU (instant courant)
    for p in sorted(procs, key=lambda p: (p.arrival, p.pid)):
        if temps < p.arrival:                      # personne n'est arrivé : le CPU attend
            # trou dans le Gantt : le CPU ne fait rien de temps à p.arrival
            gantt.append(("IDLE", temps, p.arrival))
            temps = p.arrival                      # on saute directement à l'arrivée
        # non préemptif : une fois lancé, p tourne pendant tout son burst
        gantt.append((p.pid, temps, temps + p.burst))   # il s'exécute jusqu'au bout
        temps += p.burst                           # l'horloge avance de la durée du burst
    return gantt
