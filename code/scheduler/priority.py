"""
Ordonnancement par priorité, non préemptif (plus petit nombre = plus prioritaire).
Renvoie un Gantt : liste de (pid, debut, fin).
"""


def priority(procs):
    """Ordonnancement par priorité, non préemptif.

    procs : liste de tuples (pid, arrivee, burst, priorite)
    Convention : PLUS PETIT NOMBRE = PRIORITÉ PLUS HAUTE.
    Égalité de priorité -> le premier arrivé passe en premier.
    Retour : liste de tuples (pid, debut, fin), avec "IDLE" pour les trous.
    """
    # 1. même squelette que SJF : restants, temps = 0, gantt = []
    restants = list(procs)
    temps = 0
    gantt = []

    # 2. tant qu'il reste des processus
    while restants:
        # prêts = ceux avec arrival <= temps
        prets = [p for p in restants if p[1] <= temps]

        # sinon IDLE jusqu'à la prochaine arrivée
        if not prets:
            prochaine = min(p[1] for p in restants)
            gantt.append(("IDLE", temps, prochaine))
            temps = prochaine
            continue

        # plus petit `priority` (égalité -> arrivée la plus tôt)
        p = min(prets, key=lambda x: (x[3], x[1]))
        pid, arrivee, burst, _ = p

        gantt.append((pid, temps, temps + burst))
        temps += burst
        restants.remove(p)

    # 3. renvoyer gantt
    return gantt


def moyennes(procs, gantt):
    """Renvoie (attente moyenne, séjour moyen)."""
    fin = {pid: f for pid, _, f in gantt if pid != "IDLE"}
    sejours = [fin[pid] - arr for pid, arr, _, _ in procs]
    attentes = [fin[pid] - arr - burst for pid, arr, burst, _ in procs]
    n = len(procs)
    return sum(attentes) / n, sum(sejours) / n