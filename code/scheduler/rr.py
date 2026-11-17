
from collections import deque

def rr(procs, quantum):
    """Exécute chaque processus au plus `quantum` unités à tour de rôle. Renvoie le Gantt.

    procs : liste de Process (comme les autres ordonnanceurs)
    Retour : liste de tuples (pid, debut, fin), avec "IDLE" pour les périodes d'inactivité.
    """
    # 1. trier par arrivée ; reste = {pid: burst} ; file = deque() ; temps = 0
    procs = sorted(((p.pid, p.arrival, p.burst) for p in procs), key=lambda p: p[1])   # Process -> tuples
    reste = {pid: burst for pid, _, burst in procs}
    file = deque()
    gantt = []
    temps = 0
    i = 0  # index du prochain processus à arriver
    n = len(procs)

    # 2. ajouter à la file les processus arrivés à temps 0
    while i < n and procs[i][1] <= temps:
        file.append(procs[i][0])
        i += 1

    # 3. tant qu'il reste du travail
    while file or i < n:
        # file vide -> IDLE jusqu'à la prochaine arrivée
        if not file:
            prochaine = procs[i][1]
            gantt.append(("IDLE", temps, prochaine))
            temps = prochaine
            while i < n and procs[i][1] <= temps:
                file.append(procs[i][0])
                i += 1
            continue

        p = file.popleft()
        duree = min(quantum, reste[p])
        gantt.append((p, temps, temps + duree))
        temps += duree
        reste[p] -= duree

        # d'abord les processus arrivés pendant cette tranche
        while i < n and procs[i][1] <= temps:
            file.append(procs[i][0])
            i += 1

        # PUIS on remet p en fin de file s'il n'a pas fini
        if reste[p] > 0:
            file.append(p)

    # 4. renvoyer gantt
    return gantt